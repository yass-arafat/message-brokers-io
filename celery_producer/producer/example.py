from celery_app import send_me_a_message
import time
import uuid, datetime

# @celery.task
# def dummy_task():
#     return "OK"


# for i in range(1):
    # time.sleep(10)
message = {
    "id": "hgfghfhgf"}
send_me_a_message(message)