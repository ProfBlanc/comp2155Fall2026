import sys

if len(sys.argv) < 2:
    exit("Not enough arguments")

nums = []
for n in sys.argv[1:]:
    nums.append(float(n))

# [ final_value for placeholder_value in list_of_values]

r_nums = [round(n) for n in nums]

for n in r_nums:
    print(n)