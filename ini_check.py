import urllib2
import os
def initialise():
 
	print("Verifying internet connectivity...")
	try:
		response=urllib2.urlopen('http://74.125.130.100', timeout=1)
		#print("response is:",response)
		print("Internet connectivity verified");
	except urllib2.URLError as err:
		print("\nError connecting.Please check your internet connection.");
	return False;


