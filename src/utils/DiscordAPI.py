import requests
import json


class DiscordApi:

    def __init__(self, auth_token, channel_id):
        self.auth_token = auth_token
        self.channel_id = channel_id

    def retrieve_message(self, order=0):
        header = {"authorization": self.auth_token}
        r = requests.get(
            f"https://discord.com/api/v8/channels/{self.channel_id}/messages",
            headers=header,
        )

        if order != 0:
            jsonn = json.loads(r.text)

            return jsonn[0:order]

        jsonn = json.loads(r.text)

        return jsonn[0]

    def send_message(self, message):
        url = "https://discord.com/api/v8/channels/{}/messages".format(self.channel_id)
        data = {"content": message}
        header = {"authorization": self.auth_token}
        r = requests.post(url, data=data, headers=header)

        return r

    def send_interact(self, payload):
        url = "https://discord.com/api/v9/interactions"
        data = payload
        header = {"authorization": self.auth_token}
        r = requests.post(url, json=data, headers=header)

        return r

    def delete_message(self, message_id):
        url = f"https://discord.com/api/v9/channels/{self.channel_id}/messages/{message_id}"
        header = {"authorization": self.auth_token}
        r = requests.delete(url, headers=header)

        return r.status_code