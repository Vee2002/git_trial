import time

def countdown():
    length_of_countdown = int(input("Enter the number of seconds: ")) 
    while length_of_countdown > 0:
        minutes,seconds = divmod(length_of_countdown,60)
        formatted_time = f"{minutes:02d}:{seconds:02d}"

        print(formatted_time)
        time.sleep(1)

        length_of_countdown -= 1

    #Calculating minutes and seconds using divmod
    return "Countdown Complete"
print(countdown())

# time_now = time.localtime()
# print(time_now)
# # print(time.ctime(time_now))
# import time

# timestamp = time.time()
# local_time = time.localtime(timestamp)

# print("Year:", local_time.tm_year)
# print("Month:", local_time.tm_mon)
# print("Day:", local_time.tm_mday)
# print("Hour:", local_time.tm_hour)
# print("Minute:", local_time.tm_min)
# print("Second:", local_time.tm_sec)