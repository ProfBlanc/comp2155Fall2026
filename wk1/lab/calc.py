import sys

print(sys.argv) # list of args

# 0: always the name of script
# calc.py
# 1 and onwards

#sys.argv[0]	=> 	script name

# ensure that only 2 additional arguments are passed to the script
if len(sys.argv) != 3:
    exit("invalid use of script")

# ensure additionals args are numerical (int/float or either)

try:
    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])

    # output the sum, diff, prod, quot of 2 numbers
    print(n1 + n2, n1 - n2, n1 * n2, n1 / n2, sep='\n')
except:
    print("Execution error")



