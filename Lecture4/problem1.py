


# emojize libraries 

# i love :thumbs_up: >>> i love 
import emoji 


def main(): 
    x = input("Unesi nesto: ")
    result = get_emoji_text(x) 
    print(result) 

def get_emoji_text(string): 
    return emoji.emojize(string, language="alias")  


if __name__ == "__main__": 
    main() 