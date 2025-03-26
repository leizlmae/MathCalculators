
def main():
    length = float(input("Enter length of the sidewalk (m): "))
    width = float(input("Enter width of the sidewalk (m): "))
    depth = float(input("Enter depth of the sidewalk (m): "))
    volume = length * width * depth

    print(f"So, you need {volume} cubic meters of concrete.")


if __name__ == "__main__":
    main()