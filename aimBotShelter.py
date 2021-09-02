import pyautogui
import time

cont = 0
temp = 'tchau'
while temp != 'oi':
    time.sleep(4)
    sc = pyautogui.screenshot(region=(261, 276, 895, 362))
    sc.save('img1.png')
    largura, altura = sc.size
    for x in range(0,largura,20):
        for y in range(0,altura,20):
            r,g,b = sc.getpixel((x,y))
            if r == 17 and g == 255 and b == 21: #Itens
                pyautogui.mouseDown(261+x, 276+y)
                pyautogui.mouseUp(261+x, 276+y)
                print('laco 1')
                time.sleep(1)
    time.sleep(4)
    sc = pyautogui.screenshot(region=(261, 276, 895, 362))
    sc.save('img2.png')
    largura, altura = sc.size
    for x in range(0,largura,10):
        for y in range(0,altura,10):
            r,g,b = sc.getpixel((x,y))
            if r == 18 and g == 255 and b == 21: #lvl up
                pyautogui.mouseDown(261 + x, 276 + y)
                pyautogui.mouseUp(261 + x, 276 + y)
                print('laco 2')
                time.sleep(1)
    time.sleep(4)
    sc = pyautogui.screenshot(region=(261, 276, 895, 362))
    sc.save('img3.png')
    largura, altura = sc.size
    for x in range(0, largura, 10):
        for y in range(0, altura, 10):
            r, g, b = sc.getpixel((x, y))
            if r == 1 and g == 255 and b == 2:
                pyautogui.mouseDown(261 + x, 276 + y)
                pyautogui.mouseUp(261 + x, 276 + y)
                print('laco 3')
                time.sleep(1)
                
