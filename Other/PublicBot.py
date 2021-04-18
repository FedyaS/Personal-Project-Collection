from telethon import TelegramClient, events
import telegram
from fuzzywuzzy import fuzz, process
import os
import time

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


bot = telegram.Bot('private key')

api_id = 0
api_hash = 'private hash'
client = TelegramClient('anon', api_id, api_hash)

testing = False

mirror_chat_id = 0
receive_chat_id = 0
test_chat_id = 0
official_channel_id = 0
include_chat_ids = [0]
#-1001269340179 is Talking Chat...
#-1001242348586 is official alert Chat...
testing_include_chat_ids = []
welcome_message = "Hello"
test_counter = 0

flog = open("log2.txt", "a", encoding="UTF-8")
flog.seek(0)

prior_alert = ["Target Message 1", "Target Message 2"]

#prior_alert = "Внимание,  открыта дополнительная регистрация на рейс AFL103 Нью-Йорк – Москва 30.08.2020 в 19:20 (по местному времени)\n\nЗарегистрироваться на рейс необходимо по ссылке https://www.gosuslugi.ru/395443/1. Количество мест на борту ограничено. Списки будут формироваться на основании регистрации н а госуслугах."
#prior_alert = "Готов список пассажиров рейса AFL103 Нью-Йорк – Москва 30.08.2020 в 19:20 (по местному времени)\n\nПассажиры, включенные в данный список, должны прибыть в аэропорт за 3 часа до вылета."
MIN_RATIO = 75

# key_words = ["Flight", "Внимание", "AFL 103", "по местному", "регистрация на рейс", "Зарегистрироваться на рейс необходимо по ссылке", "AFL103", "23", "Спасибо"]
key_words = ["ZQZ"]


def log(main_string: str):
    global flog
    string = time.ctime(time.time())
    string = string + "\t" + main_string + "\n"
    flog.write(string)
    flog.flush()
    os.fsync(flog.fileno())
    print(string)


# @client.on(events.ChatAction)
# async def chat_event_handler(event: events.ChatAction):
#     global welcome_message
#     print("Chat Action")
#     if event.user_joined or event.user_added:
#         print("Joined")
#         chat = await event.get_chat()
#         if event.chat_id == official_channel_id:
#             bot.send_message(event.user, welcome_message)
#             log("New OC User..." + event.user.id)

