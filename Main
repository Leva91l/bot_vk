import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

from DB_VKinder import insert_data, women, men
from engine import send_message
import os

with open('Token_VKinder', 'r') as f:
    token = str(f.readline())

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        text = event.text.lower()
        user_id = event.user_id
        user_data = {
            'user_id': user_id
        }
        user_name = vk.method('users.get', {'user_ids': user_id, 'fields': 'first_name'})
        user_city = vk.method('users.get', {'user_ids': user_id, 'fields': 'city'})
        user_sex = vk.method('users.get', {'user_ids': user_id, 'fields': 'sex'})
        user_age = vk.method('users.get', {'user_ids': user_id, 'fields': 'bdate'})

        user_data['user_name'] = user_name[0]['first_name']
        user_data['user_age'] = user_age[0]['bdate']
        user_data['user_sex'] = user_sex[0]['sex']
        user_data['user_city'] = user_city[0]['city']['title']
        answer_1 = None
        answer_2 = None
        answer_3 = None
        if text == 'начать':
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Парня', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Девушку', VkKeyboardColor.NEGATIVE)
            send_message(user_id, 'Кого ищете?', keyboard)

            for key, value in user_data.items():
                with open(f'{user_id}.txt', 'a', encoding='UTF-8') as file:
                    file.write(f'{value}\n')

        if text == 'парня' or text == 'девушку':
            answer_1 = text
            with open(f'{user_id}.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{text}\n')
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Для серьезных отношений!', VkKeyboardColor.PRIMARY)
            keyboard.add_button('Просто скучно)', VkKeyboardColor.NEGATIVE)
            send_message(user_id, 'Какая цель знакомства?', keyboard)

        if text == 'для серьезных отношений!' or text == 'просто скучно)':
            answer_2 = text
            with open(f'{user_id}.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{text}\n')
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('18-25 лет', VkKeyboardColor.PRIMARY)
            keyboard.add_button('25-30 лет', VkKeyboardColor.NEGATIVE)
            keyboard.add_button('30-35 лет', VkKeyboardColor.SECONDARY)
            keyboard.add_button('35-40 лет', VkKeyboardColor.POSITIVE)
            send_message(user_id, 'Каким должен быт возраст партнера?', keyboard)

        if text == '18-25 лет' or text == '25-30 лет' or text == '30-35 лет' or text == '35-40 лет':
            answer_3 = text
            with open(f'{user_id}.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{text}\n')

            with open(f'{user_id}.txt', 'r', encoding='UTF-8') as file:
                if user_data['user_sex'] == 1:
                    insert_data(women,
                                user_id=file.readline()[:-1],
                                name=file.readline()[:-1],
                                age=str(file.readline()[:-1]),
                                sex=file.readline()[:-1],
                                city=file.readline()[:-1],
                                objective=file.readline()[:-1],
                                intention=file.readline()[:-1],
                                partners_age=file.readline()[:-1]
                    )

                else:
                    insert_data(men,
                                user_id=file.readline()[:-1],
                                name=file.readline()[:-1],
                                age=str(file.readline()[:-1]),
                                sex=file.readline()[:-1],
                                city=file.readline()[:-1],
                                objective=file.readline()[:-1],
                                intention=file.readline()[:-1],
                                partners_age=file.readline()[:-1]
                                )
                file.close()
                os.remove(f'{user_id}.txt')
                
