# ========= PSEUDO CODE ==========
# BMI - NUTRITIONAL STATUS GUIDE
#   BMI         NUTRITIONAL STATUS

# BELOW 18.5         UNDERWEIGHT
# 18.5 - 24.9       NORMAL WEIGHT
# 25.0 - 29.9        OVERWEIGHT
# ABOVE 30.0          OBESITY

# - Asking the user's weight and height
print("USER'S INFORMATION")
ask_user_weight = float(input("Enter your weight:"))
ask_user_height = float(input("Enter your height:"))

# - Calculations of user's BMI and categorize its status
def bmi_calculation(weight, height):
    return (weight / (height*height))
bmi_result = bmi_calculation(ask_user_weight, ask_user_height)

# - Displaying the user's BMI and its classification
def bmi_classification(value):
    if value < 18.5:
        return "Underweight"
    else:
        if 18.5 <= value <= 24.9:
            return "Normal Weight"
        else: 
            if 25 <= value <= 29.9:
                return "Overweight"
            else: 
                if value > 30.0:
                    return "Obesity"
                else:
                    return "Error"

bmi_classification_result = bmi_classification(bmi_result)
print("\n")
print("SUMMARY OF USER'S BMI")
print("Weight:", ask_user_weight, ";", "Height:", ask_user_height)
print("BMI result:", bmi_result)
print("BMI Classification:", bmi_classification_result)



# Be cautious when reading input of various data types.
# Select and employ a string concatenation method based on your personal preference and comfort level.
