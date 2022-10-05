import string
import time
import requests
import json
import random
import os


auth = "NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA"



tatsu = 1020999184091975700
fishTatsu = 1020999184091975700
genTatsu = 1020999184091975700
dank = 1020998895960084530
owo = 1023873700308729866

urlMsg = "https://discord.com/api/v9/channels/1019193416254496778/messages"
# auth = 'NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA'
# auth = 'MTAyMDcyMDEwODI0ODc2MDM3MQ.G1vG_z.L-ore_flev_1Hz4d38_L30Kdmu4c5oB9yMH47M'
# auth = 'MTAyMDcyMDEwODI0ODc2MDM3MQ.Gsr4cf.uq_UOe0qWT7wV070hl-B4_x1O_xfUNwc2T50EM'
# auth = 'MTAyMDc0MTcxNTIyMjYwMTgxOA.GzRgJ5.c3VBAqB3sYeQ3Y5znanlorNJSEGaEfwkuDiASQ'
# auth = 'MTAyMDk3MTk3OTE0ODM2OTk1MA.GqRzVL.DyrtXLkDkZouQPCdlFaQbJBUTEn7Jv1pLzH4Gk'



def retrieve_message(channelId):
  header = {
    'authorization' : auth
  }
  r = requests.get(
    f'https://discord.com/api/v8/channels/{channelId}/messages', headers=header
  )

  jsonn = json.loads(r.text)
  # cusId = jsonn[0]['components'][0]["components"][0]['custom_id']
  # print(json.dumps(jsonn,indent=4))
  # print(jsonn[0]['content'])
  # print(jsonn[0]['components'][0]["components"][0]['custom_id'])
  # for value in jsonn:
  #   print(value)
  return jsonn[0]['content']

def sendMessage(channel_id, message):
  url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
  data = {"content": message}
  header = {"authorization": auth}
  r = requests.post(url, data=data, headers=header)
  return r.status_code

def confirm(channel):
  status = sendMessage(channel, "confirm")
  time.sleep(20)

def train(n, seconds):
  for i in range(n):
    status = sendMessage(tatsu, "t!tg train")
    print(i+1," status train : ", status)
    if(seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8),seconds))

def walk(n, seconds):
  for i in range(round(n/2)):
    status = sendMessage(tatsu, "t!tg feed")
    time.sleep(random.randint(12,20))
    print(i + 1, " status feed : ", status)
    status = sendMessage(tatsu, "t!tg walk")
    time.sleep(random.randint(12,20))
    print(i + 1, " status walk : ", status)
    status = sendMessage(tatsu, "t!tg walk")
    time.sleep(random.randint(12,20))
    print(i + 1, " status walk : ", status)
    if (seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8), seconds))

def fish(n, seconds):
  for i in range(n):
    status = sendMessage(fishTatsu, "t!fish")
    print(i + 1, " status fish : ", status)
    if (seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8), seconds))

def slot(n, seconds):
  for i in range(n):
    status = sendMessage(genTatsu, "t!slot")
    print(i + 1, " status slot : ", status)
    if (seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8), seconds))

def cookie(n, seconds):
  for i in range(n):
    status = sendMessage(genTatsu, "t!cookie tatsu")
    print(i + 1, " status cookie : ", status)
    if (seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8), seconds))

def claim_mail():
  status = sendMessage(genTatsu, "t!mail claim all")
  print(" status claim mail : ", status)
  time.sleep(10)

def open():
  status = sendMessage(genTatsu, "t!open")
  print(" status open : ", status)
  time.sleep(10)
  status = sendMessage(genTatsu, "1")
  time.sleep(10)
  confirm(genTatsu)
  status = sendMessage(genTatsu, "6")
  time.sleep(10)
  confirm(genTatsu)

def pet_active():
  status = sendMessage(genTatsu, "t!tg edit")
  print(" status active : ", status)
  time.sleep(10)
  status = sendMessage(genTatsu, "1")
  time.sleep(10)
  status = sendMessage(genTatsu, "1")
  time.sleep(10)
  status = sendMessage(genTatsu, "1")
  time.sleep(10)


def daily():
  status = sendMessage(genTatsu, "t!daily")
  print(" status daily : ", status)
  time.sleep(10)


