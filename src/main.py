import os 
import sys
import time
#strating project
if __name__ == '__main__':
	try:
		# level = []
		# paths = []
		# com = [level,path]
		# i = 0

		path =  input('Enter path name : ')
		rootDir = '.'
		for dirName, subdirList, fileList in os.walk(path):
			print('Found directory: %s' % dirName)
			for fname in fileList:
				print('\t%s' % fname)
	except KeyboardInterrupt:
		print(' \n Interrupted \n')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

