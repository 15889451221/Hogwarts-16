from test_Appium.po.page.app import App
from test_Appium.po.page.main_page import MainPage


class TestAddMemer():
    def test_add_member(self):
        app = App()
        app.start()
        result = app.goto_main().goto_address().click_AddMember().add_member_menual().add_contact()
        assert result