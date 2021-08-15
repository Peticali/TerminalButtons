# TerminalButtons
Python curses made easy

Clicable Buttons in Linux terminal, Termux, etc

![Captura de Tela 2021-08-15 às 08 03 05](https://user-images.githubusercontent.com/34588988/129476983-85d7be6c-b261-428f-977c-3149e975d35f.png)



Example:
```python
from TerminalButtons import *
import curses

def example(std):
    Tb = TerminalButtons(std)
    Tb.CreateButton(positiony=CENTER,positionx=CENTER,fg=curses.COLOR_BLUE,text='hi')
    Tb.mainLoop()

curses.wrapper(example)
```

Methods:
```python
CreateButton(self,positionx,positiony,fg,bg,commmand,text,row,col,typeText)
#positions = Top,Left,Bottom,Right
#fg,bg = curses COLOR (Foreground,Background Color)
#command = Function to run when click the button (without '()')
#row,col = padding
#typeText = curses BOLD,ITALIC,etc

ReqInput(self,x,y)
#x,y = coords where input will show up
#returns the string typed

AddKeyEvent(self,key,func)
#key = curses KEY
#func = Function to run when event fire

ConfigureBg(self,bg,fg)
#bg,fg = curses COLOR (will change the screen colors)

mainLoop(self)
#principal loop

ClearScreen(self)
#i need to document this?

GetMaxYX(self)
#returns the char size of terminal (x,y)

Exit(self)
#breaks the mainLoop and exit
```

