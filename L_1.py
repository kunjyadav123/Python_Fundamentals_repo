# Problem 1 : counting postive numbers! 

number = [1,-2,3,-4,5,-6,7,-8,9,-10]
positive_number_count = 0

for val in number:
    if val > 0:
        positive_number_count += 1

print("Final Count of Positive Numbers :",positive_number_count) 
