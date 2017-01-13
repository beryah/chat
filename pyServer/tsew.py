#/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import zipfile
import json
import time
import os
import logging
import logging.handlers
import threading
from datetime import datetime

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


def http_request(url, to_as, timeout=180, desc='', slack_notify=True):
    try:
        from_as = requests.post(url, json=to_as)
        #logger.debug("http_request {0}".format(from_as.text))
        if from_as.status_code == 408:
            return 'timeout'
        return from_as.text
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


def register(to_as, ws):
    url = 'http://{0}/api/as/v2/session/register'.format('10.206.132.8')
    from_as = json.loads(http_request(url, to_as, desc='get_token'))
    to_as['token'] = from_as['token']
    to_as['sessionId'] = from_as['sessionId']
    start_polling(to_as, ws)
    return from_as


def start_polling(to_as, ws):
    key = getKey(to_as['token'], to_as['sessionId'])
    threads[key] = {'status': 'running', 'first_time': datetime.utcnow(), 'terminate_time': None}
    threading.Thread(target=polling, args=(
        to_as['token'],
        to_as['sessionId'],
        to_as['supportId'],
        to_as['clientId'],
        to_as['sessionId'],
        ws), name=key).start()


def polling(token_id, session_id, support_id, client_id, source, ws):
    tmp_support_id = support_id
    to_as = {"sessionId": session_id, "token": token_id,
             "supportId": tmp_support_id, "seq": 1000, "clientId": client_id}
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
                logger.debug(
                    "[POLLING][{0}] Threads[{0}] going to exit.".format(key))
                continue
        else:
            logger.debug(
                "[POLLING][{0}] Threads[{0}] not existing.".format(key))

        logger.debug(
            "[POLLING][{0}] Query AirSupport for Terminate (session/status), index:{1}".format(key, index))
        logger.debug("[POLLING][{0}] Query AirSupport for Terminate (session/status), timespan from start:{1}".format(
            key, (time.time() - first_polling_time)))
        logger.debug("[POLLING][{0}] Query AirSupport for Terminate (session/status), timespan:{1}".format(
            key, (time.time() - last_polling_time)))
        if (time.time() - last_polling_time) > 119 and (time.time() - first_polling_time) > 15:
            logger.debug(
                "[POLLING][{0}] Query AirSupport for Terminate (session/status) begin".format(key))

            status_url = ''
            status_url = 'http://{0}/api/as/v2/session/status'.format(
                '10.206.132.8')

            r_desc = key + "][status polling_index:{0}".format(index)
            rtext = http_request(status_url, to_as, desc=r_desc)
            logger.debug(
                "[POLLING][{0}] Query AirSupport for Terminate (session/status) done".format(key))
            try:
                status_data = json.loads(rtext)
                if status_data['status'] is not None:
                    if status_data['status'] == "OK":
                        if status_data['session'] == "TERMINATED":
                            if key not in transfer_case:
                                logger.debug(
                                    "[POLLING][{0}] Query AirSupport for Terminate, terminate signal:{1}".format(key, rtext))
                                terminated = True
                                logger.debug(
                                    "[POLLING][{0}] Threads[{0}] going to exist.".format(key))
                            else:
                                logger.debug("[POLLING][{0}] change support {1} to {2}".format(
                                    key, tmp_support_id, transfer_case[key]['toSupportId']))
                                tmp_support_id = transfer_case[
                                    key]['toSupportId']
                                del transfer_case[key]
                    elif status_data['code'] == "SESSION_NOT_FOUND":
                        if key not in transfer_case:
                            logger.debug(
                                "[POLLING][{0}] Query AirSupport for Terminate, terminate signal:{1}".format(key, rtext))
                            terminated = True
                            logger.debug(
                                "[POLLING][{0}] Threads[{0}] going to exist.".format(key))
                        else:
                            logger.debug("[POLLING][{0}] change support {1} to {2}".format(
                                key, tmp_support_id, transfer_case[key]['toSupportId']))
                            tmp_support_id = transfer_case[key]['toSupportId']
                            del transfer_case[key]
                    else:
                        logger.debug(
                            "[POLLING][{0}] Query AirSupport for Terminate, error:{1}".format(key, rtext))

                    if terminated:
                        if key in ts:
                            ts[key]['status'] = "terminate"
                        else:
                            logger.debug(
                                "[POLLING][{0}] can't find key in thread it could be terminate by command api".format(key))

            except Exception as e:
                logger.debug(
                    "[POLLING][{0}] Query AirSupport for Terminate, exception:{1}, [{2}]".format(key, rtext, e))

        # time.sleep(0.3)
        logger.debug(
            "[POLLING][{0}][index:{1}] Query AirSupport".format(key, index))
        last_polling_time = time.time()
        getStatus_url = 'http://{0}/api/as/v2/status/getStatus'.format(
            '10.206.132.8')
        r_desc = key + '][getStatus polling_index:{0}'.format(index)
        rtext = http_request(getStatus_url, to_as,
                             desc=r_desc, slack_notify=False)
        rdata = json.loads(rtext)
        ws_rp = {}
        ws_rp['content'] = rdata
        ws_rp['command'] = 'getStatus'
        ws.sendMessage(json.dumps(ws_rp), False)
        logger.debug("[POLLING][{0}] Query AirSupport done".format(key))
        if rtext == 'timeout':
            timeout_count += 1
            continue
        else:
            timeout_count = 0

        # logger.debug('[polling_as] get status:{0}'.format(rtext))

        start_time = time.time()

        logger.debug("[POLLING][{0}] update tsew time:{1}".format(
            key, (time.time() - start_time)))
        index += 1


