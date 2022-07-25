import unittest
from parameterized import parameterized
import sys

sys.path.append('..')
from balanced import is_balanced

FIXTURE = [
    ('(((([{}]))))', True),
    ('[([])((([[[]]])))]{()}', True),
    ('{{[()]}}', True),
    ('}{}', False),
    ('{{[(])]}}', False),
    ('[[{())}]', False),
    ('{[([])((([[[]]])))]{()}]', False),
    ('}{', False),
    ('', False),
    ('aa', False),
    (None, False),
    ('aa()', False),
    ('{{}}', True),
    ('[]', True),
    ('[}', False),
]


class TestStack(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_is_balanced(self, elements, ans):
        res = is_balanced(elements)
        self.assertEqual(res, ans)
