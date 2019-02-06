import os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f: #讀入清單
		for line in f: # FOR LOOP是讀取檔案
			if '商品,價格' in line:
				continue # 沒有跳出迴圈 ，繼續，跳到下一回，就是看到商品,價格 直接不處理的意思 7 8行不處理 
			name, price = line.strip().split(',') #以,切割	split 切割完的東西是清單
			products.append([name, price])
	return products


#讓使用者輸入資訊
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		products.append([name, price])# 寫小清單裝到大清單，需用清單裝進去
	print(products)
	return products
# 印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0], '是', product[1], '元')
	# 存入檔案
def write_file(filename, products): #2個參數
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n') #讓EXCEL出現這個欄位，要注意編碼問題
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n')


def main():
	filename = 'products.cvs'
	if os.path.isfile(filename):
		print('YA found it')
		products = read_file(filename)
	else:
		print('找不到檔案')
	products = user_input(products)
	print_products(products)
	write_file('products.cvs', products)

main()