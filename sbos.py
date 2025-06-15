#! /usr/bin/python

import speech_recognition as sr				#has the speech recognition module 1.1.4
import ini_check					#Does the initial health checks for the SBOS
from sbos_settings import say, output as spk					#Sets the required (global) variables and profiles
import internal_cmd					#Library of SBOS's internal commands		
import adv_internal_cmd
import intel	
import sys

sbos_cmd_dict_1 = set(['execute','exit','delete','open','close','play','copy','rename','move','delete','locate','goto'])
sbos_cmd_dict_2 =set(['make a note of','remind me','when i say','power down','power up','create folder','list folder','say directory'])			

"""
To create an internal sbos_cmd :- 
1. add the sbos_cmd here
2. create a function in intrnl_cmds.py file 
		(OR)
1. add the cmd 
2. create a separate file for your fn 
3. import it to intrnl_cmds.py

Note: Add one word commands to sbos_cmd_dict_1 and for more than one word add it to sbos_cmd_dict_2
"""

def main():
	"The good old main(), this is where it all begins ;) "
	if ( len(sys.argv)>1):
		print "System arguments execution has not been done yet... You got to wait!! Sorry :("
	else:
		start()
def whatis(cmd):
	i=0
	fnd=0
	cmd_part=cmd.split(' ')  
	cmd_new=cmd_part[0]             
	if cmd_part[0] in sbos_cmd_dict_1:				# for one word sbos_cmds followed by optional arguments			
		fnd=1
		return 1							
	while i<len(cmd_part):
		if cmd_new in sbos_cmd_dict_2:
			fnd=1
			return 2
		elif i+1<len(cmd_part):
			i=i+1
			cmd_new+=' '
			cmd_new+=cmd_part[i]
		else:
			break
	
	if fnd == 0 : return 3	
	
def start():
	while True:
		cmd=say("Command:")
		cmd_type=whatis(cmd)
		#print "Cmd_Type=",cmd_type			
		if cmd_type == 1:
			#print "type 1"
			ret=internal_cmd.sbos_recog(cmd)
		elif cmd_type == 2:
			#print "type 2"
			ret=adv_internal_cmd.sbos_recog(cmd)
		elif cmd_type == 3:
			#print "type 3"
			ret=intel.understand(cmd)
		if ret == 1 :				
			spk("I did not understand that")
		elif ret == 214:
			spk("Bye, I am powering down")
			break;
		elif ret == -1:
			spk("Something is wrong but i don't know what")
		elif ret ==-302:
			spk("Such a command does not exist")
		
		
		

if __name__=="__main__":
	main()
