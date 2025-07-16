
# LETS SEE BASIC BACK WORKING OF PYTHON ! AND HERE BE  SUPER ATTENTIVE ! 


print("Hello World")

def chai(n):   # methods by function.
    print(n)

chai("Lemon Tea")  # methods 
chai("Mango Tea")
chai("Chicken chai")

chai_one  = "Nepali chai"  # attributes 
chai_two = "UP CHAI"   # attributes



# Nothing new but here we will sent this method to other file name as file1.py  and understand the actual back working of python . so chill! 
# so we here imports one file code , function , method into other file see how we do it .

# Now prefer hardnotes for better understanding of inner working of python, .pyc, __pycache__ , PVM, Bytes codes , how garbage collection works and how and why garbage collcetion  is different in case of string , numbers datatypes , how referncing works in variables , diiference in being same and being equal refrenced  etc . so explore as much as you can .
# here we will see more practicals.
# ls command is used to get the idea of list of files and folder in current working directory. we can 


# get super familiar with how coding works  in the terminal(>>>) or shell(>>>) IDE and there s lot of similirity as per usual files codes but again their are several advantage and  disadvantage  of coding in usual file vs coding in shell/terminal so see in notes.




# importing module and using their method , property and function is valid in terminal  just like normal code blocks .

import os  # os is preinstallled module(no need to install just import and use) in python so when we import os in python it get inculcates the all methods , property,function of os module in the pythons directory and than we can explore lot of their method and property  lets seee! 
os.getcwd()  # see there os.getcwd( ) is method used to get our current working directory (cwd) as os module . 


#Let see one more ! 


import sys  # sys  stand for system .
sys.platform  # this property let us know us about the Operating system platform we are  using. as it returns win32  here which is true  



# we can obaviously import  our directory file to terminals or in normal other files as well using import and more important that we can use that remote(others) files method and properties as well  as well there so grab facts , figures and practice hard .
# And one more things we can acces the imported files attributes by their name but to do it firtsly we need to impotrs some other supporting modules which gives some leverage as so to do if follw given step!

# step1 : Import the directory(file) in terminal or in other normal files  whose atttributes and properties  you want to access. just use import file_name. and when we import it will give you all printed code instantly.
# step2 : write given command then as  :   from importlib import reload , #   we uses this command to use the method , attributes of imported files in other file.
# step : reload(file_name) it willl gives(basically import) you all codes output values of file and after this we may accces the atttribute of the files by there name.
# step : access attribute value using the   file_name.attribute_name  , eg as   Lecture_1.chai_one   , Lecture_2.chai_two . 

# remember difference between method and properties/attributes.

# remember above 4 steps are if we wish to use attribute or properties  but agar normal method use karna hai to sirf normal import file_name  se kaam ho jagea .