from mean_var_std import calculate

# Example input list
data = [0, 1, 2, 3, 4, 5, 6, 7, 8]

try:
    result = calculate(data)
    print("Mean-Variance-Standard Deviation Calculations:")
    print(result)
except ValueError as e:
    print(e)
