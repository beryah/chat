from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory, listenWS
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File
import requests, json, time, sys, logging, logging.handlers, threading
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
threads = {}
datetime_format = "%Y-%m-%d %H:%M:%S.%f"
#logger.addHandler(consoleHandler)
#observer = log.PythonLoggingObserver()
#observer.start()

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
        # logger.debug("request.host:{0}".format(request.host))
        # logger.debug("request.path:{0}".format(request.path))
        # logger.debug("request.params:{0}".format(request.params))
        # logger.debug("request.version:{0}".format(request.version))
        # logger.debug("request.origin:{0}".format(request.origin))
        # logger.debug("request.protocols:{0}".format(request.protocols))
        # logger.debug("request.extensions:{0}".format(request.extensions))
        self.factory.register(self)
        logger.debug("Factory register: {0}".format(request.peer))

    def onOpen(self):
        logger.debug("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            logger.debug("Binary message received: {0} bytes".format(len(payload)))
            self.sendMessage(payload, isBinary)
        else:
            decode_payload = payload.decode('utf8')            
            logger.debug("payload.decode('utf8'): {0}".format(payload.decode('utf8')))
            tsew_command = json.loads(decode_payload)
            if tsew_command['tsew_command'] == "get_token":                
                r = get_token(tsew_command['content'], self)
                logger.debug("aaaa reponse {0}".format(r))
                tsew_command['content'] = r
                response = tsew_command
                #response = {'tsew_command':'get_token','status':'ok','token':'99999','clientId':'michaelclient'}
            else:
                r = command(tsew_command['content'], self)
                logger.debug("command reponse {0}".format(r))
                tsew_command['content'] = r
                response = tsew_command
                #logger.debug("Text message received: {0}".format(payload.decode('utf8')))
            logger.debug("response: {0}".format(json.dumps(response)))            
            self.sendMessage(json.dumps(response),isBinary)
        # echo back message verbatim

    def onClose(self, wasClean, code, reason):
        logger.debug("WebSocket connection closed: {0}".format(reason))

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)

def get_token(to_as_data, ws):
    register_url = 'http://{0}/api/as/v2/session/register'.format('10.206.132.8')
    rtext = http_request(register_url, to_as_data, desc = 'get_token')    
    data = json.loads(rtext)        
    get_token_ready(data, to_as_data['clientId'], to_as_data['supportId'], 'DLS', ws)    
    return data

def get_token_ready(data, clientId, supportId, source, ws):
    token_id = data['token']
    session_id = data['sessionId']
    support_id = supportId
    client_id = clientId
    key = 'as_' + str(token_id) + '_' + str(session_id)    
    threads[key] = {'status': 'running', 'first_time':datetime.utcnow(), 'terminate_time': None}
    threading.Thread(target=polling_as, args=(token_id, session_id, support_id, client_id, source, ws), name=key).start()        

