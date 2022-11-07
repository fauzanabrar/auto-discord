import json
import random
import time
import os
import requests



dank = "1023197387063308318"
dank_memer = "1020998895960084530"


urlMsg = "https://discord.com/api/v9/channels/1019193416254496778/messages"
auth = 'NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA'
urlInteract = "https://discord.com/api/v9/interactions"


def sendMessage(channel_id, message):
  url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
  data = {"content": message}
  header = {"authorization": auth}
  r = requests.post(url, json=data, headers=header)
  return r.status_code

def sendInteract(payload):
  url = urlInteract
  data = payload
  header = {"authorization": auth}
  r = requests.post(url, json=data, headers=header)
  return r.status_code

def retrieve_message(channelId):
  header = {
    'authorization' : auth
  }
  r = requests.get(
    f'https://discord.com/api/v8/channels/{channelId}/messages', headers=header
  )
  try:
    jsonn = json.loads(r.text)
    # print(jsonn[0])
    return jsonn[0]
  except:
    time.sleep(1)
    return retrieve_message(channelId)

def check_res():

  pass

def fishing():
    fish = {
      "type": 2,
      "application_id": "270904126974590976",
      "guild_id": "1020996568029077596",
      "channel_id": "1020998895960084530",
      "session_id": "a8e82f3c195b2c33c17643a3b43150ed",
      "data": {
        "version": "1022917002878259287",
        "id": "1011560371078832206",
        "name": "fish",
        "type": 1,
        "options": [],
        "application_command": {
          "id": "1011560371078832206",
          "application_id": "270904126974590976",
          "version": "1022917002878259287",
          "default_permission": "true",
          "default_member_permissions": "null",
          "type": 1,
          "name": "fish",
          "description": "Grab a fishing pole from the shop and go fishing for some fun items!",
          "dm_permission": "true"
        },
        "attachments": []
      }
    }
    return sendInteract(fish)

def diging():
    dig = {
      "type": 2,
      "application_id": "270904126974590976",
      "guild_id": "1020996568029077596",
      "channel_id": "1020998895960084530",
      "session_id": "a8e82f3c195b2c33c17643a3b43150ed",
      "data": {
        "version": "1022917002878259285",
        "id": "1011560371078832204",
        "name": "dig",
        "type": 1,
        "options": [],
        "application_command": {
          "id": "1011560371078832204",
          "application_id": "270904126974590976",
          "version": "1022917002878259285",
          "default_permission": "true",
          "default_member_permissions": "null",
          "type": 1,
          "name": "dig",
          "description": "Dig in the dirt for bugs and other fun items.",
          "dm_permission": "true"
        },
        "attachments": []
      }
    }
    return sendInteract(dig)

def hunting():
    hunt = {
      "type": 2,
      "application_id": "270904126974590976",
      "guild_id": "1020996568029077596",
      "channel_id": "1020998895960084530",
      "session_id": "a8e82f3c195b2c33c17643a3b43150ed",
      "data": {
        "version": "1022917002932793367",
        "id": "1011560371171102760",
        "name": "hunt",
        "type": 1,
        "options": [],
        "application_command": {
          "id": "1011560371171102760",
          "application_id": "270904126974590976",
          "version": "1022917002932793367",
          "default_permission": "true",
          "default_member_permissions": "null",
          "type": 1,
          "name": "hunt",
          "description": "Grab a rifle from the shop and go hunting for fun items!",
          "dm_permission": "true"
        },
        "attachments": []
      }
    }
    return sendInteract(hunt)

def begging():
    beg = {
      "type": 2,
      "application_id": "270904126974590976",
      "guild_id": "1020996568029077596",
      "channel_id": "1020998895960084530",
      "session_id": "a8e82f3c195b2c33c17643a3b43150ed",
      "data": {
        "version": "1022917002878259280",
        "id": "1011560371041095699",
        "name": "beg",
        "type": 1,
        "options": [],
        "application_command": {
          "id": "1011560371041095699",
          "application_id": "270904126974590976",
          "version": "1022917002878259280",
          "default_permission": "true",
          "default_member_permissions": "null",
          "type": 1,
          "name": "beg",
          "description": "Beg for coins to help bolster your pocket balance.",
          "dm_permission": "true"
        },
        "attachments": []
      }
    }
    return sendInteract(beg)

