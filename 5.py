def sum_digits(number):
    if number<10:
        return number
    else:
        return number%10 + sum_digits(number//10)
x=sum_digits(int(input('Ввести число:')))
print("Число", x)