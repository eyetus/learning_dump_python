# BMI Calculator

def gather_info():
    height = float(nput("What is your height? (inches or meters) "))
    weight = float(nput("What is your weight? (pounds or kilograms) "))
    unit = input("Are your mearsurements in metric or imperial units? ").lower().strip()
    return (height, weight, unit)


def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    print(f"Your BMI is {bmi}")


while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(weight, unit='imperial', height=height)
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")

