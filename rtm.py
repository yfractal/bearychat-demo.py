import time
from bearychat import RTMClient

from rtm_loop import RTMLoop


def main():
    # init the rtm client
    client = RTMClient("your-rtm-token", "https://rtm.bearychat.com")

    resp = client.start()  # get rtm user and ws_host

    user = resp["user"]
    ws_host = resp["ws_host"]
    print("ws_host {0}".format(ws_host))


    loop = RTMLoop(ws_host)  # init the loop
    loop.start()
    time.sleep(2)

    while True:
        error = loop.get_error()

        if error:
            print(error)
            continue

        message = loop.get_message(True, 5)

        if not message or not message.is_chat_message():
            continue
        try:
            if message["file"] and message["file"]["category"] == "image":
                print("The image's url is: {0}".format(message["file"]["image_url"]))
        except Exception:
            continue

        if message.is_from(user):
            continue

        loop.send(message.refer("Pardon?"))


if __name__ == '__main__':
    main()
