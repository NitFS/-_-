with open('-.txt', 'r',encoding='utf-8') as file:
    text = file.read()

with open('test.txt','w',encoding='utf-8') as des_file:
    des_file.write(text)
   
