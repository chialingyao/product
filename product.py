products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')

	#寫小清單裝到大清單
	products.append([name, price])
print(products)

