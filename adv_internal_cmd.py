from sbos_settings import say, output as spk
import sbos_settings
import os
import fnmatch #for file path matching
def power_up():
	spk("Powering up")

def power_down():
	return 0



		
def new_folder(cmd):
	i=0
	print cmd
	fname=""
	while(not cmd[i] == 'in' ):
		print "i=",i,"len=",len(cmd)
		fname+=' '+cmd[i]
		print fname
		if i+1 < len(cmd):
			i+=1
		else:
			break
	if 'in' in cmd:
		i=0
		while(not cmd[i] == 'in'):
			i+=1
		to_folder=' '.join(cmd[i+1:])
		path=sbos_settings.home_dir+to_folder+'/'+fname		#to create a folder inside another folder
	else:
		path=sbos_settings.home_dir+fname				# to create a folder inside the present folder
	file_exists=os.access(path,os.F_OK)
	#print "ex:",file_exists
	if not file_exists:
		os.makedirs(path)
		spk("Directory Files has been created")
	else:
		spk("File or folder by that name exists")
		


def get_cur_dir():
	print "The current working directory is:\n ",sbos_settings.current_dir
	spk("The current working directory is:\n "+sbos_settings.current_dir)

def get_home_dir():
	print "The current home directory is:\n ",sbos_settings.home_dir
	spk("The current home directory is:\n "+sbos_settings.home_dir)
		
		
def list_folder(cmd):
	if cmd=='':
		path=sbos_settings.home_dir
	else:
		path=sbos_settings.current_dir
	path+='/'.join(cmd)
	#print cmd
	print "listing files in",path
	dirs=os.listdir(path)
	for file in dirs:
		print file
		spk(file)
	

	
	
def sbos_recog(cmd):
	print "Its an advanced command"
	cmd_part = cmd.split(' ')
	if (cmd_part[0] == 'power'):
		if(cmd_part[1]== 'up'):
			power_up()
		elif(cmd_part[1]== 'down'):
			ret=power_down()
			if ret == 0:
				return 214
	elif (cmd_part[0] == 'create'): 
		if(cmd_part[1] == 'folder'):
			new_folder(cmd_part[2:])
	elif (cmd_part[0] =='list') and (cmd_part[1]=='folder'):
		list_folder(cmd_part[2:])
	elif ((cmd_part[0]=='say') and cmd_part[1]=='directory'):
		get_cur_dir()
	elif ((cmd_part[0]=='say') and  cmd_part[1] == 'home' and cmd_part[2]=='directory'):
		get_home_dir()
	else:
		return -302
