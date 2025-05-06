import os
import datetime
import time


def main():
    while True:
        os.system('clear')
        get_time()


def get_time():

    now = time.strftime("%I:%M:%S %p")
    print(f"\033[1m{now}\033[0m")

    today = datetime.date.today()
    print(f"\033[1m{today}\033[0m")
    
    time.sleep(1)
    
if __name__ == '__main__':
    main()