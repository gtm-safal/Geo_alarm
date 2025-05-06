import time
import os


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        get_time()


def get_time():

    now = time.strftime("%I:%M:%S %p")
    print(f"\033[1m{now}\033[0m")
    time.sleep(1)
    
if __name__ == '__main__':
    main()