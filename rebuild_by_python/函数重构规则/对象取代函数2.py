class disCount(object):
	def __init__(self, inputVal, quantity, yearToDate):
		self.inputVal  = inputVal
		self.quantity  = quantity
		self.yearToDate = yearToDate

	def geti1(self):
		return self.inputVal * self.quantity + 10
	
	def geti2(self):
		res = self.inputVal * self.yearToDate + 100
		if self.yearToDate - self.geti1() > 100:
			res -= 2
		return res		

	def geti3(self):
		return self.geti2() * 8 

	def getResult(self):
		return self.geti3() - 2 * self.geti1()

def main():
	dc = disCount(100,200,300)
	result = dc.getResult()
	print(result)
	
if __name__ == '__main__':
	main()


