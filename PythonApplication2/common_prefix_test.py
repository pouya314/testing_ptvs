import unittest
from common_prefix import find_common_prefix_between

class Test_common_prefix_test(unittest.TestCase):
    def test_it_works_with_usual_scenarios(self):
        self.assertEqual(find_common_prefix_between(['foobar','foomay','fooji']), 'foo')
        self.assertEqual(find_common_prefix_between(['foobar','fobmay','fooji']), 'fo')
        self.assertEqual(find_common_prefix_between(['foobar','faamay','fooji']), 'f')

    def test_it_works_with_empty_string_in_list(self):
        self.assertEqual(find_common_prefix_between(['','faamay','fooji']), '')

    def test_it_works_with_lists_that_contain_single_char(self):
        self.assertEqual(find_common_prefix_between(['f','faamay','fooji']), 'f')
        self.assertEqual(find_common_prefix_between(['f','f','f']), 'f')

    def test_it_works_with_every_other_weird_scenario(self):
        self.assertEqual(find_common_prefix_between(['fffffffff','faamay','fooji']), 'f')


if __name__ == '__main__':
    unittest.main()
