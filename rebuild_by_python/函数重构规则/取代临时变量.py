class Product(object):
	def __init__(self,quantity,itemPrice):
		self.quantity = quantity
		self.itemPrice = itemPrice
	
	def getPrice(self):
		return self.getBasePrice() * self.getDiscountFactor()

	def getBasePrice(self):
		return self.quantity * self.itemPrice

	def getDiscountFactor(self): 
		disCountFactor = 1
		if self.getBasePrice() > 1000:
			disCountFactor = 0.95
		else:
			disCountFactor = 0.98

		return disCountFactor


def main():
	p = Product(100,5.6)
	print(p.getPrice())


if __name__ == '__main__':
	main()
