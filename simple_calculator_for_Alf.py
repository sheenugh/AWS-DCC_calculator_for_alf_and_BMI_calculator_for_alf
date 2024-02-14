# ========= PSEUDO CODE ==========
# - Printing 'Simple Calculator for Alf'
print("SIMPLE CALCULATOR FOR ALF")

print("\n")

# - Code for asking the user's input
ask_user_the_first_num = float(input("Enter your first desired number:"))
ask_user_the_second_num = float(input("Enter your second desired number:"))
print("What operation you want to use?")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (x)")
print("4. Division (/)")
ask_user_the_operation_desire = input("Enter the operation (1,2,3,4):")

# - Code for performing the calculation based on user's inputted values 
def calculation(value):
    if value == "1":
        result1 = ask_user_the_first_num + ask_user_the_second_num
        return result1
    else: 
        if value == "2":
            result2 = ask_user_the_first_num - ask_user_the_second_num
            return result2
        else:
            if value== "3":
                result3 = ask_user_the_first_num * ask_user_the_second_num
                return result3
            else:
                if value == "4":
                    result4 = ask_user_the_first_num / ask_user_the_second_num
                    return result4
                else: 
                    return "Invalid"
                
result = calculation(ask_user_the_operation_desire)

# - Code for displaying the output
print("The result is", result)