def choose_postmemes(custom_id, value, message_id):
  return {
     "type":3,
     "guild_id":"1020996568029077596",
     "channel_id":dank,
     "message_flags":0,
     "message_id":message_id,
     "application_id":"270904126974590976",
     "session_id":"4f3e7d4f9dd539b87416e294ef65020e",
     "data":{
        "component_type":3,
        "custom_id":custom_id,
        "type":3,
        "values":[
           value
        ]
     }
  }

def postMemes():
  post = {
    "type": 2,
    "application_id": "270904126974590976",
    "guild_id": "1020996568029077596",
    "channel_id": dank,
    "session_id": "c19bf8530a1860234764bb1c0f97ee35",
    "data": {
      "version": "1022917002794381384",
      "id": "1011560370911072263",
      "name": "postmemes",
      "type": 1,
      "options": [],
      "application_command": {
        "id": "1011560370911072263",
        "application_id": "270904126974590976",
        "version": "1022917002794381384",
        "default_permission": "true",
        "default_member_permissions": "null",
        "type": 1,
        "name": "postmemes",
        "description": "Post (fake) memes with the chance to earn some coins.",
        "dm_permission": "true"
      },
      "attachments": []
    }
  }
  p = sendInteract(post)
  print("post", p)

  time.sleep(1)
  res = retrieve_message(dank)
  try:
    message_id = res['id']
    custom_id1 = res['components'][0]['components'][0]['custom_id']  # select platform
    custom_id2 = res['components'][1]['components'][0]['custom_id']  # select meme type
    post_btn = res['components'][2]['components'][0]['custom_id']  # post button

    platforms = ["discord", "reddit", "twitter", "facebook"]
    meme_types = ["Fresh", "Repost", "Intellectual", "Copypasta", "Kind"]

    p = sendInteract(choose_postmemes(custom_id1,random.choice(platforms), message_id))
    print("platform memes choosed", p)
    time.sleep(1)
    p = sendInteract(choose_postmemes(custom_id2,random.choice(meme_types), message_id))
    print("meme type has choosed", p)
    time.sleep(1)

    post_meme = {
       "type":3,
       "guild_id":"1020996568029077596",
       "channel_id":dank,
       "message_flags":0,
       "message_id":message_id,
       "application_id":"270904126974590976",
       "session_id":"4f3e7d4f9dd539b87416e294ef65020e",
       "data":{
          "component_type":2,
          "custom_id":post_btn
       }
    }

    p = sendInteract(post_meme)
    print("meme has posted", p)
  except:
    pass


def chooseComponents(arr, channelId = dank):
  res = retrieve_message(channelId)
  messageId = res['id']
  try:
    components = res['components'][0]['components']
    choose = arr
    isChoosed = False
    for j in choose:
      if isChoosed:
        break
      for i in components:
        print(j)
        print(i['label'])
        print(i['custom_id'])
        if j.lower() == i['label'].lower():
          print("choosed",j)
          customId = i['custom_id']
          data = {
            "type": 3,
            "guild_id": "1020996568029077596",
            "channel_id": channelId,
            "message_flags": 0,
            "message_id": messageId,
            "application_id": "270904126974590976",
            "session_id": "c19bf8530a1860234764bb1c0f97ee35",
            "data": {
              "component_type": 2,
              "custom_id": customId
            }
          }
          l = sendInteract(data)
          print(j, l)
          isChoosed = True
          break

  except:
    print("cant choose")

