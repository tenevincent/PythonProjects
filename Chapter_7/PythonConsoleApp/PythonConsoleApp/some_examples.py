
# https://www.geeksforgeeks.org/python-string-interpolation/

def user_defined_input():
     message = input("Tell me something, and I will repeat it back to you: ")
     print(message)
     name = input("Please enter your name: ")
     print(f"\nHello, {name}!")





def string_interpolation_01():
    #string interpolation
    # Python program to demonstrate
    # string interpolation
    n1 = 'Hello'
    n2 = 'GeeksforGeeks'
    # for single substitution
    print('Hello, {}'.format(n1)) 
    # for single or multiple substitutions
    # let's say b1 and b2 are formal parameters
    # and n1 and n2 are actual parameters
    print("{b1}! This is {b2}.".format(b1 = n1, b2 = n2)) 
    # else both can be same too
    print("{n1}! This is {n2}.".format(n2 = n2, n1 = n1)) 


def string_interpolation_02():

    # Python program to demonstrate 
    # string interpolation 
    n1 = 'Hello'
    n2 ='GeeksforGeeks'
    # for single substitution 
    message = "Welcome to % s" % n2
    print(message) 

    # for single and multiple substitutions () mandatory 
    print("% s ! This is % s."%(n1, n2)) 


def string_interpolation_03():
    # Python program to demonstrate 
    # string interpolation 
    n1 = 'Hello'
    n2 ='GeeksforGeeks'

    # for single substitution 
    print('Hello, {}'.format(n1)) 

    # for single or multiple substitutions 
    # let's say b1 and b2 are formal parameters 
    # and n1 and n2 are actual parameters 
    print("{b1}! This is {b2}.".format(b1 = n1, b2 = n2)) 

    # else both can be same too 
    print("{n1}! This is {n2}.".format(n2 = n2, n1 = n1)) 


def string_interpolation_04():
    # Python program to demonstrate 
    # string interpolation 


    from string import Template 

    n1 = 'Hello'
    n2 ='GeeksforGeeks'

    # made a template which we used to 
    # pass two variable so n3 and n4 
    # formal and n1 and n2 actual 
    n = Template('$n3 ! This is $n4.') 

    # and pass the parameters into the template string. 
    print(n.substitute(n3 = n1, n4 = n2)) 







def string_interpolation():

    # string_interpolation_01()
    # second 
    # string_interpolation_02()
    # third 
    # string_interpolation_03()

    string_interpolation_04()