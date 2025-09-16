import schedule
import time
import datetime

def Myschedule():
    print("inside my schedule at:",datetime.datetime.now())
    
def main():
    print("insie auomation script")
    print("Current time is :",datetime.datetime.now())

    schedule.every(10).seconds.do(Myschedule)

    print("application in waitinh state: ")


    time.sleep(50)


if __name__ == "__main__":
    main()