def auto_search():
  search = {
    "type": 2,
    "application_id": "270904126974590976",
    "guild_id": "1020996568029077596",
    "channel_id": "1023197387063308318",
    "session_id": "3bc2fa9f30874f239299b62d727dd5f0",
    "data": {
      "version": "1022917002987315252",
      "id": "1011560371267579935",
      "name": "search",
      "type": 1,
      "options": [],
      "application_command": {
        "id": "1011560371267579935",
        "application_id": "270904126974590976",
        "version": "1022917002987315252",
        "default_permission": "true",
        "default_member_permissions": "null",
        "type": 1,
        "name": "search",
        "description": "Search various places for items and coins, with some risks.",
        "dm_permission": "true"
      },
      "attachments": []
    }
  }
  s = sendInteract(search)
  print("search", s)

  time.sleep(2)

  allOptions = [
    "Aeradella's home",
    "Air",
    "Area51",
    "Attic",
    "Bank",
    "Basement",
    "Bathroom",
    "Bed",
    "Beehive",
    "Book",
    "Briefcase",
    "Bus",
    "Bushes",
    "Car",
    "Coat",
    "Coffee shop",
    "Computer",
    "Couch",
    "Crawlspace",
    "Dark room",
    "Discord",
    "Dog",
    "Dresser",
    "Dumpster",
    "Fridge",
    "Garage",
    "Glovebox",
    "God's Own Place",
    "Grass",
    "Hospital",
    "Immortals Dimension",
    "Kitchen",
    "Laundromat",
    "Lego bin",
    "Mailbox",
    "McDonald's",
    "Movie Theater",
    "Ocean",
    "Pantry",
    "Phoenix pits",
    "Pocket",
    "Police officer",
    "Purse",
    "Sewer",
    "Shoe",
    "Sink",
    "Soul's chamber",
    "Street	",
    "Supreme Court",
    "Tesla",
    "Toilet",
    "Toxic waste plant",
    "Twitch",
    "Twitter",
    "Tree",
    "Uber",
    "Vacuum",
    "Van",
    "Washer",
    "Who asked",
    "ZomB's Grave"
  ]
  choose = [
    "Toxic waste plant",
    "Soul's chamber",
    "Tesla",
    "Dog",
    "Grass",
    "Phoenix pits",
    "Twitch",
    "Police officer",
    "McDonald's",
    "Sewer",
    "Ocean",
    "Pantry",
    "ZomB's Grave",
    "Mailbox",
    "Area51",
    "Fridge",
    "Hospital",
    "Basement",
    "Bathroom",
    "Beehive",
    "Kitchen",
    "Stock Market",
    "Book",
    "Dresser",
    "Briefcase",
    "Glovebox",
    "Street	",
    "Bushes",
    "Car",
    "Vacuum",
    "Dark room",
    "Aeradella's home",
    "Air",
    "Attic",
    "Bank",
    "Bed",
    "Bus",
    "Car",
    "Coat",
    "Computer",
    "Crawlspace",
    "Dumpster",
    "Garage",
    "God's Own Place",
    "Immortals Dimension",
    "Lego bin",
    "Movie Theater",
    "Purse",
    "Shoe",
    "Sink",
    "Supreme Court",
    "Twitter",
    "Tree",
    "Uber",
    "Van"
  ]
  chooseComponents(choose)

def auto_crime():
  crime = {
    "type": 2,
    "application_id": "270904126974590976",
    "guild_id": "1020996568029077596",
    "channel_id": "1023197387063308318",
    "session_id": "2ea2c43414a8ae0e721eb2b57ea6873d",
    "data": {
      "version": "1022917002878259283",
      "id": "1011560371078832202",
      "name": "crime",
      "type": 1,
      "options": [],
      "application_command": {
        "id": "1011560371078832202",
        "application_id": "270904126974590976",
        "version": "1022917002878259283",
        "default_permission": "true",
        "default_member_permissions": "null",
        "type": 1,
        "name": "crime",
        "description": "Commit a (fake) crime for items and coins, with some risk.",
        "dm_permission": "true"
      },
      "attachments": []
    }
  }
  c = sendInteract(crime)
  print("crime", c)

  time.sleep(2)

  allOptions = [
    "Arson",
    "Bank robbing",
    "Boredom",
    "Cyber bullying",
    "Drug distribution",
    "Driving under the influence (DUI)",
    "Eating A Hot Dog Sideways",
    "Fraud",
    "Hacking",
    "Identity theft",
    "Littering",
    "Murder",
    "Piracy",
    "Shoplifting",
    "Tax evasion",
    "Treason",
    "Trespassing",
    "Vandalism"
  ]
  choose = [
    "Tax evasion",
    "DUI",
    "Driving under the influence (DUI)",
    "Piracy",
    "Eating A Hot Dog Sideways",
    "Hacking",
    "Treason",
    "Bank robbing",
    "Murder",
    "Boredom",
    "Cyber bullying",
    "Drug distribution",
    "Identity theft",
    "Littering",
    "Shoplifting",
    "Vandalism",
    "Trespassing",
    "Fraud",
    "Arson"
  ]
  chooseComponents(choose)
  time.sleep(10)

