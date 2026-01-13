m
def main():
    time = input("Please, enter a time  formatted in 24-hour time as #:## or ##:## ")

    time = time.strip()

    time = convert(time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":", 1)

    hours = float(hours)
    minutes = float(minutes)

    time = ((hours * 60) + minutes)/60

    return time


if __name__ == "__main__":
    main()
