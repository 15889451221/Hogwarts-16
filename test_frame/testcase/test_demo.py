

# def b():
#     print("a1")
#     a()
#     print("a2")

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