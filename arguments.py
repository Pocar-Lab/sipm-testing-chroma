#!/usr/bin/env python
import sys, getopt

def usage():
	print ("  The minimum paramaters the simulation needs are:")
	print ("  	(1) '-d <pmt/sipm>'	choosing the correct detector.") 
	print ("  	(2) '-n <#>'		number of photons to be simulated.")
	print ("  Additional options can be chosen:")
	print ("  	(3) '-v' or '-view'	to view the setup before simulation.")
	print ("  	(4) '-a' 		to analyze the simulated photons.")
	print ("     (5) '-s' <#> choose the seed number")
	print ("=====================================================================")

def todo():
	print ("  In order to check the manual type 'help'.")
	print ("  If you want to leave and try again just press enter.")
	try:
		mode=raw_input('  >>>  ')
		if(mode == "help"):
			usage()
		else:
			sys.exit()
	except ValueError:
		sys.exit()

def main(argv):
	#photon_nr = 10000
	photon_nr = 0
	detectChoice = "sipm" 
	arg_num = True   #For seeding, can delete this line if it does not work. This should allow the arg_list to take seed as argument #2 (starting from 0,1,2)
	Show = False
	seed = 0
	arg_det = True
	Plot = True
	Analysis = True

	try:
		opts, args = getopt.getopt(argv,"apvd:n:s:",["view","help","d=","n=", "s="])
	except getopt.GetoptError:
		print ("  You have passed the wrong/or not enough arguments.")
		usage()
		sys.exit()
	if not opts:
		print ("  You haven't passed any arguments to the simulation. How is this supposed to work?")
		usage()
		sys.exit()
	for opt, arg in opts:
		if opt == "-help ":
			usage()
			sys.exit()
		elif opt == "-n":
			try:
				photon_nr = int(arg)
				arg_nr = True
			except:
				print ("  You should take care of proper spacings betweens options and arguments.")
				usage()
				sys.exit()
		elif opt == "-d":
				detectChoice = arg
				arg_det = True
		elif opt == "-v":
			Show = True
		elif opt == "-a":
			Analysis = True
		elif opt == "-p":
			Plot = True
		elif opt == "-s":  #Seeding argument added here 
			try:
				seed=int(arg)
				arg_num = True
			except: 
				print ("Seed not specified")

	arg_list=(photon_nr, detectChoice, Show, Plot, Analysis, seed)
	if (arg_nr and arg_det):
		print ("  Number of photons: 				", arg_list[0])
		print ("  Detector used: 				", arg_list[1])
		if (arg_list[2]):
			print ("  View setup before simulation: 		enabled")
		else:
			print ("  View setup before simulation: 		disabled")
	
		if (arg_list[3]):
			print ("  View plots: 					enabled")
		else:
			print ("  View plots: 					disabled")
		if (arg_list[4]):
			print ("  Analyze simulation: 				enabled")
		else:
			print ("  Analyze simulation: 				disabled")
		if (arg_list[5]):
			print ("seed:  ", arg_list[5])
		else:
			print (" Seed=0 ")
	else:
		if(arg_nr):
			print ("  You haven't specified the detector to be used.")
			todo()
		else:
			print ("  You haven't specified the number of photons that should be simulated.")
			todo()
		sys.exit()
	return (arg_list)
