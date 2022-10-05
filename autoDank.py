import json
import time
import os
import requests


auth = "isi token auth disini"
dank = "channel id disini"
guildId = "isi guild id disini"



urlMsg = "https://discord.com/api/v9/channels/1019193416254496778/messages"
# auth = 'NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA'

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

  jsonn = json.loads(r.text)
  print(jsonn[0])
  return jsonn[0]

def fishing():
    fish = {
      "type": 2,
      "application_id": "270904126974590976",
      "guild_id": guildId,
      "channel_id": dank,
      "session_id": "a8e82f3c195b2c33c17643a3b43150ed",
      "data": {
        "version": "1022917002878259287",
        "id": "1011560371078832206",
        "name": "fish",
        "type": 1,
        "options": [],
        "application_command": {
          "id": "1011560371041095699",
          "application_id": "270904126974590976",
          "version": "1022917002878259280",
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
      "guild_id": guildId,
      "channel_id": dank,
      "session_id": "a8e82f3c195b2c33c17643a3b43150ed",
      "data": {
        "version": "1022917002878259285",
        "id": "1011560371078832204",
        "name": "dig",
        "type": 1,
        "options": [],
        "application_command": {
          "id": "1011560371041095699",
          "application_id": "270904126974590976",
          "version": "1022917002878259280",
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
      "guild_id": guildId,
      "channel_id": dank,
      "session_id": "a8e82f3c195b2c33c17643a3b43150ed",
      "data": {
        "version": "1022917002932793367",
        "id": "1011560371171102760",
        "name": "hunt",
        "type": 1,
        "options": [],
        "application_command": {
          "id": "1011560371041095699",
          "application_id": "270904126974590976",
          "version": "1022917002878259280",
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
      "guild_id": guildId,
      "channel_id": dank,
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

def postMemes():
  post = {
    "type": 2,
    "application_id": "270904126974590976",
    "guild_id": guildId,
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

  time.sleep(2)

  allOptions = ['Fresh', 'Repost', 'Intellectual', 'Copypasta', 'Kind']
  choose = ['Fresh']
  chooseComponents(choose)


def chooseComponents(arr):
  res = retrieve_message(dank)
  messageId = res['id']
  try:
    components = res['components'][0]['components']
    choose = arr

    for j in choose:
      for i in components:
        # print(j)
        # print(i['label'])
        # print(i['custom_id'])
        if j == i['label']:
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
  except:
    print("cant choose")


while True:
    print(fishing())
    time.sleep(3)
    print(hunting())
    time.sleep(3)
    print(diging())
    time.sleep(3)
    print(begging())
    time.sleep(3)
    postMemes()
    time.sleep(40)




