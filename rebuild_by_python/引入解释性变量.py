# 引入解释性变量，用于替代句子中超长表达式的情况.

class Product(object):
	def __init__(self,quantity,itemPrice):
		self.quantity = quantity
		self.itemPrice = itemPrice
	
	def getPrice(self):
		basePrice = self.quantity * self.itemPrice
		quantityDiscount = max(0, self.quantity - 500) * self.itemPrice *0.05
		shipping = min(basePrice * 0.1, 100)
		return basePrice + quantityDiscount + shipping



def main():
	p = Product(100,5.6)
	print(p.getPrice())


if __name__ == '__main__':
	main()
