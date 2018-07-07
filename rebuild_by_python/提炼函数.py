class MyCostomer{

	def __init__(self,name,orders):
		self.name=name
		self.orders=orders
	
	def printBanner(self):
		print("***********************************************")
		print("*********       Custome Owes       ************")
		print("***********************************************")
	
	def getOutstanding(self):
		res = 0
		for order in self.orders:
			res += order
		return res
	
	def printDetail(self):
		print(name:self.name)
		print(amount:self.getOutstanding())

	def printOwing(self):
		printBanner()
		printDetail()

}

