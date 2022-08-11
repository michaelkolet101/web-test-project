from playwright.sync_api import sync_playwright
import pytest
import logging

TEST_CASES = {"valid": ['michael101@gmail.com', '12345'],
              "not valid 1": ['DanidinTheKing@gmail.com', '12345'],
              "not valid 2": ['banana', '12345'],
              "not valid 3": ['michael101@gmail.com', '123456'],
              "not valid 4": ['michael101@gmail.com', '1234'],
              "not valid 5": ['', '']
              }


def login_to_acoount(page: 'page', uesr_info: list):
    """
    :param driver:
    :param uesr_info:
    :return: NAN
    """
    email = uesr_info[0]
    passwd = uesr_info[1]

    login = page.wait_for_selector(".login")
    login.click()

    email_box = page.wait_for_selector("#email")
    password_box = page.wait_for_selector("#passwd")

    email_box.fill(email)
    password_box.fill(passwd)

    submit = page.wait_for_selector("#SubmitLogin")
    submit.click()


class Test_login:

    def test_login_1(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('http://automationpractice.com/index.php')

            login_to_acoount(page, TEST_CASES['valid'])

            logging.info(TEST_CASES['valid'])
            text = page.wait_for_selector('.info-account')
            logging.info(text.inner_html())
            assert 'Welcome to your account' in text.inner_html()

            page.wait_for_timeout(5000)
            browser.close()

    def test_login_2(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('http://automationpractice.com/index.php')

            login_to_acoount(page, TEST_CASES['not valid 1'])
            logging.info(TEST_CASES['not valid 1'])
            res = page.wait_for_selector('.alert-danger')

            assert 'Authentication failed.' in res.inner_text()
            logging.info(res.inner_text())

            page.wait_for_timeout(5000)
            browser.close()

    def test_login_3(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('http://automationpractice.com/index.php')

            login_to_acoount(page, TEST_CASES['not valid 2'])
            logging.info(TEST_CASES['not valid 2'])

            res = page.wait_for_selector('.alert-danger')

            assert 'Invalid email address' in res.inner_text()
            logging.info(res.inner_text())

            page.wait_for_timeout(5000)
            browser.close()

    def test_login_4(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('http://automationpractice.com/index.php')

            login_to_acoount(page, TEST_CASES['not valid 3'])
            logging.info(TEST_CASES['not valid 3'])

            res = page.wait_for_selector('.alert-danger')

            assert 'Authentication failed.' in res.inner_text()
            logging.info(res.inner_text())

            page.wait_for_timeout(5000)
            browser.close()

    def test_login_5(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('http://automationpractice.com/index.php')

            login_to_acoount(page, TEST_CASES['not valid 4'])
            logging.info(TEST_CASES['not valid 4'])

            res = page.wait_for_selector('.alert-danger')

            assert 'Invalid password.' in res.inner_text()
            logging.info(res.inner_text())

            page.wait_for_timeout(5000)
            browser.close()




    # TODO
    def test_login_6(self):
        # test to forgot password

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('http://automationpractice.com/index.php')

            login_btn = page.wait_for_selector(".login")
            logging.info(login_btn.inner_text())
            login_btn.click()

            lost_password = page.locator('.lost_password')
            logging.info(lost_password.inner_text())
            lost_password.locator("a").click()
            logging.info("lost_password - clicked")

            page_subheading = page.wait_for_selector('.page-subheading')
            logging.info(page_subheading.inner_text())
            assert 'FORGOT YOUR PASSWORD?' in page_subheading.inner_text()
            email_box = page.wait_for_selector('#email')
            email_box.fill(TEST_CASES['valid'][0])

            button = page.locator("button", has_text="Retrieve Password").click()
            success = page.wait_for_selector('.alert-success')
            logging.info(success.inner_text())
            assert 'A confirmation email has been sent to your address:' in success.inner_text()
            assert TEST_CASES['valid'][0] in success.inner_text()

            page.wait_for_timeout(5000)
            browser.close()
