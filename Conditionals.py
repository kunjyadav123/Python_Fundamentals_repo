# USER INPUTS :   d=bydefault case of string ! 

# in_str = input("Enter string  :")
# print(in_str*2)   # here 12 is as string  not as number coz bydefault input takes it as string if we doest not specify it as to thr data types .
# print(in_str/2)  # shows error cause we can not divide an string by the number ! 



# in_int = int(input("Enter value :"))  # we can make any number value into the string but opposite is not possible.
# print(in_int)                         # in int input we can only we integral value only.
# print(in_int**2)
# print(in_int+3)



# we got it ! How input works ! 


## In conditional codes not all codes runs infact  only that section of codes runs which is get fullfilled by conditions thats why we call it conditionals .

# always be aware about the scope of if , elif or else what you write within the indentation will comes to print underthat if , elif or else conditions and when any codes comes out of indentation it will print at base level(means it will always get print).
# for example :


age = int(input("Enter age of person :"))
if age < 13:
    print("Baby hai! ")  #  this is within scope of conditional if 
    print("Kid")       # This is also in scope of conditional if 
else:
    print("Young")  
    print("Seniors")
print("Out of scope")   # But this comes out of scope  of conditionals statments coz it comes out of range of indentation. And it will get print unconditionally.


# we may use multiple if's or multiple elif's in conditional but else sirf ek baar hi use ho sakt hai its use for when no condition/no options  left .

# Rememeber we need to pass definetly some condition in if's and elif's but since else is conditionless so plese dont pass any condition in it is case of last or condition less option to get execute.

# Explore about nested conditional statements and , how scope of conditional works and grab notion about the indentation clearly.