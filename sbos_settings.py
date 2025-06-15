import os

# Global values 
global current_dir
current_dir = 'Home_Docs/'
global Home_dir 
home_dir= 'Home_Docs/'


def say(something=""):
	tmp=raw_input(something)
	return tmp

def output(text):
	"outputs  the recieved msg as voice"
	os.system('espeak " '+text+' "')
	
