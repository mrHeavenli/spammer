from time import sleep
import pyautogui

run = True
while run:
    print('1 Autoclicker (for sticker)')
    print('2 Typewriter (for text)')
    print('3 Type E to quit')
    o = input('')
    if o == '1':
        x = 0
        o = int(input('How many clicks?'))
        print("You have 6 seconds before the spam starts")
        sleep(6)
        while x != o:
            x += 1
            sleep(1)
            pyautogui.leftClick()
        print('Done!')
    elif o == '2':
        x = 0
        num = int(input('Number of messages to send:'))
        nachricht = input('Content of messages:')
        print("You have 6 seconds before the spam starts")
        sleep(6)
        while x < num:
            x += 1
            pyautogui.typewrite(nachricht)
            pyautogui.press('enter')
        print('Done!')
    elif o == 'E':
        quit()
    else:
        pass
