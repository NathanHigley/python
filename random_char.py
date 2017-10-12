from random import randint
def randlist(r):
	alpha = ["a","b","c","d","e"]
	c = alpha[r]
	return c
	
def main():
	while True:
		r = randint(0,4)
		c = randlist(r)
		print (c,end="")
main()
