import time
import logging
import pytest
from playwright.sync_api import sync_playwright

my_user = ["michael101@gmail.com", "12345"]
Test_log = logging.getLogger()


class Test_buy_dress:

    @pytest.fixture
    def open_page(self):
        """
        function will open the page of
        :return: None
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("http://automationpractice.com/index.php")
            yield page
            page.close()

    def login(self, open_page:sync_playwright)->None:
        """
        test login with right details to website
        :param open_page: sync_playwright: website driver page
        :return: None
        """
        page = open_page
        page.wait_for_timeout(3)
        page.click('.login')
        page.locator('id=email').fill(my_user[0])
        page.locator('id=passwd').fill(my_user[1])
        page.locator('id=SubmitLogin').click()
        Test_log.info(f"You have logged on to {page.title()}")
        assert page.title() == 'My account - My Store'


    def search_summer_dress(self, open_page:sync_playwright) -> None:
        """
        :param open_page:
        :return: NAN
        """
        search_box = open_page.wait_for_selector("#search_query_top")
        search_box.fill("summer")
        search_btn = open_page.wait_for_selector(".button-search")
        search_btn.click()
        # Takes time for the website to load all products
        time.sleep(2)

    def finding_relevant(self, open_page:sync_playwright) -> dict:
        """
        finding relevant products - and make a Dict[price:product]
        :param open_page:
        :return: dict of products
        """
        product_list = open_page.query_selector_all(".product-container")
        price_list = {}
        for product in product_list:
            price = product.query_selector(".product-price").text_content().strip()
            # Dict[price:product]
            price_list[price] = product

        return price_list

    def buying_process(self, open_page:sync_playwright) -> None:
        """
        Starting buying process
        :param open_page:
        :return: NAN
        """
        for i in range(5):
            Test_log.info(f"{open_page.title()}")
            time.sleep(2)
            if i == 2:
                open_page.locator('id=cgv').click()
            if i == 3:
                open_page.locator('text=Pay by bank wire').last.click()
                continue
            if i == 4:
                open_page.locator('.cart_navigation').click()
                open_page.locator('xpath=//*[@id="cart_navigation"]/button').click()
                continue
            open_page.locator('text=Proceed to checkout').last.click()


    def test_find_and_buy_cheap(self, open_page:sync_playwright)->None:
        """
        function log in the website and  find the cheapest product under summer search and complete Buying
        :param test_open: sync_playwright: website driver page
        :return: None
        """

        # log in with correct user and password
        self.login(open_page)

        # after log in going to search summer
        self.search_summer_dress(open_page)

        # finding relevant products - and make a Dict[price:product]
        price_list = self.finding_relevant(open_page)

        # finding cheap dress
        cheapes = min(price_list.keys())
        price_list[cheapes].click()

        # add to cart
        price_list[cheapes].query_selector('.ajax_add_to_cart_button').click()
        open_page.wait_for_timeout(2)
        open_page.locator("text=Proceed to checkout").click()

        # Starting buying process
        self.buying_process(open_page)

        # Finish buying process
        Test_log.info(f"{open_page.title()}")
        assert "Order confirmation - My Store" == open_page.title()
