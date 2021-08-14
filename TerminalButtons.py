import curses,sys

CENTER = 'center'
LEFT = 'left'
RIGHT = 'right'
BOTTOM = 'bottom'
TOP = 'top'

class TerminalButtons:
    
    def assignList(self,aa,ab,h,c):
        #list with all objs coords (first char,last,height)
        self.Buttons[str(self.countObj)] = [aa,ab,h,c]

    def CreateButton(self,positionx='left',positiony='center',bg=curses.COLOR_WHITE,fg=curses.COLOR_BLACK,commmand=None,text='test',row=0,col=0):
        curses.init_pair(self.countObj, fg, bg)

        hm, wm = self.std.getmaxyx()
        
        if positionx == 'center':
            w = wm//2
            w = w - len(text)//2 + col
        if positiony == 'center':
            h = hm//2 + row
        if positionx == 'left':
            w = 0 + col
        if positiony == 'top':
            h = 0 + row
        if positionx == 'right':
            w = wm - len(text) + col
        if positiony == 'bottom':
            h = hm - 1 + row

            
        self.std.attron(curses.color_pair(self.countObj))
        self.std.addstr(h, w, text)
        self.std.attroff(curses.color_pair(self.countObj))

        finalt = w + len(text)
        self.assignList(w,finalt,h,commmand)
        self.countObj = self.countObj + 1

    def ReqInput(self, x, y):
        curses.echo()
        curses.nocbreak() 
        self.std.refresh()
        input = self.std.getstr(x, y)

        self.CreateButton(color=curses.COLOR_CYAN,text=input)
        curses.noecho()
        curses.cbreak()
        return input 

    def mainLoop(self):
        debug = False
        while self.running:
            self.std.refresh()
            key = self.std.getch()

            if key == curses.KEY_MOUSE:
                _, x, y, _, _ = curses.getmouse()

                if debug: self.CreateButton(color=curses.COLOR_MAGENTA,text=str(self.Buttons['1'])+'%i %i' % (x,y))
                
                buttons = self.Buttons
                try:
                    for i in buttons:
                        obj = self.Buttons[i]
                        aa,ab,h,c = obj

                        if y == h and x in range(aa,ab):
                            if c != None:
                                c()
                except:pass
        
            elif key == 27:
                sys.exit()
                
    def ClearScreen(self):
        self.std.clear()
        self.Buttons = {}

    def Exit(self):
        self.running = False

    def __init__(self,std,cursor=0):
        self.Buttons = {}
        self.countObj = 1
        self.std = std
        self.running = True
        curses.curs_set(cursor)
        curses.mousemask(1)



if __name__ == '__main__':
    def main(stdscr):

        Tb = TerminalButtons(stdscr)
        Tb.CreateButton(positiony=CENTER,positionx=CENTER,fg=curses.COLOR_BLUE,text='center',commmand=Tb.ClearScreen)

        Tb.CreateButton(positiony=TOP,positionx=CENTER,fg=curses.COLOR_BLUE,text='top',commmand=Tb.ClearScreen)
        Tb.CreateButton(positiony=BOTTOM,positionx=CENTER,fg=curses.COLOR_BLUE,text='bottom',commmand=Tb.ClearScreen)
        Tb.CreateButton(positiony=CENTER,positionx=RIGHT,fg=curses.COLOR_BLUE,text='right',commmand=Tb.ClearScreen)
        Tb.CreateButton(positiony=CENTER,positionx=LEFT,fg=curses.COLOR_GREEN,text='left',commmand=lambda:[Tb.my_raw_input(1,1,'teste')])
        
        Tb.CreateButton(positionx=CENTER,positiony=CENTER,bg=curses.COLOR_GREEN,text='Click for Input',row=2)
        Tb.mainLoop()

    curses.wrapper(main)