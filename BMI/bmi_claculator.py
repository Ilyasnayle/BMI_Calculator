weight = 0.0
height = 0.0

#Functions to calculate BMI
def calculate_bmi(weight,height):
        return round(weight / (height **2),2)
    
#Convert kg to pound   
def pound_to_kg(pound):
    return pound / 2.20462

#Convert meter to inches
def inches_to_meter(inches):
    return inches / 39.3701


#get UserInput for weight and heigh alongside their units
user_input_weight = int(input('Please enter the weight: '))
weight_unit = input('Please Enter the weight unit in KG or LB: ').lower()
user_input_height = float(input('Please enter the height in meters or inches: '))
height_unit = input('Please enter the height unit in m or in: ').lower()

#checking for the unit, if matched then convert otherwise do not.
if weight_unit == 'lb':
        user_input_weight = pound_to_kg(user_input_weight)
if height_unit == 'in':
       user_input_height = inches_to_meter(user_input_height)
        

#calculating the BMI.  
bmi = calculate_bmi(user_input_weight,user_input_height)

#printing the result of of the claculation.
if bmi < 18.5:
    print(f'\nYour weight is {user_input_weight:.2f} kg and height is {user_input_height:.2f} m')
    print(f"Underweight: BMI is less than 18.5")
elif 18.5 < bmi <24.9:
    print(f'\nYour weight is {user_input_weight:.2f} kg and height is {user_input_height:.2f} m')
    print(f'Normal weight: BMI is between 18.5 to 24.9')
elif 25 < bmi > 29.9:
    print(f'\nYour weight is {user_input_weight:.2f} kg and height is {user_input_height:.2f} m')    
    print(f'Overweight: BMI is between 25 to 29.9')
else:
    print(f'\nYour weight is {user_input_weight:.2f} kg and height is {user_input_height:.2f} m')
    print("BMI is greater than 30")
    
