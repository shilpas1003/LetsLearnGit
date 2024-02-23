# Function to perform sum of two variables
def sum_of_variables(a, b,c):
    return a + b + c

# Main function
def main():
    # Taking input from user
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    num3 = float(input("Enter the Third num: "))

    # Calculating sum of 3 var
    result = sum_of_variables(num1, num2, num3)

    # Displaying the result
    print("The sum of", num1, "and", num2, "and" ,num3, "is:", result)

if __name__ == "__main__":
    main()