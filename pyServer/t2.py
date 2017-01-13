

try:
	raise Exception('asd')
except Exception as e:
	 print( type(e).__name__ )	 
else:
	pass
finally:
	pass