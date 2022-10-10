import time
import requests
import json
import random
import os


auth = "MTAyMzQzODQ2OTYyMTYyMDg1Nw.GQposd.457v3IY1XOH6Dyurv0nAp2sT6uwqdMa-qPMK_M"
username = "bayes4"


tatsu = 1025205942977056800


def retrieve_message(channelId, order=0):
  header = {
    'authorization' : auth
  }
  r = requests.get(
    f'https://discord.com/api/v8/channels/{channelId}/messages', headers=header
  )
  if order != 0:
    jsonn = json.loads(r.text)
    print(jsonn[0:order])
    return jsonn[0:order]
  jsonn = json.loads(r.text)
  print(jsonn[0])
  return jsonn[0]

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
    sendMessage(tatsu, f"train {i+1}")
    status = sendMessage(tatsu, "t!tg train")
    print(i+1," status train : ", status)
    if(seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8),seconds))

def walk(n, seconds):
  for i in range(round(n/2)):
    sendMessage(tatsu, f"walk {i + 1}")
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
  nfish = 0
  i = 0
  while nfish != n:
    sendMessage(tatsu, f"fish {i + 1}")
    status = sendMessage(tatsu, "t!fish")
    print(i + 1, " status fish : ", status)
    time.sleep(2)
    res = retrieve_message(tatsu,2)
    tfish = ""

    for j in range(len(res)):
      if (res[j]['content'] == "t!fish") and ((res[j]['author']['username']).lower() == username.lower()):
        tfish = j
        if j == 1:
          if "🐟" in res[j-1]["content"] or ("🐠" in res[j-1]["content"]) :

            nfish+=1
            print("yey ikan", nfish)


        # for k in range(j-1, 0, -1):
        #   print("masuk loop2")
        #   if "🐟" in res[k]["content"] or ("🐠" in res[k]["content"]):
        #
        #     nfish += 1
        #     print("yey ikan", nfish)
        #     break
    # print(res)
    if (seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8), seconds))
    i+=1


def slot(n, seconds):
  for i in range(n):
    sendMessage(tatsu, f"slot {i + 1}")
    status = sendMessage(tatsu, "t!slot")
    print(i + 1, " status slot : ", status)
    if (seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8), seconds))

def cookie(n, seconds):
  for i in range(n):
    sendMessage(tatsu, f"cookie {i + 1}")
    status = sendMessage(tatsu, "t!cookie tatsu")
    print(i + 1, " status cookie : ", status)
    if (seconds <= 10):
      time.sleep(seconds)
    else:
      time.sleep(random.randint(round(seconds * 0.8), seconds))

def claim_mail():
  status = sendMessage(tatsu, "t!mail claim all")
  print(" status claim mail : ", status)
  time.sleep(10)

def open():
  status = sendMessage(tatsu, "t!open")
  print(" status open : ", status)
  time.sleep(10)
  status = sendMessage(tatsu, "1")
  time.sleep(10)
  confirm(tatsu)
  status = sendMessage(tatsu, "6")
  time.sleep(10)
  confirm(tatsu)

def pet_active():
  status = sendMessage(tatsu, "t!tg edit")
  print(" status active : ", status)
  time.sleep(10)
  status = sendMessage(tatsu, "1")
  time.sleep(10)
  status = sendMessage(tatsu, "1")
  time.sleep(10)
  status = sendMessage(tatsu, "1")
  time.sleep(10)

def daily():
  status = sendMessage(tatsu, "t!daily")
  print(" status daily : ", status)
  time.sleep(10)

def exchange():
  status = sendMessage(tatsu, "t!exchange")
  print(" status daily : ", status)
  time.sleep(10)
  status = sendMessage(tatsu, "1")
  time.sleep(10)
  status = sendMessage(tatsu, "add 1")
  time.sleep(10)
  status = sendMessage(tatsu, "4")
  time.sleep(10)
  confirm(tatsu)

def trade(user, amount):
  status = sendMessage(tatsu, "t!trade")
  print(" status daily : ", status)
  time.sleep(10)
  status = sendMessage(tatsu, "1")
  time.sleep(10)
  status = sendMessage(tatsu, user)
  time.sleep(10)
  status = sendMessage(tatsu, "add send")
  time.sleep(10)
  status = sendMessage(tatsu, "2")
  time.sleep(10)
  status = sendMessage(tatsu, "1")
  time.sleep(10)
  confirm(tatsu)

def vote():
  status = sendMessage(tatsu, "t!vote")
  print(" status vote : ", status)
  time.sleep(10)

def check_quest():
  status = sendMessage(tatsu, "t!quest 1")
  time.sleep(1)
  res = retrieve_message(tatsu)
  walkTask = 0
  chatTask = 0
  fishTask = 0
  slotTask = 0
  cookieTask = 0
  trainTask = 0
  try:
    task = res['embeds'][0]['fields']
    if len(task) == 5:
      for i in task:
        print(i['name'])
        t = i['name']
        if "Walk" in t:
          walkTask = int(t.split()[3])
          # print(walkTask)
        elif " Chat" in t:
          chatTask = int(t.split()[1])
          # print(chatTask)
        elif " Fish" in t:
          fishTask = int(t.split()[1])
          # print(fishTask)
        elif " Slots " in t:
          slotTask = int(t.split()[2])
          # print(slotTask)
        elif "Cookies" in t:
          cookieTask = int(t.split()[1])
          # print(cookieTask)
        elif "Train" in t:
          trainTask = int(t.split()[3])
          # print(trainTask)


      # print(walkTask,fishTask,slotTask,chatTask,cookieTask,trainTask)
      quest(w=walkTask, tr=trainTask, f=fishTask,s=slotTask,c=cookieTask,ch=chatTask)
    else:
      print('cant see the quest, check quest again')
      time.sleep(5)
      check_quest()
  except:
    print('cant see the quest, check quest again')
    time.sleep(5)
    check_quest()

def quest(tr, w, s, f, c,ch):
  print("tr", tr, "w", w, "s", s, "f", f, "c", c, "ch", ch)
  daily()
  train(tr+round(ch/5),1)
  walk(w,12)
  fish(f,40)
  slot(s,12)
  cookie(c,12)
  status = sendMessage(tatsu, "t!quest claim")
  print(" status quest : ", status)
  time.sleep(10)

def start():
  claim_mail()
  # open()
  # pet_active()
  check_quest()

  auto(800)
  # exchange()
  # trade("leghorn", 2000)

def auto(n):
  for i in range(n):
    print("auto ", i+1)
    sendMessage(tatsu,f"auto {i}")
    train(2,30)
    # walk(2,30)
    time.sleep(60)
  start()

start()