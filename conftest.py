import pytest



@pytest.fixture(scope="module")
def myfixture():
    print("开始计算")
    yield
    print("结束计算")

'''
def pytest_collection_modifyitems(session,config,items):
    print(type(items))
    items.reverse()
    for item in items:
        item.name=item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')
        print("item.name="+item.name)
        print("item._nodeid="+item._nodeid)
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
'''
