from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory, listenWS
from twisted.internet import reactor
import requests
import json
import time
import sys
import logging
import logging.handlers
import threading
import tsew
from datetime import datetime
from gates import *

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler('tsew.log', "a", maxBytes=50000000, backupCount=10)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


class BroadcastServerProtocol(WebSocketServerProtocol):

    def onOpen(self):
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            msg = "{} from {}".format(payload.decode('utf8'), self.peer)
            logger.debug("BroadcastServerProtocol")
            self.factory.broadcast(msg)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        logger.debug("Client connecting: {0}".format(request.peer))
        self.factory.register(self)
        logger.debug("Factory register: {0}".format(request.peer))

    def onOpen(self):
        logger.debug("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            logger.debug(
                "Binary message received: {0} bytes".format(len(payload)))
            self.sendMessage(payload, isBinary)
        else:
            logger.debug("payload.decode('utf8'): {0}".format(payload.decode('utf8')))
            payload_obj = json.loads(payload.decode('utf8'))
            command, content = payload_obj['command'], payload_obj['content']

            if command == "get_token":
                command_rep = tsew.register(content, self)
            elif command == "command":
                command_rep = tsew.command(content, self)
            elif command = "terminate"
                command_rep = tsew.terminate(content, self)

            response = {}
            response['command'] = command
            response['content'] = command_rep
            logger.debug("response: {0}".format(json.dumps(response)))
            self.sendMessage(json.dumps(response), isBinary)

    def onClose(self, wasClean, code, reason):
        logger.debug("WebSocket connection closed: {0}".format(reason))

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):

    def __init__(self):
        WebSocketServerFactory.__init__(self)
        self.clients = []

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        print("broadcasting prepared message '{}' ..".format(msg))
        preparedMsg = self.prepareMessage(msg)
        for c in self.clients:
            c.sendPreparedMessage(preparedMsg)
            print("prepared message sent to {}".format(c.peer))

if __name__ == '__main__':
    import sys
    from twisted.internet import reactor
    factory = BroadcastServerFactory()
    factory.protocol = MyServerProtocol
    logger.debug("factory.protocol = MyServerProtocol")
    c = reactor.listenTCP(9010, factory)

    try:
        reactor.run()
    finally:
        c.stopListening()
