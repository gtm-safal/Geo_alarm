import os
import datetime
import time
import geocoder


def main():
    while True:
        os.system('clear')
        print(get_time())
        print(get_date())
        print("\nLocation:", get_location())


        print("\n1. Check Alarm History")
        print("2. Set Alarm")
        print("\n0. Exit")

        user_choice = input("Choose an option: ")
        
        match(user_choice):
            case '1':
                print("Showing Alarm History... (placeholder)")
            case '2' :
                print("Setting Alarm... (placeholder)")
            case '0':
                print("Exiting. Have a great day!")
                break
            case _:
                print("Invalid option. Try again.")
                pass

        pseudo = input("Press Enter to continue....")


        # time.sleep(5)




def get_time():
    today = datetime.date.today()
    return f"\033[1m{today}\033[0m"

def get_date():
    
    now = time.strftime("%I:%M:%S %p")
    return f"\033[1m{now}\033[0m"

def get_location():
    g = geocoder.ip('me')
    lat, lng = g.latlng

    # Determine N/S and E/W
    lat_dir = 'N' if lat >= 0 else 'S'
    lng_dir = 'E' if lng >= 0 else 'W'

    # Absolute value to remove negative signs
    lat = abs(lat)
    lng = abs(lng)

    return f"\033[1m{lat:.4f}° {lat_dir} {lng:.4f}° {lng_dir}\033[0m"

if __name__ == '__main__':
    main()
