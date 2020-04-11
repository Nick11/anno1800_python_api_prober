import subprocess, sys
import pickle

class Prober:
	
	def __init__(self):
		self.log("Init script")
		
	def log(self, text):
		with open('debug.log', 'a') as log_file:
			log_file.write(str(text)+'\n')
		
	def debug(self, obj):
		try:
			with open('debugger.py', 'r') as py_file:
				exec(py_file.read(), {'DATA': obj})
		except Exception as e:
			print('ERROR:' + str(e))
			with open('debug.log', 'a') as log_file:
				log_file.write(str(e)+'\n')

	def pressNine(self):
		self.debug(TextSources)
	
	def pressEight(self):
		self.debug(session)	
	
	def pressSeven(self):
		self.debug(scenes)
		#Values ?
			
prober = Prober();

