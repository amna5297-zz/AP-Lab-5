#websites used for guidance:
#http://pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-2/
#https://simplejson.readthedocs.io/en/latest/

#Assignment 1
#Submitted by: Amna Abdul Rehman(3515)
#				BSCS_4C
#Platform: Windows has only C & D directory
#
#
#	In this I traversed through pat and saved the file word by splitting 
#	and saving it in another dictionary.
#
#	Github: https://github.com/amna5297/AP-Lab-5
#
##########################################
#File Sender



import os
import csv	
import json
import time
import socket
import datetime

def file_size_mb(filePath): 
	return float(os.path.getsize(filePath)) / (1024 * 1024)
	

def send_file(self, name):
  with open('./sampletest/' + name, 'rb') as handle:
    return handle.read()

		
path1 = r"C:\\"	
path2 = r"d:\\"

currentDirectorPath = r"C:\\Users\\Amna\\Desktop\\AP\\"

fileNameList = dict();

#logfile = 'fileLog.log'

current_time = datetime.datetime.now().time() 
current_time.isoformat()
#print(current_time)

slogs = 'slog.log'

localtime = time.localtime(time.time())

i = 1;


	#_______________________________________________________________________________________#
	############################     SEARCH DRIVE C 	####################################
	#_______________________________________________________________________________________#
	
	#	Crawls the whole file system starting from the root directory

for roots, dirs, files in os.walk(currentDirectorPath):
	for file in files:
		#print(file)
		filePath = os.path.join(roots, file)
		
		
		#fileNameList.setdefault(i,[].append(file))
		#print(i)          				#-----------> UNIT TEST
		#print(filePath)				#-----------> UNIT TEST
		#print(file)					#-----------> UNIT TEST
		#___________________________________________________________#
		############	SAVE CONTENT OF FILE    #####################
		#___________________________________________________________#
		
		rFile = open(filePath,'r')
		data = rFile.read();
		for word in data.split():			
			#word = word.decode('utf-8');
			if word in fileNameList:				
				fileNameList[word][len(fileNameList[word])] = filePath;
			else:
				fileNameList[word] = dict();
				fileNameList[word][len(fileNameList[word])] = filePath;
			
			
		
		rFile.close()
		#print(readFile)				#-----------> UNIT TEST
		i = i + 1
			
	

	
#_______________________________________________________________________________________#
###################       GET SEARCH WORD FROM USER         #############################
#_______________________________________________________________________________________#
	
print("**********************************\n")
searchFile = input('Enter Word:') 
print("\n**********************************\n")
	


#_______________________________________________________________________________________#
#######################     SEARCH WORD FROM Dictionary     #############################
#_______________________________________________________________________________________#

#for x in fileNameList:
#	print ("Key: "x,"  ",fileNameList[x],"\n\n")

#print(fileNameList)
if searchFile in fileNameList:
	#print("ASDf");
	print(fileNameList[searchFile]);    #---------> UNIT TEST
	

		





