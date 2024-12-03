


import re 

def main(): 
    log_file = "access1.log" 
    ips = find_ip_adresses(log_file) 
    print("IP adresses found: ") 
    print(len(ips)) 
    for ip in ips: 
        print(ip)  


def find_ip_adresses(log_file): 
    ip_adresses = set() # {}
    with open(log_file, "r") as file: 
        for line in file: 
            ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.d{1,3}", line) 
            ip_adresses.update(ips) 
    
    return ip_adresses


if __name__ == "__main__": 
    main() 