from src.utils.DiscordAPI import *
import discord

init = {
    "auth_token": "NzEyNTYzNzQ3ODEzNTg5MDQy.GTBF5B.JIpfNRW-_WkhcC7lPmQn-qKe_Tt7QRgp3MauKU",
    "channel_id": {
        "ninja_sage_id": "949159340802199593",
        "adventure_frontier": {
            "url": "https://discord.com/channels/1362991722476605520/1362992125733503177",
            "application_id": "1034876159197974569",
            "session_id": "035a9f9f5b08eb9f030bec01a1a7a25e",
        },
    },
}

auth = init["auth_token"]
url = init["channel_id"]["adventure_frontier"]["url"]
channel_id = init["channel_id"]["adventure_frontier"]["url"].split("/")[-1]
guild_id = init["channel_id"]["adventure_frontier"]["url"].split("/")[-2]
app_id = init["channel_id"]["adventure_frontier"]["application_id"]
ss_id = init["channel_id"]["adventure_frontier"]["session_id"]

msg_id = "1363339387127201814"

payload = {
    "type": 3,
    "guild_id": "1362991722476605520",
    "channel_id": "1362992125733503177",
    "message_flags": 64,
    "message_id": msg_id,
    "application_id": "1034876159197974569",
    "session_id": "0b297e24a8ddc6725cb7ff7772f11516",
    "data": {
        "component_type": 2,
        "custom_id": "profmenu-hunting",
    },
}


# api = DiscordApi(auth, channel_id)
# status = api.send_interact(payload).text
# print(status)
# res = api.retrieve_ephimeral_message("1363341826475688008")
# print(res)
# api.send_message("</professions:1113153202922209371>")

# curl 'https://adventurefrontier.net/sell-item?id=1964c0c3f09c6ea392a2dde' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-US,en;q=0.9,id;q=0.8' \
#   -H 'Connection: keep-alive' \
#   -b 'connect.sid=s%3Az8I3TUiqKgI-rJzGhgDNrhPP-4xBfUPF.q3HucgbL0Zee9clnWDCAhti%2BUABm5cwce%2BjxPuTIWpE' \
#   -H 'If-None-Match: W/"7-U6VofLJtxB8qtAM+l+E63v03QNY"' \
#   -H 'Referer: https://adventurefrontier.net/dashboard' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
#   -H 'X-Requested-With: XMLHttpRequest' \
#   -H 'sec-ch-ua: "Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"'
