

import sys 

count = 0 
if len(sys.argv) != 2: 
    sys.exit("Not valid arguments.") 
else: 
    try: 
        if sys.argv[1].endswith(".py"): # True/False 
            with open(f"{sys.argv[1]}", "r") as file: 
                for line in file: 
                    nice_line = line.strip()  
                    if nice_line != "": 
                        if "#" in nice_line: 
                            if nice_line.startswith("#"): 
                                pass 
                            else: 
                                count += 1 
                        else: 
                            count += 1  
                    else: 
                        pass 

        else: 
            raise ValueError("Not a Python File")         
    except FileNotFoundError: 
        sys.exit("File does not exists.") 
    except ValueError as error: 
        sys.exit(error) 

print(count) 