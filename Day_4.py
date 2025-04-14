# Operators and its types 
# Arithmetic,Assignment,Relational(comparison),Logical,Bitwise operators

# Arithmetic(+,-,*,/,//,%)
number1 = 10
number2 = 20
add = number1+number2
sub =  number1-number2
div = number1/number2
mul = number1*number2
rem = number1%number2
fdiv = number1//number2
exp = number1**number2
print(add)
print(sub)
print(div)
print(rem)

#Assigment operations(=,+=,-=,*=,%=,...)
a = 12
a = a+1
print(a)
a += 1
print(a)
a -= 1
print(a)
a *= 1
print(a)
a /= 1
print(a)
a %= 5
print(a)

# Relation (comparison)
boy = 10
girl = 20
print(boy>girl)
print(boy<girl)
print(boy>=girl)
print(boy<=girl)
print(boy==girl)
print(boy!=girl)

# Logical operators (AND,OR,NOT)
# AND - if BOTH of the inputs are HIGH(TRUE) and the outputs is high
# OR - If any one of the inputs are HIGH(TRUE) and the outputs are high
# NOT - inverts the output as True to false and False to True
input1 = 1
input2 = 2
input0 = 0
print(input1 and input2)
print(input1 and input0)
print(input2 and input0)
print("" and input1)
print(2 and 3)
print(3 and 2)
print(1+2j and 0+0j)
print(True and True)
print(False and True)
print(True and False)
print(False and False)
print([1,2,3] and [])
print({} and {})


input1 = 1
input2 = 2
input0 = 0
print(input1 or input2)
print(input1 or input0)
print(input2 or input0)
print("" or input1)
print(2 or 3)
print(3 or 2)
print(1+2j or 0+0j)
print(True or True)
print(False or True)
print(True or False)
print(False or False)
print([1,2,3] or [])
print({} or {})

print(not True)
print(not False)

# Bitwise operators - These operators are optimised version of Logical or extension of Logical operators
# &,|,^,~,<<,>>.
bin1 = 0b01010 
bin2 = 0b10101
bin3 = 10
bin4 = 20
print(bin1 & bin2)
print(bin1 | bin2)
print(bin1^bin2)
print(~bin1)
print(~bin2)
print(int(bin2))
print(bin1>>1)
print(bin2<<1)

print(bin3 & bin4)
print(bin3 | bin4)
print(bin3 ^ bin4)
print(~bin3)
print(~bin4)