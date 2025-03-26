
def main():
    rise = float(input("Enter the rise (m): "))
    run = float(input("Enter  the run (m): "))
    slope = (rise / run)* 100

    print(f"So,  the slope of the road is {slope:.2f}%")


if __name__ == "__main__":
    main()