# example 'Lucky Horse', 'apple'
def auto_use_item(item):
  itemPayload = {
    "type": 2,
    "application_id": "270904126974590976",
    "guild_id": "1020996568029077596",
    "channel_id": "1023197387063308318",
    "session_id": "2ea2c43414a8ae0e721eb2b57ea6873d",
    "data": {
      "version": "1022917002987315258",
      "id": "1011560371267579941",
      "name": "use",
      "type": 1,
      "options": [
        {
          "type": 3,
          "name": "item",
          "value": item.capitalize()
        }
      ],
      "application_command": {
        "id": "1011560371267579941",
        "application_id": "270904126974590976",
        "version": "1022917002987315258",
        "default_permission": "true",
        "default_member_permissions": "null",
        "type": 1,
        "name": "use",
        "description": "Use currency items that you own.",
        "dm_permission": "true",
        "options": [
          {
            "type": 3,
            "name": "item",
            "description": "Select an item",
            "required": "true",
            "autocomplete": "true"
          },
          {
            "type": 6,
            "name": "user",
            "description": "Used to choose a user when required."
          },
          {
            "type": 4,
            "name": "quantity",
            "description": "Amount of items you want to use when possible."
          }
        ]
      },
      "attachments": []
    }
  }
  i = sendInteract(itemPayload)
  print(f"use {item}", i)
  time.sleep(3)

def highlow():
  highlowPayload = {
     "type":2,
     "application_id":"270904126974590976",
     "guild_id":"1020996568029077596",
     "channel_id":"1023197387063308318",
     "session_id":"ec6eef22e041061d1b2b8ab44c41ff15",
     "data":{
        "version":"1022917002748235843",
        "id":"1011560370911072258",
        "name":"highlow",
        "type":1,
        "options":[

        ],
        "application_command":{
           "id":"1011560370911072258",
           "application_id":"270904126974590976",
           "version":"1022917002748235843",
           "default_permission":"true",
           "default_member_permissions":"null",
           "type":1,
           "name":"highlow",
           "description":"Guess if the number is higher or lower and if you're right you get coins. Jackpot wins big!",
           "dm_permission":"true"
        },
        "attachments":[

        ]
     }
  }
  hl = sendInteract(highlowPayload)
  print("highlow", hl)

  time.sleep(2)

  allOptions = ['Lower', 'JACKPOT!', 'Higher']

  res = retrieve_message(dank)
  messageId = res['id']
  try:
    guessNum = int(((res['embeds'][0]['description']).split("**"))[1])
    print(guessNum)
    choose = []
    if guessNum >= 50:
      choose.append("Lower")
    else:
      choose.append("Higher")

    components = res['components'][0]['components']
    isChoosed = False
    for j in choose:
      if isChoosed:
        break
      for i in components:
        # print(j)
        # print(i['label'])
        # print(i['custom_id'])
        if j.lower() == i['label'].lower():
          print("choosed", j)
          customId = i['custom_id']
          data = {
            "type": 3,
            "guild_id": "1020996568029077596",
            "channel_id": dank,
            "message_flags": 0,
            "message_id": messageId,
            "application_id": "270904126974590976",
            "session_id": "c19bf8530a1860234764bb1c0f97ee35",
            "data": {
              "component_type": 2,
              "custom_id": customId
            }
          }
          l = sendInteract(data)
          print(j, l)
          isChoosed = True
          break

  except:
    print("cant choose")