def exchange():
  status = sendMessage(genTatsu, "t!exchange")
  print(" status daily : ", status)
  time.sleep(10)
  status = sendMessage(genTatsu, "1")
  time.sleep(10)
  status = sendMessage(genTatsu, "add 1")
  time.sleep(10)
  status = sendMessage(genTatsu, "4")
  time.sleep(10)
  confirm(genTatsu)


def trade(user, amount):
  status = sendMessage(genTatsu, "t!trade")
  print(" status daily : ", status)
  time.sleep(10)
  status = sendMessage(genTatsu, "1")
  time.sleep(10)
  status = sendMessage(genTatsu, user)
  time.sleep(10)
  status = sendMessage(genTatsu, "add send")
  time.sleep(10)
  status = sendMessage(genTatsu, "2")
  time.sleep(10)
  status = sendMessage(genTatsu, "1")
  time.sleep(10)
  confirm(genTatsu)



def vote():
  status = sendMessage(genTatsu, "t!vote")
  print(" status vote : ", status)
  time.sleep(10)

def quest():
  # train(15,12)
  # walk(6,12)
  fish(10,40)
  # slot(10,12)
  cookie(10,12)
  status = sendMessage(genTatsu, "t!quest claim")
  print(" status quest : ", status)
  time.sleep(10)

def start():
  # claim_mail()
  # open()
  # pet_active()
  # quest()
  # daily()
  auto()
  # exchange()
  # trade("leghorn", 2000)

def auto_slot_owo(bet,seconds):
  new_bet = bet
  win = 0
  while True:
    time.sleep(random.randint(3, 5))
    print(sendMessage(owo, f"wh"))
    time.sleep(random.randint(3, 5))
    print(sendMessage(owo, f"wcf {new_bet}"))
    time.sleep(random.randint(round(seconds * 0.8), seconds))
    res = str(retrieve_message(owo))
    # print(res)

    if " captcha " in res :
      print("Bot paused because captcha")
      time.sleep(4*3600)

    if " lost " in res:
      print("lost")
      new_bet*=5
    elif " won " in res:
      print("won")
      new_bet = bet
      win+=1

    if win == 5:
      print(f"Bot paused because had won {win} times")
      win = 0
      time.sleep(1*3600)


def auto():
  seconds = 60
  n = 100
  choose = 1
  while True:
    if choose == 1:
      train(n, seconds)
    elif choose == 2:
      walk(n, seconds)
    elif choose == 3:
      fish(n, seconds)
    elif choose == 4:
      slot(n, seconds)

# 1k, 2k, 4k, 12k, 30k, 100k, 150k
def new_slot():
  new_bet = [10,20,40,120,300,1000,1500, 5000, 15000]
  seconds = 25
  win = 0
  lose = 0
  while True:
    print(sendMessage(owo, f"wcf {new_bet[lose]}"))
    time.sleep(random.randint(round(seconds * 0.8), seconds))
    res = str(retrieve_message(owo))
    # print(res)

    check_captcha2(res)


    if lose > 9:
      lose = 0

    if " lost " in res:
      print("lost", lose)
      lose += 1

    elif " won " in res:
      print("won", win)
      win += 1
      lose = 0

    if win == 5:
      print(f"Bot paused because had won {win} times")
      win = 0
      break

    randomCmd()


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

def check_captcha():
  res = str(retrieve_message(owo))
  # print(res)

  if " captcha " in res:
    print("Bot paused because captcha")
    time.sleep(4 * 3600)

def check_captcha2(res):
  if " captcha " in res:
    print("Bot paused because captcha")
    time.sleep(4 * 3600)

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


i = 1
while True:
  if i % 20 == 0:
    time.sleep(1*3600)

  for i in range(random.randint(10,50)):
    check_captcha()
    if random.randint(0,30)> 70:
      print(i, " wb ", wb())
      time.sleep(random.randint(5,10))
    print(i, " wh ", wh())
    time.sleep(random.randint(5,10))
    randomCmd()
    time.sleep(random.randint(5, 10))
    time.sleep(random.randint(13,25))
  time.sleep(random.randint(5, 60))
  new_slot()
  time.sleep(random.randint(150, 2*200))

  i+=1

