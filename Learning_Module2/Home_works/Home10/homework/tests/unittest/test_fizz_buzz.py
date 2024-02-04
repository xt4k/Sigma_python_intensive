'''
Testsets for fizz_buzz: pure_division() and analysis()
'''

import unittest
import Learning_Module1.Home_works.Home2.fizz_buzz
import sys
import logging


def external_logger_function_example():

    LOG_FILE_NAME = "my_pytest.log"

    # DEFAULT_LOG_LEVEL = logging.INFO      # Демонстрацція рівня повідомлень

    DEFAULT_LOG_LEVEL = logging.DEBUG       # Демонстрацція рівня повідомлень

    DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s | %(filename)-15s: %(lineno)-4d | %(message)s"
    logging.basicConfig(filename=LOG_FILE_NAME, level=DEFAULT_LOG_LEVEL, filemode='w', format=DEFAULT_LOG_FORMAT)

    logger = logging.getLogger()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(DEFAULT_LOG_LEVEL)
    console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))

    logger.addHandler(console_handler)

    return logger



logger = external_logger_function_example()


fizz = "Fizz"
buzz = "Buzz"
logger.debug("begin logging ")

class FizzBuzzTests(unittest.TestCase):
    '''
    Testset for pure_division()
    testcases:
    1) 12 divided to 3 without left -> true
    2) 12 divided to 5 without left -> false
    3) 1 divide to 0 return ZeroDivisionException
    4) 0 divide to 0 return ZeroDivisionException
    5) 0 divide to 5 -> true
    6) '1' divide to 2 return TypeError
    7) 1 divide to '2' return TypeError
    8) 1 divide to None return TypeError
    9)  None divide to 1 return TypeError
    '''



    def test_divided_true(self):
        '''
        testcase_1: 12 divided to 3 without left -> true
        '''
        result = Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(12, 3)
        logger.debug("logged result is ", result)
        self.assertTrue(result, "Should return `True` but: " + str(result))

    def test_divided_false(self):
        '''
        testcase_2: 12 divided to 5 without left -> false
        '''
        logger.debug("begin logging ")
        result = Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(12, 5)
        self.assertFalse(result, "Should return `False` but: "  + str(result))

    def test_divided_zero_exception(self):
        '''
        testcase_3: 1 divide to 0 return ZeroDivisionException
        '''
        with self.assertRaises(ZeroDivisionError):
            Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(1, 0)

    def test_zero_divided_zero_exception(self):
        '''
        testcase_4: 0 divide to 0 return ZeroDivisionException
        '''
        with self.assertRaises(ZeroDivisionError):
            Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(0, 0)

    def test_zero_divided_true(self):
        '''
        testcase_5: 0 divide to 5 -> true
        '''
        result = Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(0, 5)
        self.assertTrue(result, "Should return `True` but: " + str(result))

    def test_wrong_input_exception(self):
        '''
        testcase_6: "1" divide to 2 return TypeError
        '''
        with self.assertRaises(TypeError):
            Learning_Module1.Home_works.Home2.fizz_buzz.pure_division("1", 2)

    def test_wrong_base_exception(self):
        '''
        testcase_7: 1 divide to '2' return TypeError
        '''
        with self.assertRaises(TypeError):
            Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(1, "2")

    def test_element_none_exception(self):
        '''
        testcase_8: 1 divide to None return TypeError
        '''
        with self.assertRaises(TypeError):
            Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(1, None)


    def test_base_none_input_exception(self):
        '''
        testcase_9:  None divide to 1 return TypeError
        '''
        with self.assertRaises(TypeError):
            Learning_Module1.Home_works.Home2.fizz_buzz.pure_division(None, 1)

    '''
    Testset for pytest.analysis()
    '''

    def test_fizzbuzz(self):
        '''
        testcase_1: 15 divided to 3 and 5 without left -> "FizzBuzz"
        '''
        result = Learning_Module1.Home_works.Home2.fizz_buzz.analysis(15)
        self.assertEqual(result, fizz + buzz, "Result should be `FizzBuzz` but: " + result)

    def test_fizz(self):
        '''
        testcase_2: 12 divided to 3 without left but divided to 5 with left -> "Fizz"
        '''
        result = Learning_Module1.Home_works.Home2.fizz_buzz.analysis(12)
        message = "Result should be `", fizz, "` but: ", result
        self.assertEqual(result, fizz, message)

    def test_buzz(self):
        '''
        testcase_3: 10 divided to 5 without left but divided to 3 with left -> "Buzz"
        '''
        result = Learning_Module1.Home_works.Home2.fizz_buzz.analysis(10)
        message = "Result should be `"+ buzz+ "` but: "+ result
        self.assertEqual(result, buzz, message)

    def test_element(self):
        '''
        testcase_4: 7 -> 7
        '''
        seven = 7
        result = Learning_Module1.Home_works.Home2.fizz_buzz.analysis(seven)
        message = "Result should be `", seven, "` but: ", result
        self.assertEqual(result, seven, message)

    def test_zero(self):
        '''
        testcase_5: 0 -> "FizzBuzz"
        '''
        result = Learning_Module1.Home_works.Home2.fizz_buzz.analysis(0)
        message = "Result should be `", fizz + buzz, "` but: ", result
        self.assertEqual(result, fizz + buzz, message)

    def test_type_error(self):
        '''
        testcase_6: 'q' -> TypeError
        '''
        with self.assertRaises(TypeError):
            Learning_Module1.Home_works.Home2.fizz_buzz.analysis("q")

    def test_none(self):
        '''
        testcase_7: None -> TypeError
        '''
        with self.assertRaises(TypeError):
            Learning_Module1.Home_works.Home2.fizz_buzz.analysis(None)


if __name__ == '__main__':
    unittest.main()
    logger.info("begin logging 3 ")