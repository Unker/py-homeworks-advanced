import unittest
from parameterized import parameterized
import sys
sys.path.append('..')
from balanced import is_balanced


FIXTURE = [
    ('(((([{}]))))', True),
    ( '[([])((([[[]]])))]{()}', True),
    ( '{{[()]}}', True),
    ('}{}', False),
    ('{{[(])]}}', False),
    ('[[{())}]', False),
    ('{[([])((([[[]]])))]{()}]', False),
    ('}{', False),
    ('', False),
    ('aa', False),
    (None, False),
]

class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.lst = list(range(10))

    @parameterized.expand(FIXTURE)
    def test_is_balanced(self, elements, ans):
        res = is_balanced(elements)
        self.assertEqual(res, ans)
