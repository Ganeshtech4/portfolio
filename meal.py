def main():
    meal = input("What Time is it?: ")
    time = convert(meal)
    print(time)


def convert(time):
        hours, minutes = time.split(":")
        minute = float(minutes) / 60
        return float(hours) + minute


if __name__ == "__main__":
    main()