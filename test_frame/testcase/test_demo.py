

# def b():
#     print("a1")
#     a()
#     print("a2")
import os
from time import time

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


def b(fun):
    def run(*args,**kwargs):
        print("a1")
        fun(*args,**kwargs)
        print("a2")
    return run

@b
def a():
    print('a')


def test():
    a()

def test_yaml():
    with open("./tmp.yaml","r",encoding="utf-8") as f :
        data = yaml.load(f)
        for a in data:
         xpath_expr = a.get("find")
         print(xpath_expr)




