import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('\nCountdown Over!')
try:
    c = int(input("enter countdown time :"))
    countdown(c)
except:
    print("give correct input in numbers format")
#program complete
