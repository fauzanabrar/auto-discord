from twocaptcha import TwoCaptcha
import string
import time
import requests
import json
import random
import os

# url = 'https://cdn.discordapp.com/attachments/1025838862649540629/1027169472798277663/captcha.png'
auth = "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ" #f
owoChat = 1025838862649540629

def solveChaptcha(url):
  solver = TwoCaptcha('d48130f88087c7b46fae7ef52dff8f6a')
  # url = 'https://cdn.discordapp.com/attachments/1025838862649540629/1027169472798277663/captcha.png'
  result = solver.normal(url, caseSensitive=1)

  return result['code']


def retrieve_message(channelId, row=0):
  header = {
    'authorization': auth
  }
  r = requests.get(
    f'https://discord.com/api/v8/channels/{channelId}/messages', headers=header
  )

  # print(r.text)
  jsonn = json.loads(r.text)
  # cusId = jsonn[0]['components'][0]["components"][0]['custom_id']
  # print(json.dumps(jsonn,indent=4))
  # print(jsonn[0]['content'])
  # print(jsonn[0]['components'][0]["components"][0]['custom_id'])
  # for value in jsonn:
  #   print(value)
  # print(jsonn)
  if row != 0:
    return jsonn[0:row]

  return jsonn[0]

def sendMessage(channel_id, message):
  url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
  data = {"content": message}
  header = {"authorization": auth}
  r = requests.post(url, data=data, headers=header)
  return r.status_code

res = retrieve_message(owoChat,row = 3)
print(res)
url = res[0]['attachments'][0]['url']
sendMessage(owoChat, solveChaptcha(url))