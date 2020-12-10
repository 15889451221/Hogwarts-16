

name = "lili"
age = 20
list1 = [1,2]
dict1 = {"name":"tom","gender":"male"}

# f=open("test.txt")
# print(f.readable())
# print(f.readlines())
# f.close()

with open("test.txt","rt") as i:
    while True:
        line = i.readline()
        if line:
            print(line)
        else:
            break