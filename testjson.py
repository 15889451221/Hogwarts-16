"""
class person:
    name = "tom"
    age =20
    gender ="male"
    heith=120

    # def __init__(self):
    #     print("调用方法")

    def __init__(self,name,age,gender,heith):
        self.name=name
        self.age=age
        self.gender=gender
        self.heith=heith


    # def set_name(self,name):
    #     self.name=name
    # def set_age(self,age):
    #     self.age=age
    # def set_gender(self,gender):
    #     self.gender=gender

    @classmethod
    def eat(self):
        print(f"{self.name}:\t eating")

    def jump(self):
        print(f"{self.name}: \t jumping")

    def sleep(self):
        print("sleeping")


a = person("wangwu",20,"female",140)
a.eat()

b =person("zhaoliu",30,"male",150)
b.jump()

print(f"姓名是{a.name},年龄是{a.age},性别是{a.gender},体重是{a.heith}")
print(f"姓名是{b.name},年龄是{b.age},性别是{b.gender},体重是{b.heith}")

a = person().name="abc"
b=person("wangwu",20,"female",140)
print(b.name)
b.name="lilli"
person.eat()

import os
os.mkdir("tes")
print(os.listdir("./"))
os.removedirs("tes")
print(os.getcwd())

print(os.path.exists("tes"))
if not os.path.exists("tes"):
    os.mkdir("tes")

if not os.path.exists("tes/test1.txt"):
    f = open("tes/test1.txt","w")
    f.write("hello os usering")
    f.close()

import time

print(time.asctime())
print(time.time())
print(time.localtime())
print(time.strftime("%Y年-%m月-%d日 %H:%M:%S", time.localtime()))
获取2天前的时间
now_timestamp=time.time()
two_day_before=now_timestamp+60*60*24*3
print(time.strftime("%Y年-%m月-%d日 %H:%M:%S", time.localtime(two_day_before)))


import urllib.request
response : object = urllib.request.urlopen("http://www.baidu.com")
print(response.status)
# print(response.read())
print(response.headers)

"""
import math

print(math.sqrt(36))
print(math.ceil(23.1))
print(math.floor(24.9))
print(dir(math))
