products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')

	#寫小清單裝到大清單
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '是', product[1], '元')
with open('products.cvs', 'w') as f:
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')
