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

# TODO
        # find the dress


        # product_containers = product_list.wait_for_selector(".product-container")
        # logging.info(product_containers.inner_html())
        # print(product_containers.inner_html())
        # list_price = []
        minimum_price = 0

        # for product_container in product_containers:
        #     right_block = product_container.wait_for_selector(".right-block")
        #     price = right_block.wait_for_selector(".product-price").text
        #     list_price.append((price[1::]))
        # minimum_price = min(list_price)
        # logging.info(minimum_price)

        page.wait_for_timeout(10000)
        browser.close()


