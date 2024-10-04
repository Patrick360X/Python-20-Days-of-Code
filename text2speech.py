import win32com.client
import random
speaker = win32com.client.Dispatch("SAPI.SpVoice")

l = ["Pradyumna", "Abhishek", "Arif", "Neha", "Rahul"]
speaker.Speak("Star Award Nominees are ")
for item in l:
    speaker.Speak(item)
    
winner = random.choice(l)
speaker.Speak("Congratulations " + winner + "you have won the award")
