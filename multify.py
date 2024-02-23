# Function to perform sum of two variables
def mul_of_variables(a, b):
    return a * b

# Main function
def main():
    # Taking input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculating sum
    result = mul_of_variables(num1, num2)

    # Displaying the result
    print("The mul of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()