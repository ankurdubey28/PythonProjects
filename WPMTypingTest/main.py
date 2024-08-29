import curses
import time
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing test!")
    stdscr.addstr("\n Press Any key to begin ")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM:{wpm}")

    for i,char in enumerate(current):
        correct_char=target[i]
        color=curses.color_pair(1)
        if char!=correct_char:
            color=curses.color_pair(2)
        stdscr.addstr(0,i,char, color)



def wpm_test(stdscr):
    target_text="some test text for test"
    current_text=[]
    wpm=0
    start_time=time.time()
    while True:
        elapsed_time = (time.time() - start_time) / 60  # Time in minutes
        if elapsed_time > 0:
            wpm = len(current_text) / 5 / elapsed_time
        else:
            wpm = 0
        stdscr.clear()
        display_text(stdscr,target_text,current_text,int(wpm))
        stdscr.refresh()
        key=stdscr.getkey()

        if ord(key)==27:
            break

        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)





def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)  # Corrected function name
