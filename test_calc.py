import allure
import yaml

from pythoncode.calculator import Calculator
import pytest

class TestCalc():
    def get_data(param):
        with open("./data.yaml") as f:
            datas=yaml.safe_load(f)
            return datas[param]

    def setup_method(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a,b,expect",get_data("add_param"),
                             ids=get_data("add_ids"))
    @pytest.mark.add
    @pytest.mark.run(order=4)
    @allure.title("加法")
    @allure.story("Add Feature Testcase ")
    def test_add(self,a,b,expect,myfixture):
        # assert expect == self.calc.add(a, b)
        pytest.assume(expect == self.calc.add(a, b))

    @pytest.mark.parametrize("a,b,expect",get_data("sub_param"),
                             ids=get_data("sub_ids"))
    @pytest.mark.sub
    @pytest.mark.run(order=3)
    @allure.title("减法")
    @allure.story("Sub Feature Testcase ")
    def test_sub(self,a,b,expect):
        # assert expect == self.calc.sub(a,b)
        pytest.assume(expect == self.calc.sub(a,b))

    @pytest.mark.parametrize("a,b,expect",get_data("mul_param"),
                             ids=get_data("mul_ids"))
    @pytest.mark.mul
    @pytest.mark.run(order=2)
    @allure.title("乘法")
    @allure.story("Mul Feature Testcase ")
    def test_mul(self,a,b,expect):
        # assert expect == self.calc.mul(a,b)
        pytest.assume(expect == self.calc.mul(a,b))

    @pytest.mark.parametrize("a,b,expect",get_data("div_param"),
                             ids=get_data("div_ids"))
    @pytest.mark.div
    @pytest.mark.run(order=1)
    @allure.title("除法")
    @allure.story("Div Feature Testcase ")
    def test_div(self,a,b,expect):
        if b!=0:
            # assert expect == self.calc.div(a,b)
            pytest.assume(expect == self.calc.div(a,b))
        else:
            print(f"division by zero除数不能为{b}")


# 测试
