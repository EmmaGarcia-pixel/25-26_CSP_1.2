# Make 3 Methods following the details given here.
# Method 1: name it "tic" and it takes 2 parameters "num1" and "num2" and returns
# The value of the 2 parameters when subtracted (ie: num1 - num2)
def tic(num1, num2):
    total = num1 - num2
    return total

# Method 2: name it "tac" and it takes one parameter "exp"
# use a loop to multiply the number 5 by itself "exp" times
# return that value
def tac(exp):
    sum = 5
    for num in range(exp):
        sum = sum * 5
    return sum



# method 3: name it "toe" that makes no parameters. This method
# should print the results of a method call to "tic(3, 5)" and "tac(4)" to the console.
def toe():
    print(tic(3,5))
    print(tac(4))