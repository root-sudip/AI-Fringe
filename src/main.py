import os 
import sys
#strating project
if __name__ == '__main__':
	try:
		path =  input('Enter path name : ')
		for name in os.walk(path):
			print(name)
	except KeyboardInterrupt:
		print(' \n Interrupted \n')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

