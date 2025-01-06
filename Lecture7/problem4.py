
# test unos
# <iframe height="200" src="https://www.youtube.com/embed/akks-q3whiuw4s" width="100" class="flex"><\iframe>
# <iframe src="https://youtube.com/embed/akks-q3whiuw4s"><\iframe> 
# <iframe src="http://youtube.com/embed/akks-q3whiuw4s"><\iframe> 
# <iframe src="https://www.youtube.com/embed/akks-q3whiuw4s"><\iframe> 

# https://youtube.com/embed/akks-q3whiuw4s >>> https://youtu.be/akks-q3whiuw4s 
# http://youtube.com/embed/akks-q3whiuw4s >>> https://youtu.be/akks-q3whiuw4s

import re 

def main(): 
    link = input("Unesi youtube link: ")
    print(parse1(link)) 
# src="(https?://(?:www.\)?youtube\.com/embed/.+)"
def parse1(link):
    matches = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"', link) 
    if matches: 
        youtube_link = matches.group(1)
        if "www" in youtube_link: 
            if youtube_link.startswith("https"):
                pass 
            else: 
                youtube_link = youtube_link.replace("http", "https")
            youtube_link = youtube_link.replace("www.youtube.com/embed/", "youtu.be/")
        else: 
            if youtube_link.startswith("https"):  # https://youtube.com/embed/akks-q3whiuw4s
                pass 
            else: 
                youtube_link = youtube_link.replace("http", "https")

            youtube_link = youtube_link.replace("youtube.com/embed/", "youtu.be/")

        return youtube_link 
    else: 
        print("Not valid entry.")

main() 

