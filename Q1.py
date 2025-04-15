#print 1/1!-2/2!+3/3!-4/4!+5/5!....n/n!
def sum(n):
    sum_result = 0
    fact = 1
    sign = 1  # To alternate between addition and subtraction

    for i in range(1, n + 1):
        fact *= i
        term = i / fact
        sum_result += sign * term
        sign *= -1  # Change the sign for the next term

    return sum_result

# Get user input for the number of terms
n = int(input("Enter the number of terms for the series: "))

# Calculate and display the sum of the series
result = sum(n)
print(f"The sum of the series for {n} terms is: {result:.2f}")