def command(to_as_data, ws):
    to_as = to_as_data
    key = getKey(to_as['token'], to_as['sessionId'])
    post_url = 'http://{0}/api/as/v2/command/post'.format('10.206.132.8')
    r_desc = "{0}][command]".format(key)
    rtext = http_request(post_url, to_as, desc=r_desc)
    data = json.loads(rtext)
    logger.debug('[{1}] command data:{0}'.format(data, key))
    return rtext


def terminate(to_as, ws):
    key = getKey(to_as["token"], to_as["sessionId"])
    url = 'http://{0}/api/as/v2/session/terminate'.format('10.206.132.8')
    from_as = json.loads(http_request(url, to_as, desc=key))

    if key in threads:
        if threads[key] is not None:
            threads[key]['status'] = 'terminate'

    return from_as


def get_new_case(ws):
    while (ws.stop_get_new_case()):
        url = 'http://{0}/api/as/v2/command/fetchTukas'.format('10.206.132.8')
        from_as = json.loads(http_request(url, None))
        print 'grab case polling'
        if from_as['tuka'] is not None and len(from_as['tuka']) > 0:
            print from_as
            from_as['tuka'][0]['imgurl'] = download_s3_file(from_as['tuka'][0]["token"], from_as['tuka'][0]["sessionId"], from_as['tuka'][0]["issue"][0]["seq"], from_as['tuka'][0]["issue"][0]["content"]["url"])
            payload = {}
            payload['command'] = 'newCase'
            payload['content'] = from_as
            ws.broadcast(json.dumps(payload))

        time.sleep(1)


def download_s3_file(token, sessionId, seq, url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open('../src/assets/s3ZipFile/{0}_{1}.zip'.format(token, sessionId), 'wb') as output:
            output.write(r.content)

        with zipfile.ZipFile('../src/assets/s3ZipFile/{0}_{1}.zip'.format(token, sessionId), 'r') as zf:
            zf.extractall(pwd='virus', path='../src/assets/s3File/{0}_{1}/{2}'.format(token, sessionId, seq))
        
        for file in os.listdir('../src/assets/s3File/{0}_{1}/{2}'.format(token, sessionId, seq)):
            if file.endswith(".jpg"): 
                return '../src/assets/s3File/{0}_{1}/{2}/{3}'.format(token, sessionId, seq, file)
                break
    else:
        return None     

def getKey(token, sessionId):
    return "as_{0}_{1}".format(token, sessionId)

