from time import sleep
import pyautogui

run = True

while run:
    print('1 Autoclicker (for sticker)')
    print('2 Typewriter (for text)')
    print('3 Type E to quit')
    
    option = input('')
    
    if option == '1':
        i = 0
        option = int(input('How many clicks?'))
        
        print("You have 6 seconds before the spam starts")
        sleep(6)
        
        while i != option:
            i += 1
            sleep(1)
            
            pyautogui.leftClick()
        
        print('Done!')
    
    elif option == '2':
        i = 0
        
        num = int(input('Number of messages to send:'))
        msg = input('Content of messages:')
        
        print("You have 6 seconds before the spam starts")
        sleep(6)
        
        while i < num:
            i += 1
            
            pyautogui.typewrite(msg)
            pyautogui.press('enter')
        
        print('Done!')
    
    elif option == 'E':
        quit()
    
    else:
        pass
