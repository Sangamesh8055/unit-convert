# unit_converter.py
def convert_to_meters(feet):
    return feet * 0.3048

user_input = float(input("Enter length in feet: "))
result = convert_to_meters(user_input)
print(f"{user_input} feet is equal to {result} meters.")

