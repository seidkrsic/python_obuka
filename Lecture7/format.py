

import re 

name = input("What's your name? ") 
# tuple ---- > (1,2,3,3) 
matches = re.search(r"^(.+), ?(.+)$", name) 
if matches: 
    result = matches.group(1) + " " +  matches.group(2) 
    print(result) 

