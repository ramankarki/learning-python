import time
import curses

win = curses.initscr()
for i in range(100):
    win.clear()
    win.addstr("You have finished %d%%"%i)
    win.refresh()
    time.sleep(.1)
win.clear()
print()
curses.endwin()

#import time
#print("hello", end="\r")
#time.sleep(5)
#print("hi")
#time.sleep(5)
#print("hello")

