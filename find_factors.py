def factors(b):
	if b % i == 0:
		print(i)
		
if __name__ == '__main__':
	
	b = input('Your number please')
	b = float(b)
	
	if b > 0 and b.is_integer():
		factors (inb(b))
		else:
			print ('Please enter a posititve integer')
