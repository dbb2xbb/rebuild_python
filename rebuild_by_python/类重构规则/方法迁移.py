books = [
	[0,'《悟空传》'],
	[1,'《安娜·卡列尼娜》'],
	[2,'《小王子》'],
]


class Book(object):
	NEW_BOOK = 0
	OLD_BOOK = 1
	CHILDREN_BOOK = 2

	def __init__(self,bookCode,bookName):
		self.bookCode = bookCode
		self.bookName = bookName
	
	def charge(self):
		result = 0
		if self.bookCode == self.NEW_BOOK:
			result += 10 	
		if self.bookCode == self.OLD_BOOK:
			result += 5 	
		if self.bookCode == self.CHILDREN_BOOK:
			result += 3 	
		
		return result
		

class BookCostumer(object):
	def __init__(self,name,isVip,books):
		self.name = name
		self.isVip = isVip
		self.books = books
		self.booklist = []
	
	def chargeBooks(self):
		for book in self.books:
			result = book.charge()
			if self.isVip == True:
				result *= 0.7
			else:
				result *= 0.9
			
			self.booklist.append([book.bookName,result])

		return self
	
	def __str__(self):
		s = ''
		s += '用户名：{}\n'.format(self.name)
		s += 'VIP:'
		s += '是\n' if self.isVip else '否\n'

		for book_res in self.booklist:
			s += '书名:{},价格:{}\n'.format(book_res[0],book_res[1])

		return s

def main():
	booklist = []
	for book in books:
		booklist.append(Book(book[0],book[1]))
	
	
	print(BookCostumer('dbb2xbb',False,booklist).chargeBooks())
	

if __name__ == '__main__':
	main()
