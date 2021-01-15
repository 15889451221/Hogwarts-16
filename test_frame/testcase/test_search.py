from test_frame.base_page import BasePage
from test_frame.page.main import Main


class TestSearch:
    def setup(self):
        self.basepage = BasePage()
        self.app = Main(self.basepage)

    def test_search(self):
        self.app.goto_market().goto_search().search()