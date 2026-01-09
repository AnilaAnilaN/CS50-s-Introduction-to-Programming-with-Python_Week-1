def main():

    #taking input from the user
    math_expression = input("Please, enter a mathematical expression in the following format => 'x + y' " \
    "where x and z are the first and second operands respectively and y is the operator. " \
    "The supported maths operations are '+, - , * , /': ")

    #removing any extra spaces before and after the expression user entered
    math_expression = math_expression.strip()


    #splitting the expression into three values and saving those values into three different variables
    x, y, z = math_expression.split(" ", 2)

    # a function to perform math operations
    def calculate(x, y, z):

        # converting string operands
        x = int(x)
        z = int(z)

        #result variable will store the result of a maths operation
        result = 0

        if y == "+":
            result = x + z
        elif y == "-":
            result = x - z
        elif y == "*":
            result = x * z
        elif y == "/":
            if(z==0):
                print("z cannot be zero")
            else:
             result = x / z


        #converting result to a foloating point value and rounding it to 1 decimal point
        result = float(result)
        result = round(result, 1)

        #this functions returns the value of result
        return result


    print(calculate(x, y, z))


main()
