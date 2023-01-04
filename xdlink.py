import requests
import json
from bs4 import BeautifulSoup

#def parse(urls):
#    requrl = 'https://moodle-tools.netlify.app/.netlify/functions/encode-xd-url'
#    jsondata = {'urls':urls}
#    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#    resp = requests.post(requrl,data=json.dumps(jsondata),headers=headers)
#    return parsejson(resp.text)

def parse(urls):
    api = 'https://xd-core-api.onrender.com/xdlinks/encode'
    print('En el XDLINK')
    jsondata = {'channelid':'','urls':urls}
    resp = requests.post(api,data=json.dumps(jsondata),headers={ "Content-Type": "application/json",
                                                                'Accept': '*/*',
                                                                'Origin':'https://xdownloader.surge.sh',
                                                                'Referer':'https://xdownloader.surge.sh/'})
    jsonresp = json.loads(resp.text)
    if 'data' in jsonresp:
        print(jsonresp['data'])
        return jsonresp['data']
    return None
