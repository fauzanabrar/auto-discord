import string
import time
import requests
import json
import random
import os


# auth = "NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA"
auth = "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ" #f

owoChannel = [1023873700308729866,1026703938344460298,1026704288925364324,1026704327206772826,1026704357888102410,1026704382873579551]
owo = random.choice(owoChannel)
owo = 1025838862649540629

urlMsg = "https://discord.com/api/v9/channels/1019193416254496778/messages"


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

def check_captcha():
  print("check captcha")
  res = retrieve_message(owo)
  if 'content' in res:

    content = str(res['content'])
    if " captcha " in content:
      print("Bot paused because captcha")
      time.sleep(4 * 3600)
  else:
    print("content tidak ditemukan")
    print(res)



def check_captcha2(res):
  print("check captcha")
  if 'content' in res:
    content = str(res['content'])
    if " captcha " in content:
      print("Bot paused because captcha")
      time.sleep(4 * 3600)
  else:
    print("content tidak ditemukan")
    print(res)


def check(func):
    '''Decorator that check chaptcha after use command.'''

    def wrap(*args, **kwargs):
      r = func(*args, **kwargs)
      time.sleep(2)
      check_captcha()
      return r
    return wrap

# @check
def sendMessage(channel_id, message):
  url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
  # url = "https://discord.com/api/v9/channels/1021798935548936272/messages"
  data = {"content": message}
  header = {"authorization": auth}
  r = requests.post(url, data=data, headers=header)
  return r.status_code


def wh():
  status = sendMessage(owo, "wh")
  return status

def wb():
  status = sendMessage(owo, "wb")
  return status

def wpray():
  status = sendMessage(owo, "wpray")
  return status

def wcash():
  status = sendMessage(owo, "wcash")
  return status

def randomChat():
  chat = "".join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase+string.whitespace, k=random.randint(4,20)))
  status = sendMessage(owo, f'{chat}')
  return status

def wq():
  status = sendMessage(owo, "wq")
  return status


def wlevel():
  status = sendMessage(owo, "wlevel")
  return status

def ww():
  status = sendMessage(owo, "ww")
  return status

def winv():
  status = sendMessage(owo, "winv")
  return status

def wz():
  status = sendMessage(owo, "wz")
  return status

def sayOwo():
  status = sendMessage(owo, "owo")
  return status

# 1k, 2k, 4k, 12k, 30k, 100k, 150k
def new_slot():
  new_bet = [10,30,90,200,500,1200,2700, 6000, 15000, 50000, 150000]
  seconds = 25
  win = 0
  lose = 0
  while True:
    print(sendMessage(owo, f"wcf {new_bet[lose]}"))
    time.sleep(random.randint(round(seconds * 0.8), seconds))
    res = retrieve_message(owo,10)

    if lose > len(new_bet):
      lose = 0

    for i in res:
      content = str(i['content'])

      if " lost " in content:
        print("lost", lose)
        lose += 1
        break
      elif " won " in content:
        print("won", win)
        win += 1
        lose = 0
        break


    if win == 2:
      print(f"Bot paused because had won {win} times")
      win = 0
      break

    randomCmd()

def randomCmd():
  n = random.randint(0,1000)

  if n < 100:
    wcash()
  elif n < 150:
    wpray()
  elif n < 200:
    randomChat()
  elif n < 300:
    wq()
  elif n < 400:
    wb()
  elif n < 500:
    wh()
  elif n < 600:
    wlevel()
  elif n < 700:
    ww()
  elif n < 800:
    wz()
  elif n < 900:
    winv()
  elif n < 1000:
    sayOwo()

# sendMessage(owo,"ehe")
print(retrieve_message(owo, 3)[2]['attachments'][0]['url'])
# i = 1
# while True:
#   if i % 20 == 0:
#     time.sleep(1*3600)
#   check_captcha()
#   for i in range(random.randint(10,50)):
#     if random.randint(0,30)> 70:
#       print(i, " wb ", wb())
#       time.sleep(random.randint(5,10))
#     print(i, " wh ", wh())
#     time.sleep(random.randint(5,10))
#     randomCmd()
#
#     time.sleep(random.randint(5, 10))
#     time.sleep(random.randint(13,25))
#
#
#   new_slot()
#   time.sleep(random.randint(5, 10))
#   r = random.choice(owoChannel)
#   while r == owo:
#     r = random.choice(owoChannel)
#
#   owo = r
#
#   time.sleep(random.randint(150, 2*200))
#   i+=1
