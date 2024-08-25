# install a new module and run it
# text to speak mudule (pyttsx3)
import pyttsx3
engine = pyttsx3.init()
engine.say("I can speak this text")
engine.say('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')

engine.say('''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't put Humpty together again
Humpty Dumpty sat on the ground
Humpty Dumpty looked all around
Gone were the chimneys, gone were the roofs
All he could see were ankles and hooves
Poor old Humpty
Poor old Humpty
Poor old Humpty
Dumpty
''')
engine.runAndWait()