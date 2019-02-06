import os
products = []
if os.path.isfile('products.cvs'):
	print('YA found it')
	with open('products.cvs', 'r', encoding='utf-8') as f: #讀入清單
		for line in f: # FOR LOOP是讀取檔案
			if '商品,價格' in line:
				continue # 沒有跳出迴圈 ，繼續，跳到下一回，就是看到商品,價格 直接不處理的意思 7 8行不處理 
			name, price = line.strip().split(',') #以,切割	split 切割完的東西是清單
			products.append([name, price])
	print(products)


else:
	print('找不到檔案')


#讀取檔案 


#讓使用者輸入資訊
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
                                     #寫小清單裝到大清單，需用清單裝進去
	products.append([name, price])
print(products)
# 印出所有購買紀錄
for product in products:
	print(product[0], '是', product[1], '元')
# 存入檔案
with open('products.cvs', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n') #讓EXCEL出現這個欄位，要注意編碼問題
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')
