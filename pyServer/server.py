from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory, listenWS
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File
import requests, json, time, threading, sys, signal, os, logging, logging.handlers, urllib
import json
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
logger.addHandler(consoleHandler)
observer = log.PythonLoggingObserver()
observer.start()
class BroadcastServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.register(self)
    def onMessage(self, payload, isBinary):
        if not isBinary:
            msg = "{} from {}".format(payload.decode('utf8'), self.peer)
            self.factory.broadcast(msg)
    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)
class MyServerProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        logger.debug("Client connecting: {0}".format(request.peer))
        logger.debug("request.host:{0}".format(request.host))
        logger.debug("request.path:{0}".format(request.path))
        logger.debug("request.params:{0}".format(request.params))
        logger.debug("request.version:{0}".format(request.version))
        logger.debug("request.origin:{0}".format(request.origin))
        logger.debug("request.protocols:{0}".format(request.protocols))
        logger.debug("request.extensions:{0}".format(request.extensions))
        self.factory.register(self)
        logger.debug("Factory register: {0}".format(request.peer))
    def onOpen(self):
        logger.debug("WebSocket connection open.")
    def onMessage(self, payload, isBinary):
        if isBinary:
            logger.debug("Binary message received: {0} bytes".format(len(payload)))
            self.sendMessage(payload, isBinary)
        else:
            a = payload.decode('utf8')
            logger.debug("payload.decode('utf8'): {0}".format(a))
            tsew_command = json.loads(a)
            logger.debug("payload.decode('utf8'): {0}".format(payload.decode('utf8')))
            if tsew_command['tsew_command'] == "get_token":
                response = {'seq_id':1,'content':'test success'}
            else:
                response = {'seq_id':1,'content':'content unknow'}
                #logger.debug("Text message received: {0}".format(payload.decode('utf8')))
            logger.debug("response: {0}".format(json.dumps(response)))            
            self.sendMessage(json.dumps(response),isBinary)
        # echo back message verbatim
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
    #from twisted.python import log
    from twisted.internet import reactor
    #log.startLogging(sys.stdout)
    #observer = log.PythonLoggingObserver(loggerName='aaaaa')
    #observer.start()
    factory = BroadcastServerFactory()
    factory.protocol = MyServerProtocol
    logger.debug("factory.protocol = MyServerProtocol")
    # factory.setProtocolOptions(maxConnections=2)
    # note to self: if using putChild, the child must be bytes...
    reactor.listenTCP(9006, factory)
    reactor.run()