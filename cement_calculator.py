
def main():
    C1 = float(input("Enter concentration of original slurry (g/L): "))
    C2 = float(input("Enter desired concentration of diluted slurry (g/L): "))
    V2 = float(input("Enter volume of diluted slurry to be prepared (L): "))
    V1 = (C2*V2)/C1

    print(f"So, you need {V1:.2f} liters of the original slurry.")


if __name__ == "__main__":
    main()