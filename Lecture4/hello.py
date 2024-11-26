


import sys 

# check for errors 
if len(sys.argv) < 2: 
    sys.exit("Too few arguments.") 

# slice dijela stringa -- i dijela liste 
for arg in sys.argv[1:]: 
    print("Hello my name is", arg.title()) 


  


