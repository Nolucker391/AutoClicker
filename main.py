import pyautogui

if __name__ == '__main__':
    # button="SECONDARY" - НАЖАТИЕ ПРАВОЙ КНОПКОЙ МЫШИ
    # button="MIDDLE" - НАЖАТИЕ КОЛЕСИКОЙ МЫШИ
    # pyautogui.click(1000, 500, 1000, 0.1) - простой кликер левой пкм интервал 0.1, кол-во нажатий 1000
    # pyautogui.doubleClick(1000, 500, 0.1) - двойной клик
    #pyautogui.moveTo(1000,500, 2) # перемещение мышки
    #pyautogui.dragTo(100, 1000,2) # перетаскивание мыши с выделением

    #pyautogui.scroll(100) #движение колесико, по умолчанию вверх,если вних то -100

    # pyautogui.moveTo(1220, 1049,1)
    # pyautogui.click()
    # pyautogui.moveTo(953, 585,1)
    # pyautogui.click(clicks=1000, interval=0.1)



    # pyautogui.moveTo(1264, 1063,1.5)
    # pyautogui.click()
    # pyautogui.moveTo(1636, 16, 1.5)
    # pyautogui.click()
    # pyautogui.moveTo(993, 418, 1.5)
    # pyautogui.click()
    # pyautogui.moveTo(915, 509, 1.5)
    # pyautogui.click()
    # pyautogui.moveTo(383, 363, 1.5)
    # pyautogui.click()
    # pyautogui.sleep(2.5)
    # pyautogui.moveTo(824, 725, 1.5)
    # pyautogui.click()




    while True:
        xy_coordinates = pyautogui.position() # получаем координаты мыши
        print(xy_coordinates)
        pyautogui.sleep(0.5) # делаем паузу, чтобы не спамила быстро



