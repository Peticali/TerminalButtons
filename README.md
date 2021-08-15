# TerminalButtons
Python curses made easy

Clicable Buttons in Linux terminal, Termux, etc




```python
from TerminalButtons import *
import curses

def example(std):
  Tb = TerminalButtons(std)
  Tb.CreateButton(positiony=CENTER,positionx=CENTER,fg=curses.COLOR_BLUE,text='hi')

curses.wrapper(example)
```
