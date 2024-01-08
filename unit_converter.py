# unit_converter.py
import sys

def convert_to_meters(feet):
    return feet * 0.3048

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python unit_converter.py <length_in_feet>")
        sys.exit(1)

    try:
        user_input = float(sys.argv[1])
        result = convert_to_meters(user_input)
        print(f"{user_input} feet is equal to {result} meters.")
    except ValueError:
        print("Invalid input. Please provide a valid number.")
        sys.exit(1)
