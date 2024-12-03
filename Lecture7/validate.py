

# regularni izrazi 
import re 

email = input("What's your email? ") 

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE): 
    print("Valid") 
else: 
    print("Invalid") 

""" 
. - bilo koji karakter 
* - 0 ili vise puta 
+ - 1 ili vise put a
? - 0 ili 1 put 
{m} - m - pojavljivanja 
{m,n} - m-n pojavljivanja 
[abc] - skup dozvoljenih karaktera 
[^t] - skup karaktera koji nisu dozvoljeni 
\d - cifre 
\D - nesto sto nije cifra 
\s - blanko karakteri 
\S - nema blanko karaktera 
\w - word char - obicna slova  
\W - not word char 
A|B - ili A ili B 
(...) - group 
(?:...) - group ciji nas sadrzaj ne interesuje 

""" 