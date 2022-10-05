import json
import time
import os
import requests



dank = "1020998895960084530"

urlVote = "https://discordbotlist.com/api/v1/bots/270904126974590976/upvote"
urlVote = "https://discordbotlist.com/api/v1"
authVote = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0IjowLCJ0b2tlbiI6IldCdkdhR0ZUbGJGZUtWVFdqdTdzV3AwMHJOVDVWSSIsImlkIjoiNzEyNTYzNzQ3ODEzNTg5MDQyIiwiaWF0IjoxNjYzNzM5NDI3LCJleHAiOjIyNjg1Mzk0Mjd9.oh4fRb04uZO8WMQxn9eWoW5SmLwazdqff6wglqOx_Gk"
secret = {"secret":"=7e023ffa"}
secret = {"secret":"=MTM3cjMxkzM"}


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
  url = urlVote
  data = payload
  header = {"authorization": auth}
  r = requests.post(url, json=data, headers=header)
  return r.status_code

def retrieve_message(channelId):
  header = {
    'authorization' : authVote
  }
  r = requests.get(
    "https://discordbotlist.com/bots/tatsu/upvote", headers=header
  )
  print(r.text)
  # jsonn = json.loads(r.text)
  # print(jsonn[0])
  # return jsonn[0]

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

def postMemes():
  post = {
    "type": 2,
    "application_id": "270904126974590976",
    "guild_id": "1020996568029077596",
    "channel_id": "1020998895960084530",
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

  res = retrieve_message(dank)
  messageId = res['id']
  # customId = res['components'][0]['components'][4]['custom_id']
  customId = res['components'][0]['components'][4]['custom_id']
  kind = {
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
  k = sendInteract(kind)
  print("kind", k)


#
# while True:
#     print(fishing())
#     time.sleep(3)
#     print(hunting())
#     time.sleep(3)
#     print(diging())
#     time.sleep(3)
#     print(begging())
#     time.sleep(3)
#     postMemes()
#     time.sleep(40)


retrieve_message(dank)

sendInteract(secret)