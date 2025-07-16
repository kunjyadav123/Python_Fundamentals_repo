# Here we will see about the Mutable and Non mutalbe databtypes meaning what actuallly they are ! 

# Its is highly advisibe that plese grab the notion and inner working meaning of objects(basically datatypes/variables) , memory management , how assignement works between  memory and objects(variables / datatypes) ,  mutable and immutable datatype and how automatic garbage collection done in python etc . And for best understanding parctice concepts and go to hanrd notes as well.

# Lets Goo! we will just finish basic clarity with 2 examples. see

# Example 

x = 11
y = x
print(x) # Returns 11 fine 
print(y) # returns 11 okay its easy
x = 15 # we reassigned x 
print(x)  # returns 15 okay
# Now actual surprise is here! 
print(y)  # its will even return 11 not 15 actually ! 
# To know why it happens prefer hardnotes they will provide you better understanding of  how referncing and memory allocation works in python .


# Example  : 

user_name = "Pankaj"
print(user_name )  # returns Pankaj simple ! 
user_name = "Kunj"  # reassignment happens here 
print(user_name)  # returns Kunj  as refernce of user_name get shifted from Pankaj to Kunj and with slight delay (since Pankaj is string) it get garbage out automatically.

# Now go to notes  and understand how actually assignment happens , how memory allocation works , how refernces works , how garbage collection works(and how and why the garbage collection happens late in case of string and number daattype) , how assignment works between object( ie. datatypes/ variables) and memory ! 
# Grab it wisely its important.

# Quick facts [ ] are brackets ,( ) are perenthesis , while { } are braces so remember it !


# In Lecture_3.md(yes .md not .py as it gives us page to revies our content as in page format) we will explore about data types  but sadly we cant code in  .md files  so remember it .
# .md means markdown file.

# Remmebere there is differernce between changing the memory value refernces and being  mutable and non mutable see it clearly here! 
# wheather the data type is mutable or immutable you can surely change its  references  but but but
# you cannnot makes changes in an existing value of non mutable datatype value while you can do it for the mutable ones okay.

# atleast get meaning of reg_count and know what sys.getrefcount() method is .