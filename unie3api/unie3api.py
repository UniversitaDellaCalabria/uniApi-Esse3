import base64
import json
import requests


def e3_basic_token(username, password):
    _upseq = ':'.join((username, password))
    return base64.b64encode(_upseq.encode('utf-8')).decode()


class uniE3Api(object):

    def __init__(self, base_url, token='', **kwargs):
        _username = kwargs.get('username')
        _password = kwargs.get('password')
        self.token = token or e3_basic_token(_username, _password)
        self.base_url = base_url

    def get(self, url):
        headers = {'Authorization': 'Basic {}'.format(self.token)}
        req = requests.get(url, headers=headers)
        if not req.status_code == 200:
            raise Exception(req.json())
        return req.json()

    def carriera(self, codice_fiscale):
        _url = self.base_url + '/anagrafica-service-v2/carriere?codFis={}'
        return self.get(_url.format(codice_fiscale.upper()))

    def anagrafica(self, codice_fiscale):
        _url = self.base_url + '/anagrafica-service-v2/utenti/{}/trattiAttivi'
        return self.get(_url.format(codice_fiscale.lower()))

    def attivo(self, codice_fiscale):
        """
        ordCod = CS-0001-01 -> corsi singoli

        torna lo stato attuale se attivo, altrimento None
        """
        tratti = self.anagrafica(codice_fiscale)
        tratto = {}
        for i in tratti:
            if not tratto.get('aaId'):
                tratto = i
                continue
            if i['staStuCod'] == 'A' and i['aaId'] >= tratto.get('aaId'):
                tratto = i

        if tratto['statoTasse'] and tratto['staStuCod'] == 'A' and \
           not tratto['dataChiusura'] and tratto['ordCod'] != 'CS-0001-01':
            return tratto
