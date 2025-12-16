A = float(input("Enter a number with two decimal places: "))
integer_part = int(A)      
fractional_part = int(round((A - integer_part) * 100)) 
new_number = fractional_part + integer_part / 100
print(new_number)