@client.on(events.NewMessage)
async def my_event_handler(event: events.NewMessage):
    global testing, mirror_chat_id, receive_chat_id, test_chat_id, official_channel_id, include_chat_ids, testing_include_chat_ids, prior_alert, MIN_RATIO, test_counter
    text = event.raw_text

    chat = await event.get_chat()
    #print(chat.title, event.chat_id, text)

    if text == "Test Here 2004":
        test_chat_id = event.chat_id
        chat = await event.get_chat()
        print("Testing in ", chat.title, " ID: ", test_chat_id)
        bot.send_message(test_chat_id, "Testing Here!")
        log("Test Here " + chat.title + " ID: " + str(test_chat_id))

    elif test_chat_id == 0:
        log("Something / No test_chat_id")
        pass

    elif text == "TESTING NOW 2004":
        testing = True
        test_counter = 2
        chat = await event.get_chat()
        bot.send_message(test_chat_id, "Testing Mode Entered")
        log("Testing Activated" + chat.title + " ID: " + str(event.chat_id))

    elif text == "STOP TESTING NOW 2004":
        chat = await event.get_chat()
        if not testing:
            bot.send_message(test_chat_id, "I wasn't testing")
            log("Fake Testing Disable " + chat.title + " ID: " + str(event.chat_id))

        else:
            testing = False
            test_counter = 0
            bot.send_message(test_chat_id, "Testing Stopped")
            log("Testing Stopped " + chat.title + " ID: " + str(event.chat_id))
            testing_include_chat_ids = []

    elif test_counter > 0:
        if text == "123" or text == "456":
            chat = await event.get_chat()
            testing_include_chat_ids.append(event.chat_id)
            test_counter -= 1
            log("Testing Reception Chat " + chat.title + "ID: " + str(event.chat_id))
        else:
            pass

    elif text == "Mirror Here 2004":
        mirror_chat_id = event.chat_id
        chat = await event.get_chat()
        print("Mirroring in ", chat.title, " ID: ", mirror_chat_id)
        bot.send_message(mirror_chat_id, "I will be sending the 'URGENT' update here in case the other one goes through!")
        log("Mirror Here " + chat.title + " ID: " + str(mirror_chat_id))

    elif text == "Receive Here 2004":
        receive_chat_id = event.chat_id
        chat = await event.get_chat()
        print("Receiving in ", chat.title, " ID: ", receive_chat_id)
        bot.send_message(receive_chat_id, "I will be forwarding matched messages to this chat!")
        log("Receive Here " + chat.title + " ID: " + str(receive_chat_id))

    elif text == "STOP NOW 2004":
        log("REMOTE QUIT: " + chat.title)
        quit()

    # elif text == "Ready Check 2004":
    #     chat = await event.get_chat()
    #     ratio = fuzz.token_sort_ratio(prior_alert, prior_alert)
    #     if not testing:
    #         if ratio >= prior_alert:

    # elif text == "Stop Now 2004":
    #     chat = await event.get_chat()
    #     file_str = file_str + "\tSN " + chat.title + " ID: " + str(event.chat_id) + "\n"
    #     flog.write(file_str)
    #     flog.close()
    #     quit()

    # elif mirror_chat_id == 0 or receive_chat_id == 0:
    #     pass

    # elif mirror_chat_id == event.chat_id or receive_chat_id == event.chat_id or test_chat_id == event.chat_id:
    #     pass

    else:
        ratio = 0
        #ratio = process.extractOne(text, prior_alert, scorer=fuzz.token_sort_ratio)[1]
        #ratio = fuzz.token_sort_ratio(prior_alert, text)
        chat = await event.get_chat()

        if testing:
            ratio = process.extractOne(text, prior_alert, scorer=fuzz.token_sort_ratio)[1]
            if event.chat_id == test_chat_id:
                pass

            elif event.chat_id not in testing_include_chat_ids:
                await event.forward_to(entity=test_chat_id)
                bot.send_message(test_chat_id, "Test...Wrong Chat\t" + str(ratio) + "%")
                flog.write("Test... Wrong Chat: " + text[0:100])

            elif ratio >= MIN_RATIO:
                await event.forward_to(entity=test_chat_id)
                bot.send_message(test_chat_id, "Test...Urgent\t" + str(ratio) + "%")
                flog.write("Test... " + str(ratio) + "% match = URGENT: " + text[0:100])
            else:
                await event.forward_to(entity=test_chat_id)
                bot.send_message(test_chat_id, "Test...Not Urgent\t" + str(ratio) + "%")
                flog.write("Test... " + str(ratio) + "% match = NOT URGENT: " + text[0:100])

        elif event.chat_id != test_chat_id:

            # log(str(ratio) + "% match: " + text[0:100])

            if event.chat_id not in include_chat_ids:
                #print("N/A Percent Match with Prior Alerts: ", text[0:100])
                log("Wrong Chat..." + "no match: " + text[0:100])
                reply = "Wrong Chat..."
                ratio = 0

            else:
                ratio = process.extractOne(text, prior_alert, scorer=fuzz.token_sort_ratio)[1]

            if ratio >= MIN_RATIO:
                await event.forward_to(entity=official_channel_id)
                log("Official Urgent..." + str(ratio) + "% match: " + text[0:100])
                reply = "Urgent..."
                # await event.forward_to(entity=test_chat_id)
                # bot.send_message(test_chat_id, "URGENT")

            elif ratio != 0:
                log("Not Urgent..." + str(ratio) + "% match: " + text[0:100])
                reply = "Not Urgent..."

            if event.chat_id != test_chat_id and ratio != 0:
                await event.forward_to(entity=test_chat_id)
                reply = reply + str(ratio) + "% match"
                bot.send_message(test_chat_id, reply)

        # for word in key_words:
        #     if word in text:
        #         await event.forward_to(entity=receive_chat_id)
        #         bot.send_message(mirror_chat_id, "URGENT")

        flog.flush()
        os.fsync(flog.fileno())

client.start()
client.run_until_disconnected()