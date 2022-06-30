f=open('example.txt','a')
content=f.write('  appending text to the previous')
print(content)

f=open('example.txt','r')
content=f.read()
print(content)
f.close()


f1=open('text.txt','r')
store=f1.read()
print(store)
