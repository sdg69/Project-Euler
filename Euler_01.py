# Find the sum of all multiples of 3 or 5 below 1000

def sum_of_multiples(limit):
    return sum(n for n in range(limit)
               if n % 3 == 0 or n % 5 == 0)

# Run the function with limit = 1000
result = sum_of_multiples(1000)
print(result)




















#     elif  n % 5 == 0:
#         tmp_multiply_by_5 += tmp_multiply_by_5
#         print("multiply by 5")
#
#     answer = tmp_multiply_by_3 + tmp_multiply_by_5

