import pytest
from pom.LoginPage import LoginPage


@pytest.mark.usefixtures('setup')
class TestLogin:

    def test_checking_if_fields_are_required_username(self):
        element = LoginPage(self.driver)
        element.username().send_keys('standard_user')
        element.button().click()
        result = element.error().text
        assert result == element.EXPECTED_ERROR_PASSWORD

    def test_checking_if_fields_are_required_password(self):
        element = LoginPage(self.driver)
        element.password().send_keys('secret_sauce')
        element.button().click()
        result = element.error().text
        assert result == element.EXPECTED_ERROR_USERNAME

    def test_successful_authorization(self):
        element = LoginPage(self.driver)
        element.username().send_keys('standard_user')
        element.password().send_keys('secret_sauce')
        element.button().click()
        result = element.element_site().text
        assert result == element.EXPECTED_201_OK

    def test_authorization_with_empty_fields(self):
        element = LoginPage(self.driver)
        element.button().click()
        result = element.error().text
        assert result == element.EXPECTED_ERROR_USERNAME

    def test_authorization_using_the_wrong_username(self):
        element = LoginPage(self.driver)
        element.username().send_keys('standard_user')
        element.password().send_keys('test')
        element.button().click()
        result = element.error().text
        assert result == element.EXPECTED_ERROR_USERNAME_PASSWORD

    def test_authorization_using_the_wrong_password(self):
        element = LoginPage(self.driver)
        element.username().send_keys('test')
        element.password().send_keys('standard_user')
        element.button().click()
        result = element.error().text
        assert result == element.EXPECTED_ERROR_USERNAME_PASSWORD

    def test_checking_case_change_when_filling_out_a_form_password(self):
        element = LoginPage(self.driver )
        element.username().send_keys('test')
        element.password().send_keys('secret_sauce')
        element.button().click()
        result = element.error().text
        assert result == element.EXPECTED_ERROR_USERNAME_PASSWORD

    def test_checking_case_change_when_filling_out_a_form_username(self):
        element = LoginPage(self.driver )
        element.username().send_keys('standard_user')
        element.password().send_keys('test')
        element.button().click()
        result = element.error().text
        assert result == element.EXPECTED_ERROR_USERNAME_PASSWORD
