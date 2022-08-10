import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrom_driver_path = '/home/michael/seleln/chromedriver'
TEST_CASES = {"valid": ['michael101@gmail.com', '12345'],
              "not valid 1": ['DanidinTheKing@gmail.com', '12345'],
              "not valid 2": ['banana', '12345'],
              "not valid 3": ['michael101@gmail.com', '123456'],
              "not valid 4": ['michael101@gmail.com', '1234'],
              "not valid 5": ['', '']
              }


def set_driver():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    return driver


def login_to_acoount(driver, uesr_info: list):
    """
    :param driver:
    :param uesr_info:
    :return: NAN
    """
    email = uesr_info[0]
    passwd = uesr_info[1]

    login_btn = driver.find_element(By.CLASS_NAME, "login")
    login_btn.click()
    time.sleep(2)

    email_box = driver.find_element(By.ID, "email")
    password_box = driver.find_element(By.ID, "passwd")

    email_box.send_keys(email)
    password_box.send_keys(passwd)

    submit = driver.find_element(By.ID, "SubmitLogin")
    submit.click()


def test_login_1():
    driver = set_driver()

    login_to_acoount(driver, TEST_CASES['valid'])
    time.sleep(5)
    logging.info(TEST_CASES['valid'])
    text = driver.find_element(By.CLASS_NAME, 'info-account')
    assert 'Welcome to your account' in text.text
    time.sleep(2)
    driver.quit()


def test_login_2():
    flag = False
    while flag == False:
        try:
            driver = set_driver()
            time.sleep(2)
            login_to_acoount(driver, TEST_CASES['not valid 1'])
            logging.info(TEST_CASES['not valid 1'])
            time.sleep(5)
            res = driver.find_element(By.CLASS_NAME, 'alert-danger')
            flag = True
            logging.info(flag)
        except:
            driver.refresh()

    assert 'Authentication failed.' in res.text
    logging.info(res.text)
    time.sleep(2)
    driver.quit()


def test_login_3():
    flag = False
    while flag == False:
        try:
            driver = set_driver()
            time.sleep(2)
            login_to_acoount(driver, TEST_CASES['not valid 2'])
            logging.info(TEST_CASES['not valid 2'])
            time.sleep(5)
            res = driver.find_element(By.CLASS_NAME, 'alert-danger')
            flag = True
            logging.info(flag)
        except:
            driver.refresh()

    assert 'Invalid email address' in res.text
    logging.info(res.text)
    time.sleep(2)
    driver.quit()


def test_login_4():
    flag = False
    while flag == False:
        try:
            driver = set_driver()
            time.sleep(2)
            login_to_acoount(driver, TEST_CASES['not valid 3'])
            logging.info(TEST_CASES['not valid 3'])
            time.sleep(5)
            res = driver.find_element(By.CLASS_NAME, 'alert-danger')
            flag = True
            logging.info(flag)
        except:
            driver.refresh()

    assert 'Authentication failed.' in res.text
    logging.info(res.text)
    time.sleep(2)
    driver.quit()


def test_login_5():
    flag = False
    while flag == False:
        try:
            driver = set_driver()
            time.sleep(2)
            login_to_acoount(driver, TEST_CASES['not valid 4'])
            logging.info(TEST_CASES['not valid 4'])
            time.sleep(5)
            res = driver.find_element(By.CLASS_NAME, 'alert-danger')
            flag = True
            logging.info(flag)
        except:
            driver.refresh()

    assert 'Invalid password.' in res.text
    logging.info(res.text)
    time.sleep(2)
    driver.quit()


def test_login_5():
    flag = False
    while flag == False:
        try:
            driver = set_driver()
            time.sleep(2)
            login_to_acoount(driver, TEST_CASES['not valid 4'])
            logging.info(TEST_CASES['not valid 4'])
            time.sleep(5)
            res = driver.find_element(By.CLASS_NAME, 'alert-danger')
            flag = True
            logging.info(flag)
        except:
            driver.refresh()

    assert 'Invalid password.' in res.text
    logging.info(res.text)
    time.sleep(2)
    driver.quit()
# lost_password


# TODO
def test_login_6():
    # test to forgot password

    driver = set_driver()
    time.sleep(2)

    login_btn = driver.find_element(By.CLASS_NAME, "login")
    logging.info(login_btn.text)
    login_btn.click()
    time.sleep(2)


    lost_password = driver.find_element(By.CLASS_NAME, 'lost_password')
    lost_password.click()
    logging.info("lost_password - clicked")
    logging.info(lost_password.text)

    time.sleep(1)

    page_subheading = driver.find_element(By.CLASS_NAME, 'center_column')
    logging.info(page_subheading.text)
    assert 'FORGOT YOUR PASSWORD?' in page_subheading.text
    email_box = driver.find_element(By.ID, 'email')
    email_box.send_keys(TEST_CASES['valid'][0])

    button = driver.find_element(By.CLASS_NAME, 'button-medium')
    logging.info(button.text)
    button.click()
    time.sleep(2)

    success = driver.find_element(By.CLASS_NAME, 'alert alert-success')
    logging.info(success.text)
    assert 'A confirmation email has been sent to your address:' in success.text
    assert TEST_CASES['valid'][0] in success.text
    driver.quit()
