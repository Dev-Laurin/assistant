import speech_recognition as SR 
import pygame 

pygame.init() 
pygame.mixer.music.load('Cheerful.mp3')
pygame.mixer.music.play()
pygame.mixer.music.play()

r = SR.Recognizer()
with SR.Microphone() as source: 
	print("Talk to me")
	audio = r.listen(source)
	while True: 
		try: 
			text = r.recognize_google(audio)
			print("You said: {}".format(text))
		except: 
			print("Sorry, I didn't get that.")