def auto_pepe_adv():
  pepePayload = {
    "type": 2,
    "application_id": "270904126974590976",
    "guild_id": "1020996568029077596",
    "channel_id": "1023197387063308318",
    "session_id": "49ac6d09a4837dfff6740e04aad19fa3",
    "data": {
      "version": "1022917002848903204",
      "id": "1011560371041095695",
      "name": "adventure",
      "type": 1,
      "options": [],
      "application_command": {
        "id": "1011560371041095695",
        "application_id": "270904126974590976",
        "version": "1022917002848903204",
        "default_permission": "true",
        "default_member_permissions": "null",
        "type": 1,
        "name": "adventure",
        "description": "Exchange a ticket for an interactive adventure!",
        "dm_permission": "true"
      },
      "attachments": []
    }
  }

  p = sendInteract(pepePayload)
  print("adv pepe", p)

  time.sleep(2)

  allOptions = [
    "Arson",
    "Bank robbing",
    "Boredom",
    "Cyber bullying",
    "Drug distribution",
    "Driving under the influence (DUI)",
    "Eating A Hot Dog Sideways",
    "Fraud",
    "Hacking",
    "Identity theft",
    "Littering",
    "Murder",
    "Piracy",
    "Shoplifting",
    "Tax evasion",
    "Treason",
    "Trespassing",
    "Vandalism"
  ]
  allQuestion = [
    [
      "You uh, just came across a pair of Odd Eyes floating around",
     ["Flee"]
     ],
    [
      "You got abducted by a group of aliens, who are trying to probe you. What do you do?",
      ["Sit back and enjoy"]
    ],
    [
      "A friendly alien approached you slowly. What do you do?",
      ["Probe"]
    ],
    [
      "This planet seems to be giving off radioactive chemicals. What do you do?",
      ["Distant Scan"]
    ],
    [
      "Oh my god even in space you cannot escape it",
      ["Never"]
    ],
    [
      "You're picking up a transmission from deep space!",
      ["*<)\#%':](.)#"]
    ],
    [
      "You ran out of fuel! What next?",
      ["Urinate"]
    ],
    [
      "A small but wise green alien approaches you",
      ["Do"]
    ],
    [
      "You encountered someone named Dank Sidious, what do you do?",
      ["Do it"]
    ],
    [
      "You accidentally bumped into the Webb Telescope. Oh god.",
      ["Flee"]
    ],
    [
      "You see a shooting star!",
      ["Wish"]
    ],
    [
      "You found a strange-looking object. What do you do?",
      ["Ignore"]
    ],
    [
      "Whaaaat!? You found a space kitchen! It looks like it is full of shady stuff. What do you do?",
      ["Inspect"]
    ],
    [
      "You flew past a dying star",
      ["Flee"]
    ]
  ]

  res = retrieve_message(dank)
  if check_new_adv(res):
    new_pepe_adv()
  else:
    question = res['embeds'][0]['description']
    answer = ""
    for i in allQuestion:
      if i[0].lower() in question.lower():
        answer = i[1]
    # print("question :", question)
    # print("answer :", answer)
    chooseComponents(answer)



def check_new_adv(res):

  if not 'footer' in (res['embeds'][0]) :
    return True

  if ("🚀" in res['embeds'][0]['footer']['text'] ):
    return False
  else:
    return True



def new_pepe_adv():

  res = retrieve_message(dank)
  if len(res['components']) >=2 and len(res['components'][1]['components'][0]) :
    customId = res['components'][1]['components'][0]['custom_id']
    messageId = res['id']
    startPayload = {
       "type":3,
       "guild_id":"1020996568029077596",
       "channel_id":"1023197387063308318",
       "message_flags":0,
       "message_id":messageId,
       "application_id":"270904126974590976",
       "session_id":"630dd799639f680871cece257dcd5ad0",
       "data":{
          "component_type":2,
          "custom_id":customId
       }
    }
    s1 = sendInteract(startPayload)
    print("new adv pepe", s1)

    time.sleep(2)
    res = retrieve_message(dank)
    messageId = res['id']
    customId = res['components'][2]['components'][1]['custom_id']
    equipAllPayload = {
       "type":3,
       "guild_id":"1020996568029077596",
       "channel_id":"1023197387063308318",
       "message_flags":0,
       "message_id":messageId,
       "application_id":"270904126974590976",
       "session_id":"630dd799639f680871cece257dcd5ad0",
       "data":{
          "component_type":2,
          "custom_id":customId
       }
    }
    s2 = sendInteract(equipAllPayload)
    print("new equip adv pepe", s2)

    time.sleep(2)
    res = retrieve_message(dank)
    messageId = res['id']
    customId = res['components'][1]['components'][1]['custom_id']
    unequipTrophyPayload = {
       "type":3,
       "guild_id":"1020996568029077596",
       "channel_id":"1023197387063308318",
       "message_flags":0,
       "message_id":messageId,
       "application_id":"270904126974590976",
       "session_id":"630dd799639f680871cece257dcd5ad0",
       "data":{
          "component_type":2,
          "custom_id":customId
       }
    }
    s3 = sendInteract(unequipTrophyPayload)
    print("new unequip adv pepe", s3)

    time.sleep(2)
    res = retrieve_message(dank)
    messageId = res['id']
    customId = res['components'][2]['components'][0]['custom_id']
    startAdvPayload = {
       "type":3,
       "guild_id":"1020996568029077596",
       "channel_id":"1023197387063308318",
       "message_flags":0,
       "message_id":messageId,
       "application_id":"270904126974590976",
       "session_id":"630dd799639f680871cece257dcd5ad0",
       "data":{
          "component_type":2,
          "custom_id":customId
       }
    }
    s4 = sendInteract(startAdvPayload)
    print("start new adv pepe", s4)

    time.sleep(2)
    auto_pepe_adv()


