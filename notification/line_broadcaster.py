import requests


class LineBroadcaster:

    def __init__(self, token="I7fTOMoZibl67kxg1lmq4ZPXxj7mCirgLiagkjhxGyt", url="https://notify-api.line.me/api/notify"):
        self.__token = token
        self.__url = url

    def send_notification(self, msg):
        headers = {
            "Authorization": "Bearer " + self.__token
        }
        data = {
            "message": msg
        }
        requests.post(self.__url, headers=headers, data=data)
