import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrom_driver_path ='/home/michael/seleln/chromedriver'

# my deatls
# michael101@gmail.com
# 12345
def login_to_acoount(driver):
    login_btn = driver.find_element(By.CLASS_NAME, "login")
    login_btn.click()
    time.sleep(1)

    email_box = driver.find_element(By.ID, "email")
    password_box = driver.find_element(By.ID, "passwd")

    email_box.send_keys("michael101@gmail.com")
    password_box.send_keys("12345")

    submit = driver.find_element(By.ID, "SubmitLogin")
    submit.click()



def find_the_min_price(driver):
    product_list = driver.find_element(By.CLASS_NAME, "product_list")
    product_containers = product_list.find_elements(By.CLASS_NAME, "product-container")
    list_price = []
    minimum_price = 0
    for product_container in product_containers:
        right_block = product_container.find_element(By.CLASS_NAME, "right-block")
        price = right_block.find_element(By.CLASS_NAME, "product-price").text
        list_price.append((price[1::]))
        minimum_price = min(list_price)
    return minimum_price


def buy_the_dress(driver, minimum_price):
    product_list = driver.find_element(By.CLASS_NAME, "product_list")
    product_containers = product_list.find_elements(By.CLASS_NAME, "product-container")
    for product_container in product_containers:
        right_block = product_container.find_element(By.CLASS_NAME, "right-block")
        price = right_block.find_element(By.CLASS_NAME, "product-price").text
        p = float(price[1::])
        logging.info(f"min - {minimum_price}")
        logging.info(f"price - {p}")
        if (p == float(minimum_price)):
            left_block = product_container.find_element(By.CLASS_NAME, 'left-block')
            logging.info(left_block)
            left_block.click()
            time.sleep(10)

            columns_container = driver.find_element(By.CLASS_NAME, 'columns-container')
            buy_block = columns_container.find_element(By.ID, 'buy_block')
            submit = buy_block.find_element(By.NAME, 'Submit')
            submit.click()
            time.sleep(10)

            layer_cart_cart = driver.find_element(By.CLASS_NAME, "layer_cart_cart")
            button_container = layer_cart_cart.find_element(By.CLASS_NAME, "button-container")
            btn = button_container.find_element(By.CLASS_NAME, "button-medium")
            btn.click()
            time.sleep(10)

            standard_checkout_1 = driver.find_element(By.CLASS_NAME, 'standard-checkout')
            logging.info('standard_checkout_1')
            standard_checkout_1.click()
            time.sleep(3)

            standard_checkout_2 = driver.find_element(By.NAME, 'processAddress')
            logging.info('standard_checkout_2')
            standard_checkout_2.click()
            time.sleep(3)

            chack_box = driver.find_element(By.NAME, 'cgv')
            logging.info('chack_box')
            chack_box.click()
            time.sleep(3)

            standard_checkout_3 = driver.find_element(By.NAME, 'processCarrier')
            logging.info('standard_checkout_3')
            standard_checkout_3.click()
            time.sleep(3)

            pay = driver.find_element(By.CLASS_NAME, 'payment_module')
            bankwire = pay.find_element(By.CLASS_NAME, 'bankwire')
            logging.info('bankwire')
            bankwire.click()
            time.sleep(3)

            cart_navigation = driver.find_element(By.ID, 'cart_navigation')
            logging.info('cart_navigation')
            confirm = cart_navigation.find_element(By.CLASS_NAME, 'button-medium')
            logging.info('confirm')
            confirm.click()
            time.sleep(3)

            end_msg = driver.find_element(By.CLASS_NAME, 'box')
            logging.info(end_msg.text)
            assert 'Your order on My Store is complete.' in end_msg.text
            break


def test_get_min_drees():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')

    login_to_acoount(driver)
    time.sleep(10)

    search_box = driver.find_element(By.ID, "search_query_top")
    search_box.send_keys("summer")
    search_btn = driver.find_element(By.NAME, "submit_search")
    search_btn.click()
    time.sleep(10)

    search_result_header = driver.find_element(By.CSS_SELECTOR, "#center_column>h1")
    logging.info(search_result_header.text)
    assert 'SEARCH  "SUMMER"' in search_result_header.text

    minimum_price = find_the_min_price(driver)
    logging.info(minimum_price)
    buy_the_dress(driver, minimum_price)




