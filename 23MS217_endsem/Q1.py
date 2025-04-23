# Newton forward (Near start data point)
def newton_forward(x, y, value):
    n = len(x)
    h = x[1] - x[0]  # Step size (equispaced)
        # Step 1: Build forward difference table
    diff_table = [list(y)]  # First column is y values
    for i in range(1, n):
        current_col = []
        for j in range(n - i):
            val = diff_table[i-1][j+1] - diff_table[i-1][j]
            current_col.append(val)
        diff_table.append(current_col)
    # Step 2: Print the difference table
    print("Forward Difference Table:")
    for i in range(n):
        row = f"{x[i]}\t"
        for j in range(n - i):
            row += f"{round(diff_table[j][i], 4)}\t"
        print(row)
    # Step 3: Calculate u = (value - x0)/h
    u = (value - x[0]) / h
    # Step 4: Apply Newton's formula
    result = y[0]
    u_term = 1  # u(u-1)(u-2)... term
    factorial = 1
    for i in range(1, n):
        u_term *= (u - (i - 1))
        factorial *= i
        result += (u_term * diff_table[i][0]) / factorial
    return result
# Given values
x = [2005,2010,2015,2020,2025]  # Years
y = [1154,1243,1328,1402,1463]  # Population in million
value = 2008
# printing of desired value
print("Estimatation of the Indian population in 2008.: ",newton_forward(x, y, value))
