from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll

with open('Token_VKinder', 'r') as f:
    token = str(f.readline())

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def send_message(user_id, message, keyboard=None):
    post = {
        'user_id': user_id,
        'message': message,
        'random_id': randrange(1000)
    }
    if keyboard != None:
        post['keyboard'] = keyboard.get_keyboard()
    else:
        post = post
    vk.method('messages.send', post)


