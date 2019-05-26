import unittest
from unittest import mock
from validation import validate as check_username
from validation import validate as check_email
from menu import menu


class TestLogin(unittest.TestCase):
    @mock.patch('menu.input', create=True)
    def test_user_log_in(self, mocked_input):
        mocked_input.side_effect = ['2', '123@123.com', 'asd#456']
        result = menu()
        self.assertTrue(result, "123@123.com")

    @mock.patch('menu.input', create=True)
    def test_user_log_in_faile(self, mocked_input):
        mocked_input.side_effect = ['2', '123@123.com', 'asd#466']
        result = menu()
        self.assertFalse(print("Incorrect password,please check!"))


class testMenu(unittest.TestCase):
    test = menu

    def menudisplay(self):
        self.assertTrue(print(30 * "-", "MENU", 30 * "-"))
        self.assertTrue(print(67 * "-"))


class TestValidation(unittest.TestCase):
    @mock.patch('validation.input', create=True)
    def test_check_username(self, mocked_input):
        mocked_input.side_effect = ['Albert72122']
        check_username()
        self.assertFalse(print("Invalid user name"))

    @mock.patch('validation.input', create=True)
    def test_check_email(self, mocked_input):
        mocked_input.side_effect = ['1234556']
        check_email()
        self.assertFalse(print("Invalid email,try again"))


if __name__ == "__main__":
    unittest.main()
