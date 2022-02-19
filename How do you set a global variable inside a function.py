globalvar=0
def set_globvar_to_one():
	global globvar #Need to modify global copy of globvar
	globvar=1
	def print_globvar():
		print(globvar) #No need for global declaration to read value of global
		set_globvar_to_one()
		print(_globvar())
        