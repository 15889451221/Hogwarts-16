from pythoncode.calculator import Calculator
import pytest


class TestCalc():
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(100,200,300)],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect",[(10,5,5),(-20,30,-50),(-100,-100,0)])
    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expect",[(50,10,500),(30,0,0),(-10,3,-30)])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect",[(60,30,2),(7,0,7),(0,8,0)])
    def test_div(self,a,b,expect):
        if b!=0:
            assert expect == self.calc.div(a,b)
        else:
            print(f"division by zero除数不能为{b}")
