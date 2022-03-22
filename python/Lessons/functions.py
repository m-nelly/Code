def functions(): 
    # everything you have executed so far has been part of a function. 
    # functions are self contained blocks of code that can be reused many times.
    
    # let's write a function to reverse a string that you pass in as a parameter.

    def streverse(str):
        print(str[::-1])

    streverse("Hello!")
    streverse("World!")
    streverse("")# try your own!

    # if your function accepts arguments, each argument must be represented when the function is called.

    # if you are unsure of how many arguments you will need, add an * before the argument.
    # this will allow you to accept an arbitrary number of arguments as a tuple.

    def sumofnum(*num):
        print(sum(num))
    sumofnum(100, 50, 3)

    # keyword arguments allow a key:value syntax to be used instead of ordered arguments.

    def profile(name, age, email):
        print(name, age, email)
    profile(name = "John Doe", age = 34, email = "jdoe@company.example.com")

    # recursive functions are functions that call themselves, mind the infinite loop.

    def recursion_example():
        
        i = input("2^x, x = ") # get user input. 
    
        x = int(i) # convert to integer.
    
        def recursion(x): 
        
            if x > 0: 
                y = (2 ** x) # exponentiate 2^x.
        
                print(y) # print result.

                x -= 1 # decrement x by 1.

                recursion(x) # run the function again. 
            else:
                print("Finished!") # when the loop ends, print "Finished!"
        recursion(x) # initial function call to start loop.

    recursion_example() # parent function call to define variables and get input.

    return()

def lambda_functions():
    # lambda functions are small, undefined functions.

    # the best way to illustrate this is with an example.

    def lambda_ex(n):
        return lambda a : a * n 
    
    double = lambda_ex(2)
    triple = lambda_ex(3)

    print(double(5))
    print(triple(3))

    # think of lambda functions as a more discrete way to write a function.
    # as our programs become more complex, the need for simplified code becomes more apparent.
    # for now it is only important that you recognize lambda functions, not that you can write them.

    return()

def dates():
    # the datetime module is required to work with dates. 
    import datetime 

    datetime.datetime.now() # returns current date and time. 

    datetime.datetime(2020, 5, 21, 0, 30,) # returns a specific date and time. 

    # as with most date formatting libraries, there is a formatting table to get your date into the proper readable format. 
    # for now, this is as deep as we will go. 
    return()

def math():
    # the math library contains an extended set of prebuilt mathematical functions.
    import math

    testRange = (0, 30, 100, 50, 10, 0)
    x = -4

    print( 'Min:' + str(min(testRange)))
    print( 'Max:' + str(max(testRange)))
    print('Absolute value of x: ' + str(abs(x)))

    print('|x|! = ' + str(math.factorial(abs(x))))

    # math is a pretty easy module to get a grasp of; however, it is important to know it is there. 
    return()