
# Self-Bot For Discord Bot Games
This is a multi account self-bot for discord bot games like tatsu, dank-memer, or owo.
This is use simple Discord API with request library in python.

## Feature
### Dank-Memer
* fish, dig, hunt, postmemes, search, crime, beg, highlow
* daily, adventure, stream,
* auto use item
* stream
* mini games
* blackjack

### Tatsu
* train, feed, walk, fish
* slot
* cookie, daily, quest

### OWO
* hunt, battle, pray, cookie, curse
* quest, daily
* coinflip, slot

## How to Use
You can change the `init.json` file and add your account detail. It can run for multiple account just add another account detail with same format.
```json
[
  {
    "auth_token" : "YOUR AUTH TOKEN ACCOUNT 1",
    "channel_id" : {
      "dank": {
        "url": "YOUR DANK MEMER CHANNEL URL",
        "application_id": "YOUR APPLICATION ID ACCOUNT 1",
        "session_id": "YOUR SESSION ID ACCOUNT 2"
      },
      "tatsu_channel_id": "YOUR TATSU CHANNEL ID",
      "owo_channel_id": "YOUR OWO CHANNEL ID"
    }
  },
  {
    "auth_token" : "YOUR AUTH TOKEN ACCOUNT 2",
    "channel_id" : {
      "dank": {
        "url": "YOUR DANK MEMER CHANNEL URL",
        "application_id": "YOUR APPLICATION ID ACCOUNT 2",
        "session_id": "YOUR SESSION ID ACCOUNT 2"
      },
      "tatsu_channel_id": "YOUR TATSU CHANNEL ID",
      "owo_channel_id": "YOUR OWO CHANNEL ID"
    }
  }
]
```

then run ``main.py``.

```python
python3 main.py
```













