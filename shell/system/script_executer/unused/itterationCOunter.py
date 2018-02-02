i = 0
def iPlus():
	global i
	i += 1
	try:
		iPlus()
	except:
		print i

iPlus()