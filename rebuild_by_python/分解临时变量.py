# 解释一下，这里的重构的内容主要是针对于，当一个变量不足以同时解释多个值，
# 即值与值的关联性不大时，要分别定义变量，以达到各司其职的作用。
def splitTempOver():
	aaa = 'AAA'
	print(aaa)
	bbb = 'BBB'
	print(bbb)

def main():
	splitTempOver()	

if __name__ == '__main__':
	main()