def mini_game():

  res = retrieve_message(1020998895960084530)
  print("check mini game")
  print(res)

  if not 'description' in (res['embeds'][0]) :
    print("dont have description")
    return
  choose = []
  desc = res['embeds'][0]['description']
  if "Dunk the ball!" in desc:
    print("dunk the ball")
    b = desc.split("\n")
    c = b[2]

    if c.count("<:emptyspace:827651824739156030>") == 0:
      choose.append("left")
    elif c.count("<:emptyspace:827651824739156030>") == 1:
      choose.append("middle")
    elif c.count("<:emptyspace:827651824739156030>") == 2:
      choose.append("right")

  elif "Hit the ball!" in desc:
    print("hit the ball")
    b = desc.split("\n")
    c = b[2]

    if c.count("<:emptyspace:827651824739156030>") == 0:
      choose.append("middle")
    elif c.count("<:emptyspace:827651824739156030>") == 1:
      choose.append("right")
    elif c.count("<:emptyspace:827651824739156030>") == 2:
      choose.append("left")

  elif "Catch the fish!" in desc:
    print("catch the fish")
    b = desc.split("\n")
    c = b[1]

    if c.count("<:emptyspace:827651824739156030>") == 0:
      choose.append("left")
    elif c.count("<:emptyspace:827651824739156030>") == 1:
      choose.append("middle")
    elif c.count("<:emptyspace:827651824739156030>") == 2:
      choose.append("right")

  elif "Dodge the Fireball!" in desc:
    print("dodge the fireball")
    b = desc.split("\n")
    c = b[2]

    if c.count("<:emptyspace:827651824739156030>") == 0:
      choose.append("left")
    elif c.count("<:emptyspace:827651824739156030>") == 1:
      choose.append("middle")
    elif c.count("<:emptyspace:827651824739156030>") == 2:
      choose.append("right")

  if len(choose) != 0:
    print("time to choose", choose)
    chooseComponents(choose, dank_memer)



# auto_use_item('Apple')
# auto_use_item('Lucky Horseshoe')
# auto_use_item("Cupid's Big Toe")
# auto_use_item('Prestige Coin')
# auto_use_item('Pizza Slice')
# auto_use_item('Daily Box')
# auto_use_item('Fishing Bait')
# auto_use_item('Fishing Bait')

#
jalan = 0

while True:
  if jalan % 16 == 0:
    auto_use_item('Lucky Horseshoe')
    # auto_use_item('Daily Box')

    time.sleep(2)
  if jalan % 7 == 0:
    auto_pepe_adv()
    time.sleep(6)

  # if jalan % 67 == 0:
  #   auto_use_item('Pizza Slice')
  #   time.sleep(4)


  print(fishing())
  time.sleep(3)
  mini_game()
  time.sleep(5)
  print(hunting())
  time.sleep(3)
  mini_game()
  time.sleep(5)
  print(diging())
  time.sleep(3)
  mini_game()
  time.sleep(5)
  print(begging())
  time.sleep(3)
  highlow()
  time.sleep(5)
  postMemes()
  time.sleep(5)
  auto_search()
  time.sleep(5)
  auto_crime()
  time.sleep(5)
  jalan+=1
