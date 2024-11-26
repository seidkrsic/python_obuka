

from tabulate import tabulate 

import csv 
import sys 

if len(sys.argv) == 2: 
    try: 
        if not sys.argv[1].endswith(".csv"): 
            raise ValueError("Not a CSV file.") 
        else: 
            with open(f"{sys.argv[1]}", "r") as file: 
                if sys.argv[1] == "sicilian.csv": 
                    headers = ["Sicilian Pizza", "Small", "Large"]
                    reader = csv.DictReader(file, fieldnames=["Sicilian Pizza", "Small", "Large"]) 
                elif sys.argv[1] == "regular.csv":
                    headers = ["Regular Pizza", "Small", "Large"]
                    reader = csv.DictReader(file, fieldnames=["Regular Pizza", "Small", "Large"]) 
                else: 
                    raise ValueError("Not valid CSV file.") 

                data = [] 
                # popunimo podatke u data 
                next(reader)  
                for row in reader: 
                    data.append([row[headers[0]],row["Small"], row["Large"]])

                table = tabulate(data, headers=headers, tablefmt="grid")
                print(table) 


    except ValueError as error: 
        sys.exit(error) 
    except FileNotFoundError: 
        sys.exit("File does not exists.") 

else: 
    sys.exit("Not valid arguments.")



