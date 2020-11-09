import pyttsx3
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
speak("hi i  am   you personal ai please your name my lord ")
print("hi i  am   you personal ai please your name my lord ")
a=input()
speak(f"sir your name is{a},i am gona take a game ")
print("no of odd triles u want to play ")
speak("no of odd triles u want to play ")
c=int(input())
x=int(0)
for c in range(0,int(c)):
	speak("what do you want snake, gun or water")
	print("what do you want snake, gun or water")
	b=input()
	d=random.choice(["snake","water","gun"])
	print(f"i choose {d}")
	speak(f"i choose {d}")
	if d==b:
		print("no one won this time ")
		speak("no one won this time ")
		speak(f"sir you won the game {x} out of {c} trils")
		print(f"sir you won the game {x}  out of{c} trils")
	elif d==("snake ")and b==("gun"):
		print("sir I lose you won ")
		speak("sir I lose you won ")
		speak(f"sir you won the game {x+1}  out of {c} trils")
		print(f"sir you won the game  {x+1}  out of {c}trils") 
	    
	elif d==("water") and b==("snake"):
		print("sir I lose you won ")
		speak("sir I lose you won ")
		speak(f"sir you won the game {x+1}  out of {c} trils")
		print(f"sir you won the game {x+1}  out of {c} trils")
	   
	elif d==("gun") and b==("water"):
		print("sir I lose you won ")
		speak("sir I lose you won ")
		speak(f"sir you won the game {x+1}  out of{c}trils")
		print(f"sir you won the game {x+1}  out of{c} trils") 
	    
	else:
		print("I won sir ")
		speak("I won sir ")
		speak(f"sir you won {x} the game out of {c}trils")
		print(f"sir you won {x}the game out of {c}trils")
