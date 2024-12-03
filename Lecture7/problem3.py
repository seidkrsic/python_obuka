

# v4 
# 261.1.1.23  # 0-255
import re 

def main(): 
    ip = input("IP address: ")
    result = validate(ip) 
    print(result) 

# [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}

def validate(ip_address): 
    if re.search(r"^(25[0-5]|2[0-4][0-9]|[1][0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1][0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1][0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1][0-9][0-9]|[1-9]?[0-9])$", ip_address): 
        return True 
    else: 
        return False
     
# [1]?[0-9][0-9]? 
# 03


main() 