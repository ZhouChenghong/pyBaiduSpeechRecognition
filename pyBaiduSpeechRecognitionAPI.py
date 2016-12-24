#coding=utf-8

import myBaiduVoiceKey as myKey
import urllib.request
import json
import os
import base64

serverURL   = "http://vop.baidu.com/server_api"
getTokenURL = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials" + "&client_id=" + myKey.apiKey + "&client_secret=" + myKey.secretKey;

url_test = "https:www.sbdyubsfyubydubfyubfyb.com"

try:
    url_data = urllib.request.urlopen(getTokenURL).read().decode('ascii')
except HTTPError as e:
    print('''The server couldn't fulfill the request.''')
    print('Error code: ',e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ',e.reason)
else:
    print("Get token!")
    token = eval(url_data)
    access_token = token["access_token"]
    for k,v in token.items():
        print("%s\t:\t%s"%(k,v))
    print(access_token)

os.chdir("voice")
voice = open("test.pcm",'rb')
print(voice)

speech_data = voice.read()
speech_base64=base64.b64encode(speech_data).decode('utf-8')
speech_length=len(speech_data)
data_dict = {'format':'pcm','rate':8000, 'channel':'1', 'cuid':myKey.appID, 'token':access_token, 'lan':'zh', 'speech':speech_base64, 'len':speech_length}
json_data = json.dumps(data_dict).encode('utf-8')
json_length = len(json_data)
request = urllib.request.Request(serverURL)
request.add_header("Content-Type","application/json")
request.add_header("Content-Length",json_length)
fs = urllib.request.urlopen(url=request, data=json_data)

result_str = fs.read().decode('utf-8')
json_resp = json.loads(result_str)

print(type(json_resp))
for k,v in json_resp.items():
        print("%s\t:\t%s"%(k,v))
