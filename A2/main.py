
from Expression import Expression

if __name__ == '__main__':

    # print user prompt for string
    print("Input the string for the expression, no spaces required")
    userInp = input("i.e: a+b*c or abc*+d+\n")

    # print user prompt for infix or postfix notation
    print("0 for infix, 1 for postfix")
    userDir = input("Input the direction\n")

    # create expression with user strings
    myExp = Expression(userInp, userDir)

    # call to methods to convert expression
    if userDir == "0":
        myExp.in_to_post()
    else:
        myExp.post_to_in()

    # print result of evaluated expression
    print("Evaluated expression is", myExp.evaluate())
