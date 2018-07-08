# 引入解释性变量，用于替代句子中超长表达式的情况.

class Product(object):
	def __init__(self,quantity,itemPrice):
		self.quantity = quantity
		self.itemPrice = itemPrice
	
	def getBasePrice(self):
		return self.quantity * self.itemPrice
	
	def getQuantityDiscount(self):
		return max(0, self.quantity - 500) * self.itemPrice *0.05

	def getShipping(self):
		return min(self.getBasePrice() * 0.1, 100)

	def getPrice(self):
		return self.getBasePrice()-self.getQuantityDiscount()+self.getShipping() 


def main():
	p = Product(600,5.6)
	print(p.getPrice())


if __name__ == '__main__':
	main()
