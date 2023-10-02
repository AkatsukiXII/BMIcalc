height = int(input('Please insert your height: '))
weight = int(input('Please insert your weight: '))

bmi = weight / (height / 100) ** 2
print('Your height: '+ str(height))
print('Your weight: '+ str(weight))
print('Your BMI: '+ str(round(bmi,2)))

