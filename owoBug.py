import time
import requests
import json
import random
import os
import asyncio
import aiohttp


auth = "NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA"
# username = "Leghorn"
authf = "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ" #f
authb = "MTAyMzQzODQ2OTYyMTYyMDg1Nw.GQposd.457v3IY1XOH6Dyurv0nAp2sT6uwqdMa-qPMK_M" #b

leg = "Leghorn"
foz = "foztr4"
bay = "bayes4"

legId = "<@712563747813589042>"
fozId = "<@1023440449949671424>"
bayId = "<@1023438469621620857>"

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

async def sendMessage(channel_id, message, token):
  url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
  data = {"content": message}
  header = {"authorization": token}
  r = requests.post(url, data=data, headers=header)
  # requests.post(url, data=data, headers=header)
  await asyncio.sleep(0)

  # return r.status_code

async def wcf(bet, token):
    await sendMessage(owo, f"wcf {bet}", token)


async def ws(bet, token):
    await sendMessage(owo, f"ws {bet}", token)



async def wbj(bet, token):
    await sendMessage(owo, f"wbj {bet}", token)



async def wlottery(bet, token):
    await sendMessage(owo, f"wlottery {bet}", token)



async def wgive(amount, user, token):
    await sendMessage(owo, f"wgive {user} {amount}", token)



# def same(bet, user, token):
#     asyncio.run(sendMessage(owo, f"wcf {bet}", token))
#     # asyncio.run(sendMessage(owo, f"ws {bet}", token))
#     asyncio.run(sendMessage(owo, f"wlottery {bet}", token))
#     # asyncio.run(sendMessage(owo, f"wbj {bet}", token))
#     asyncio.run(sendMessage(owo, f"wgive {user} {bet}", token))

# async def same(bet, user, token):
#     asyncio.gather(wcf(bet, token), ws(bet,token), wlottery(bet,token), wbj(bet,token), wgive(bet, user, token))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(same(16, legId, authf))
# loop.close()
bet = 2
token = authf
user = legId


asyncio.get_event_loop().run_until_complete(asyncio.gather(wcf(bet, token), ws(bet,token), wlottery(bet,token), wbj(bet,token), wgive(bet, user, token)))
# same(2, legId, authf)
# asyncio.run(same(16, legId, authf))