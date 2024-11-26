

statuses = { 
    "Alice" : "online", 
    "Bob" : "offline", 
    "Eve" : "online",
    "Marc" : "online", 
}

online = 0 
for value in statuses.values(): 
    if value == "online": 
        online += 1 

print(f"Online users: {online}") 

