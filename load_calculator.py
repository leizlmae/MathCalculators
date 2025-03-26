
def main():
    w = float(input("Enter uniform load per unit length (N/m): "))
    L = float(input("Enter  length of the beam (m): "))
    load = w * L

    print(f"So, the total load acting on the beam is {load} N.")


if __name__ == "__main__":
    main()