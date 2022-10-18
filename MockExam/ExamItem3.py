# Note:
#   Complexity of O(N) as it has to iterate through the entire list
# Step 1:
#   Since the Fibonacci is a recurrence of F(n) = F(n-2) + F(n-1) (e.g. 3rd num = 1st num + 2nd num)
#   we need to seed the first 2 values which are 0 and 1
# Step 2:
#   Check the first 2 values which are 0 and 1 if they are less than the value to be compared
#   and display accordingly
# Step 3:
#   Take the sum of our current and next numbers (the initial iteration it will be current = 0 and next = 1)
# Step 3:
#   if sum > the value to be compared then exit the loop
# Step 4:
#   Display the sum.
# Step 5:
#   Repeat step 2 and 3 while setting the new values current = next and next = sum.

def Get_Fibonacci(val_to_compare):
    fib_list = []

    if val_to_compare < 0:
        return "incorrect input value"

    if val_to_compare >= 0:
        fib_list.append(0)
    if val_to_compare >= 1:
        fib_list.append(1)
    if val_to_compare > 1:
        Fibonacci(fib_list=fib_list, val_to_compare=val_to_compare)

    return fib_list


def Fibonacci(fib_list, val_to_compare):
    n_minus_2 = fib_list[len(fib_list)-2]
    n_minus_1 = fib_list[len(fib_list)-1]
    new_fib_val = n_minus_2 + n_minus_1

    if val_to_compare < new_fib_val:
        return

    fib_list.append(new_fib_val)

    Fibonacci(fib_list=fib_list, val_to_compare=val_to_compare)


print(Get_Fibonacci(1))
print(Get_Fibonacci(6))
print(Get_Fibonacci(145))
