# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is 
# entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid 
# number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers 
# from the book for problem 5.1 and Match the desired output as shown.

largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : 
            break

        num = int(num)                        
            
        if largest is None or largest < num:
            largest = num

        if smallest is None or smallest > num:
            smallest = num
            
    except:
        print "Invalid input"
        continue
        
print "Maximum is", largest
print "Minimum is", smallest
