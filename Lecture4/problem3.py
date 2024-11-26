


import pygame 

def main(): 
    file_name = "example.mp3"
    play_audio(file_name) 


def play_audio(audio_file): 
    pygame.init() 
    pygame.mixer.music.load(audio_file) 
    pygame.mixer.music.play() 
    while pygame.mixer.music.get_busy():
        pass 

    pygame.quit()  

main() 











main()

