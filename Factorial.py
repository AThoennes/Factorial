class Factorial:
    # main method
    def main():

        # prompt user for a number
        num = int(input("Enter a number: "))

        # display the result
        print(num , "! is ", factorial(num))

    # find the factorial value of the passed in number
    #
    # EX.
    #
    # 3! = 3 * (3-1) * (3-2) = 6
    # 3! = 3 * 2 * 1 = 6
    def factorial(n):

        # return 1 if you reached the end
        if (n == 1):
            return 1
        # otherwise return n * n-1
        else:
            return (n * factorial(n - 1))
