f = open("danex.txt","r",encoding="utf-8")

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()
print("_"*50)
# print(f.readline())

f = open("danex.txt","r",encoding="utf-8")
print(f.read())
f.close()
print("_"*50)
f = open("danex.txt","r",encoding="utf-8")
for i in f:
    print(i)

f.close()
