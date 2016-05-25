import unittest
from common_prefix import common_prefix

class Test_common_prefix_test(unittest.TestCase):
    def test_it_works_with_usual_scenarios(self):
        self.assertEqual(common_prefix(['foobar','foomay','fooji']), 'foo')
        self.assertEqual(common_prefix(['foobar','fobmay','fooji']), 'fo')
        self.assertEqual(common_prefix(['foobar','faamay','fooji']), 'f')

    def test_it_works_with_empty_string_in_list(self):
        self.assertEqual(common_prefix(['','faamay','fooji']), '')

    def test_it_works_with_lists_that_contain_single_char(self):
        self.assertEqual(common_prefix(['f','faamay','fooji']), 'f')
        self.assertEqual(common_prefix(['f','f','f']), 'f')

    def test_it_works_with_every_other_weird_scenario(self):
        self.assertEqual(common_prefix(['fffffffff','faamay','fooji']), 'f')


if __name__ == '__main__':
    unittest.main()
