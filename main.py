def calculation(weight, height):
    bmi = weight / (height/100) ** 2
    return round(bmi, 1)


def respondent(bmi):.
    if bmi <= 18.5:
        print('You are underweight.')
    elif (bmi >= 18.5) and (bmi <= 24.9):
        print('Your weight is normal. (Health)')
    elif (bmi >= 25) and (bmi <= 29.9):
        print('You are overweight.')
    elif bmi >= 30:
        print('You are fat.')
    else:
        print('Incorrect weight or height.')


def main():
    weight = float(input('Enter your weight (Kilogram): '))
    height = float(input('Enter your height (Centimeter): '))
    bmi = calculation(weight=weight, height=height)

    print(f'\nYour BMI is: {bmi}')
    respondent(bmi)

    input('\nEnter for quit.')


if __name__ == '__main__':
    main()
