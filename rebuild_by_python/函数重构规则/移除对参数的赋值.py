def disCount(inputval,quantity,yearToDate):

	result = inputval

	if inputval > 50:
		result -= 2

	if inputval > 1000:
		result -= 1

	if inputval > 5000:
		result -= 3
	
	return result


def main():
	res = disCount(100,2,3)
	print(res)

if __name__ == '__main__':
	main()
