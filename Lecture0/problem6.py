

""" 
omoguciti unos nekog stringa
izmijeniti string na sljedeci nacin: 
python >>> P*thon!!!
java >>> J*va!!!
""" 
x = input("Unesi neki tekst: ") 
x = x[0].title() + "*" + x[2:] + "!!!" 
print(x) 
