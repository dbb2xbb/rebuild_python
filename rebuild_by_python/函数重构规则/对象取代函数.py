class I3(object):
	def __init__(self, orgval):
		self.i3 = 0
		self.orgval = orgval
	def geti3(self,i2):
		self.i3 = i2 * 8
		return self.i3

class I2(object):
	def __init__(self, orgval):
		self.i2 = 0
		self.orgval = orgval
	def geti2(self,i1):
		self.i2 = self.orgval.inputVal * self.orgval.yearToDate + 100
		if self.orgval.yearToDate - i1 > 100:
			self.i2 -= 2
		return self.i2

class I1(object):
	def __init__(self, orgval):
		self.i1 = 0
		self.orgval = orgval
	def geti1(self):
		self.i1 = self.orgval.inputVal * self.orgval.quantity + 10 
		return self.i1

class org_val(object):
	def __init__(self,inputVal,quantity,yearToDate):
		self.inputVal  = inputVal
		self.quantity  = quantity
		self.yearToDate	= yearToDate


def main():
	orgval = org_val(100,200,300)	
	i1 = I1(orgval).geti1()
	i2 = I2(orgval).geti2(i1)
	i3 = I3(orgval).geti3(i2)
	
	print(i3 - 2 * i1)

if __name__ == '__main__':
	main()


