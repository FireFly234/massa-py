import json
import requests


class RPC():
    def __init__(self, port, user, password, ip='127.0.0.1'):
        super(RPC, self).__init__()
        self.port = port
        self.user = user
        self.password = password
        self.ip = ip
        self.node_url = 'http://{ip}:{port}'.format(ip=self.ip, port=self.port)

    def call(self, method, *params):
        params = list(params)

        payload = json.dumps(
            {'jsonrpc': '2.0', 'method': method, 'params': params})

        try:
            responce = requests.post(
                self.node_url,
                auth=(self.user, self.password),
                data=payload,
                timeout=(1, 10)
            )
        except requests.exceptions.RequestException as e:
            print('Can not connect to {ip}:{port}\n (check allowip)'.format(
                ip=self.ip, port=self.port))
            print(e)
            return 1

        if responce.status_code == 200:
            return responce.json()['result']
        elif responce.status_code == 401:
            print('Wrong password')
        elif responce.status_code == 500:
            message = 'ERROR: {code}; {message}'.format(
                code=responce.json()['error']['code'],
                message=responce.json()['error']['message'],
            )
            print(message)
            return int(responce.json()['error']['code'])
        else:
            print('Undescribed error')
        # print(responce.status_code, responce.reason)
        return responce.status_code