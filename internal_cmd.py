import subprocess,sys
import errno,os
from sbos_settings import say
from sbos_settings import output as spk
import sbos_settings
import fnmatch,glob

"""PROCESS EXECUTION AND RELATED STUFF GO HERE"""
def execute(cmd):
	try:
		spk("executing command ... ")
		#print "Cmd=",cmd
		#open('/dev/null','w')
		ret=subprocess.Popen(cmd, shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	except ValueError:
		spk("Please check your input")
	except OSError:
		spk("Please check if such a file, program, or command exists" )
	except IOError as ioex:
		spk("There is an IOerror"+os.strerror(ioex.errno) )
	except :
		
		spk("An unknown error as occurred")
	else:
		#print ret.communicate()
		std=ret.communicate()
		if(std[0]==''):
			op=' '.join(cmd)
			spk(op+" Has been executed")
		else:
			print std[0]
			spk(std[0])
		if not std[1] == '':
			spk("There are a few errors or warnings (Eg: Check if you need sudo permission to execute)")
			spk("Would you like to hear the exact errors?")
			ip=say("Choice:(yes/no)")
			if ip=='yes':
				spk("The errors are ...")
				print std[1]
				spk(std[1])			#std[1] has errors

def locate(cmd):
	path=sbos_settings.home_dir
	if 'in' in cmd:
		i=0
		while not cmd[i] == 'in':
			i+=1
		search_path=path+'/'.join(cmd[i+1:])
		search_term=' '.join(cmd[0:i])
	else:
		search_term=' '.join(cmd)
		search_path=path
	#print "srch_term=",search_term
	#print "srch_path=",search_path
	"""for file in os.listdir(search_path):
		print "s:",file
		if fnmatch.fnmatch(file,'*'+search_term+'*'):
			print file"""
	result=[y for x in os.walk(search_path) for y in glob.glob(os.path.join(x[0],search_term))]
	if result:
		spk("Found "+str(len(result))+" result")
		for x in result:
			print x
	else:
		spk("no files or folders found")
		

def change_cur_dir(cmd):
	path=sbos_settings.home_dir
	if(cmd ==''):
		path=sbos_settings.home_dir
	elif(cmd[0] == 'root'):
		path=sbos_settings.home_dir
	else:
		path+='/'.join(cmd[0:])
	file_exists=os.access(path,os.F_OK)
	#print "ex:",file_exists
	if not file_exists:
		spk("Such a folder does not exist. should I create a new folder?")
		ip=say('choice:(yes/no)')
		if ip=='yes':
			os.makedirs(path)
			spk("Directory Files has been created")
		elif ip=='no':
			spk('Cancelled changing the current directory')
		else:
			spk('Invalid input')
	else:
		sbos_settings.current_dir=path
		print sbos_settings.current_dir
		spk("We are now in "+sbos_settings.current_dir)	
		
		
		
def opn(cmd):
	cmd=' '.join(cmd)
	try:
		spk("opening "+cmd+" ...")
		ret=subprocess.Popen(cmd, shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	except ValueError:
		spk("Please check your input")
	except OSError:
		spk("Please check if such a file, program, or command exists" )
	except IOError as ioex:
		spk("There is an IOerror"+os.strerror(ioex.errno) )
	except :
		
		spk("An unknown error as occurred")
	else:
		spk(cmd+"Has been opened")

def exit(cmd):
	
	#print cmd
	process_not_exists = os.system('pidof '+ cmd)
	if(not process_not_exists):
		spk("exiting "+cmd)
		kill_status=os.system('kill $(pidof '+ cmd+')')
		if(not kill_status):
			spk(cmd+" closed")
		else:
			spk("Cannot exit "+cmd)
	else:
		spk( "There is no "+cmd+"running" )
		
	
"""FILE OPERATIONS GO HERE """

	

"""THE HEART OF THIS FILE, THE RECOG IS BELOW """	
def sbos_recog(cmd):
	"Here sbos commands are identified and passed to the appropriate function"
	cmd_part = cmd.split(' ')
	if (cmd_part[0] == 'execute'):
		execute(cmd_part[1:])
	elif (cmd_part[0] == 'exit' or cmd_part[0] == 'close'):
		exit(cmd_part[1])
	elif (cmd_part[0] == 'open'):
		opn(cmd_part[1:])
	elif (cmd_part[0]=='locate'):
		locate(cmd_part[1:])
	elif (cmd_part[0]=='goto'):
		change_cur_dir(cmd_part[1:])
	else:
		return -1
		

		
