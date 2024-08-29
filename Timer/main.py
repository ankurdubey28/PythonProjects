import playsound
import time

# ANSI
CLEAR = "\033[2J"
CLEAR_RETURN="\033[H"

def alarm(seconds):
    time_elapsed=0

    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)

        time_elapsed+=1

        time_left=seconds-time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left%60

        print(f"{CLEAR_RETURN}{minutes_left:02d}:{seconds_left:02d}")


    playsound.playsound("TimerSound.mp3")


minu=int(input("Enter Minutes: "))
sec=int(input("Enter seconds :"))
total_time=minu*60+sec
alarm(total_time)