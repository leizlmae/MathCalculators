
def main():
    force = float(input("Enter force applied (N): "))
    area = float(input("Enter  cross-sectional area (mm²): "))
    stress = force / area

    print(f"So, the stress on the beam is {stress:.2f} Pa.")


if __name__ == "__main__":
    main()