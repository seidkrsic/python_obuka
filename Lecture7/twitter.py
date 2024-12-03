
import re 
url = input("URL: ") 
# www.twitter.com/ronaldo 
# twitter.com/ronaldo
# https://www.twitter.com/ronaldo 
# http://www.twitter.com/ronaldo  
# https://twitter.com/ronaldo 
# http://twitter.com/ronaldo 

# username = re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url) 
matches = re.search(r"(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url) 
if matches:
    print(f"Username: {matches.group(1)}") 