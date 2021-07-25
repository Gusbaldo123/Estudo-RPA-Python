import pyautogui
import time

class mouse:
    def Click(self,position):
        mouse = pyautogui
        mouse.moveTo(position[0], position[1])
        mouse.click()

    def positionCheck(self):
        mouse = pyautogui
        return mouse.position()

    def ScreenClick(self,image):
        self.Click(pyautogui.center(pyautogui.locateOnScreen(image)))

    def ScreenClickPlus(self,image,move):
        width,height = pyautogui.center(pyautogui.locateOnScreen(image))
        self.Click([width+move[0],height+move[1]])

class keyboard:
    
    keyboard = pyautogui
    def OpenProgram(self,winProgram):
        time.sleep(0.1)

        keyboard=self.keyboard

        keyboard.write(winProgram)
        time.sleep(0.1)
        keyboard.press('enter')
        time.sleep(0.4)

    def Write(self,text):
        keyboard = self.keyboard
        keyboard.write(text)
        time.sleep(0.1)

    def Press(self,key):
        time.sleep(0.1)
        keyboard = self.keyboard
        keyboard.press(key)

def CreateFile():
    Mouse = mouse()
    Keyboard = keyboard()
    cantoinfesq = [1,pyautogui.size().height+1]
    Mouse.Click(cantoinfesq)

    Keyboard.OpenProgram('bloco de notas')
    Keyboard.Write('TESTE DO BLOCO DE NOTAS')

    pyautogui.hotkey('ctrl', 's')

    Keyboard.Press('left')
    Keyboard.Press('delete')
    Keyboard.Write('Arquivo Txt')

    Mouse.ScreenClick("Barra.png")
    Keyboard.Write('Desktop')
    Keyboard.Press('enter')

    barposX,barposY = Mouse.positionCheck()
    Mouse.Click([barposX,barposY+390])
    Keyboard.Press('enter')

    time.sleep(.3)
    width,height = pyautogui.size()
    Mouse.Click([width/2+54,height/2-13])
    pyautogui.hotkey('alt', 'f4')

last = 0
while(1>0):
    if(last<0):
        last=800
        CreateFile()
    else:
        last-=.1