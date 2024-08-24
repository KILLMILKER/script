import pyautogui
import time
import random
import string

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def send_message():
    click(780, 752)
    time.sleep(1.9)

    click(944, 751)
    time.sleep(2.3)

    click(828, 893)
    time.sleep(2.9)

    message = "Привет, ты очень мне понравилась, может встретимся? Так же хочу сделать тебе подарок. Напиши мне в телеграм @Ruslan_00345 Буду ждать тебя " + generate_random_string()
    pyautogui.typewrite(message)
    
    click(1179, 878)
    time.sleep(3.0)

    click(698, 120)

def generate_random_string(length=3):
    characters = string.ascii_lowercase + "йцукенгшщзхъфывапролджэячсмитьбю" + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":

    try:
        while True:
            input("Нажмите Enter для запуска скрипта или 'q' для выхода: ")
            send_message()
    except KeyboardInterrupt:
        print("\nСкрипт прерван. Выход...")
