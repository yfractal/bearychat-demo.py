## Setup

### Install requirements
```
$ pip install -r requirements.txt
```
### Set RTM token
Need to create a hubot in BearyChat, then the get the created hubot's token.

Set the token in `rtm_loop.py:9`

eg: `client = RTMClient("852e2beb0dfbf96e9074b2xxxxxxxxxx", "https://rtm.bearychat.com")`

### Then run the program

```
$ python rtm.py
```

When a image is send to the hubot, the image's url will be printed out in console.
