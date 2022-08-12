from playwright.sync_api import sync_playwright
import pytest
import logging


# my deatls
# michael101@gmail.com
# 12345


def test_buy_dress():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://automationpractice.com/index.php')

        # enter to my user
        login = page.wait_for_selector(".login")
        login.click()

        email_box = page.wait_for_selector("#email")
        password_box = page.wait_for_selector("#passwd")

        email_box.fill("michael101@gmail.com")
        password_box.fill("12345")

        submit = page.wait_for_selector("#SubmitLogin")
        submit.click()

        search_box = page.wait_for_selector("#search_query_top")
        search_box.fill("summer")
        search_btn = page.wait_for_selector(".button-search")
        search_btn.click()

        search_result_header = page.wait_for_selector("#center_column > h1 > span.lighter")
        print(f'the res is: {search_result_header.inner_text()}')
        logging.info(search_result_header.inner_text())
        assert 'SUMMER' in search_result_header.inner_text()

        # find the dress
        product_list = page.query_selector_all(".product-container")
        price_list = []
        for product in product_list:
            price = product.query_selector(".product-price").text_content().strip()
            price_list.append(float(price[1::]))

        print(price_list)
        minimum = str(min(price_list))
        print(minimum)

        dress = page.locator(f'test={str(minimum)}')
        dress.click()

        #price_list[cheapes]
        # print(price_list[cheapes].inner_html())
        # page.wait_for_timeout(3)
        # check_out_btn_1 = page.wait_for_selector('.button-medium')
        # check_out_btn_1.click()


        page.wait_for_timeout(10000)
        browser.close()


