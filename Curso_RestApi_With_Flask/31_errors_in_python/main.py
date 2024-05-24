def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.") #ValueError, RuntimeError, TypeError... 
    
    return dividend / divisor 


grades = []

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades), len(grades))
    
except ZeroDivisionError as e: # e takes the value of the error in the variable.
    print("There are no grades yet in your list.")
else: # if no error happens, the else also executes. 
    print(f"The average grade is {average}.")
    
finally: # the finally will execute always, if the try or catch, dosent matter.
    print("Thank you!")
    