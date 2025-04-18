
# Self-Bot For Discord Bot Games
This is a multi account self-bot for discord bot games like tatsu, dank-memer, or owo.
This is use simple Discord API with request library in python.

## Feature
### Adventure Frontier
* attack
* hunt
* gather

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
      "adventure_frontier": {
        "url": "YOUR ADVENTURE FRONTIER CHANNEL URL",
        "application_id": "YOUR APPLICATION ID ACCOUNT 1",
        "session_id": "YOUR SESSION ID ACCOUNT 1"
      },
      "dank": {
        "url": "YOUR DANK MEMER CHANNEL URL",
        "application_id": "YOUR APPLICATION ID ACCOUNT 1",
        "session_id": "YOUR SESSION ID ACCOUNT 1"
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

### How to get the data
#### Authentication Token
- open discord on web browser
- login your account then inspect element
- go to network tab and filter `/api`
- read the request information and search for Authorization and copy the code (refresh the page if nothing)

#### Channel Id
- open discord on web browser
- login account and open a server discord
- choose the channel you want
- look at the url of the page, example `https://discord.com/channels/696275213708427334/1362714778073829416`
- the first random number is guild id `696275213708427334` and the second random number is the channel id `1362714778073829416`

#### Application and session id
- Open discord on web browser
- login to discord 
- inspect element (search how to inspect element on your browser)
- go to network tab
- try to chat with command `/something` then enter
- looks the network tab there is a interactions requests
- copy the value and format the json file so you can easly to find
- find application and session id













