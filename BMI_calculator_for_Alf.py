# ========= PSEUDO CODE ==========
# BMI - NUTRITIONAL STATUS GUIDE
#   BMI         NUTRITIONAL STATUS

# BELOW 18.5         UNDERWEIGHT
# 18.5 - 24.9       NORMAL WEIGHT
# 25.0 - 29.9        OVERWEIGHT
# ABOVE 30.0          OBESITY

# - Asking the user's weight and height
ask_user_weight = float(input("Enter your weight:"))
ask_user_height = float(input("Enter your height:"))

print("\n")
# - Calculations of user's BMI and categorize its status
def bmi_calculation(weight, height):
    return (weight / (height*height))

bmi_result = bmi_calculation(ask_user_weight, ask_user_height)
print(bmi_result)

print("\n")
# - Displaying the user's BMI and its classification
# print("Weight", ask_user_weight, "Height", ask_user_height, end = " ")
# print("BMI", )



# Be cautious when reading input of various data types.
# Select and employ a string concatenation method based on your personal preference and comfort level.


# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.