def polling_as(token_id, session_id, support_id, client_id, source, ws):
    tmp_support_id = support_id
    to_as = {"sessionId":session_id,"token":token_id,"supportId":tmp_support_id,"seq":1000,"clientId":client_id}
    terminated = False
    first_polling_time = time.time()
    last_polling_time = time.time()
    timeout_count = 0
    index = 0
    while not terminated:
        key = 'as_' + str(token_id) + '_' + str(session_id)

        if index == 0:
            to_as['seq'] = 0
        ts = threads
        if key in ts:
            if ts[key]['status'] == 'terminate':
                terminated = True
                logger.debug("[POLLING][{0}] Threads[{0}] going to exit.".format(key))                
                continue
        else:
            logger.debug("[POLLING][{0}] Threads[{0}] not existing.".format(key))

        logger.debug("[POLLING][{0}] Query AirSupport for Terminate (session/status), index:{1}".format(key, index))
        logger.debug("[POLLING][{0}] Query AirSupport for Terminate (session/status), timespan from start:{1}".format(key, (time.time() - first_polling_time)))
        logger.debug("[POLLING][{0}] Query AirSupport for Terminate (session/status), timespan:{1}".format(key, (time.time() - last_polling_time)))
        if (time.time() - last_polling_time) > 119 and (time.time() - first_polling_time) > 15:
            logger.debug("[POLLING][{0}] Query AirSupport for Terminate (session/status) begin".format(key))

            status_url = ''
            status_url = 'http://{0}/api/as/v2/session/status'.format('10.206.132.8')

            r_desc = key + "][status polling_index:{0}".format(index)
            rtext = http_request(status_url, to_as, desc = r_desc)
            logger.debug("[POLLING][{0}] Query AirSupport for Terminate (session/status) done".format(key))
            try:
                status_data = json.loads(rtext)
                if status_data['status'] is not None:
                    if status_data['status'] == "OK":
                        if status_data['session'] == "TERMINATED":
                            if key not in transfer_case:
                                logger.debug("[POLLING][{0}] Query AirSupport for Terminate, terminate signal:{1}".format(key,rtext))
                                terminated =True
                                logger.debug("[POLLING][{0}] Threads[{0}] going to exist.".format(key))
                            else:
                                logger.debug("[POLLING][{0}] change support {1} to {2}".format(key, tmp_support_id, transfer_case[key]['toSupportId']))
                                tmp_support_id = transfer_case[key]['toSupportId']
                                del transfer_case[key]
                    elif status_data['code'] == "SESSION_NOT_FOUND":
                        if key not in transfer_case:
                            logger.debug("[POLLING][{0}] Query AirSupport for Terminate, terminate signal:{1}".format(key,rtext))
                            terminated =True
                            logger.debug("[POLLING][{0}] Threads[{0}] going to exist.".format(key))
                        else:
                            logger.debug("[POLLING][{0}] change support {1} to {2}".format(key, tmp_support_id, transfer_case[key]['toSupportId']))
                            tmp_support_id = transfer_case[key]['toSupportId']
                            del transfer_case[key]                            
                    else:
                        logger.debug("[POLLING][{0}] Query AirSupport for Terminate, error:{1}".format(key,rtext))

                    if terminated:        
                        if key in ts:                               
                            ts[key]['status'] = "terminate"
                        else:
                            logger.debug("[POLLING][{0}] can't find key in thread it could be terminate by command api".format(key))
                        
            except Exception as e:
                logger.debug("[POLLING][{0}] Query AirSupport for Terminate, exception:{1}, [{2}]".format(key,rtext, e))

        #time.sleep(0.3)
        logger.debug("[POLLING][{0}][index:{1}] Query AirSupport".format(key, index))
        last_polling_time = time.time()
        getStatus_url = 'http://{0}/api/as/v2/status/getStatus'.format('10.206.132.8')
        r_desc = key + '][getStatus polling_index:{0}'.format(index)
        rtext = http_request(getStatus_url, to_as, desc=r_desc, slack_notify=False)                
        rdata = json.loads(rtext)
        ws_rp = {}
        ws_rp['content'] = rdata
        ws_rp['tsew_command'] = 'getStatus'
        ws.sendMessage(json.dumps(ws_rp),False)
        logger.debug("[POLLING][{0}] Query AirSupport done".format(key))
        if rtext == 'timeout':
            timeout_count += 1
            continue
        else:
            timeout_count = 0

        #logger.debug('[polling_as] get status:{0}'.format(rtext))
        
        start_time = time.time()
       

        logger.debug("[POLLING][{0}] update tsew time:{1}".format(key,(time.time() - start_time)))
        index += 1

def http_request(url, to_as, timeout=180, desc='', slack_notify = True):
    try:
        r = requests.post(url, json=to_as)     
        logger.debug("[RRRRRRRRRRRR] {0}".format(r.text))       
        if r.status_code == 408:
            return 'timeout'
        return r.text
    except requests.exceptions.ReadTimeout:
        return 'timeout'
    except requests.exceptions.Timeout:
        return 'timeout'
    except requests.exceptions.ConnectionError as ce:
        if 'Connection aborted.' in ce.message:
            return 'timeout'
        else:            
            return 'timeout'
    except Exception:       
        raise

def command(to_as_data, ws):   
    to_as = to_as_data
    key = 'as_' + str(to_as['token']) + '_' + str(to_as['sessionId'])
    post_url = 'http://{0}/api/as/v2/command/post'.format('10.206.132.8')
    r_desc ="{0}][command]".format(key)
    rtext = http_request(post_url, to_as, desc = r_desc)    
    data = json.loads(rtext)
    logger.debug('[{1}] command data:{0}'.format(data, key))
    return rtext

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
    c = reactor.listenTCP(9010, factory)
    
    try:
        reactor.run()
    finally:
        c.stopListening()