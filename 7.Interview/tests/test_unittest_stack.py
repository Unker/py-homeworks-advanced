import unittest
import sys
sys.path.append('..')
import stack


class TestStack(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lst = list(range(10))

    def test_main_methods(self):
        self.stack = stack.Stack(TestStack.lst)
        # test size()
        ret = self.stack.size()
        self.assertEqual(ret, len(self.lst))
        # test is_empty()
        self.assertFalse(self.stack.is_empty())
        # test peek
        last_element = self.stack.peek()
        self.assertEqual(last_element, self.lst[-1])
        # test push
        old_sz = self.stack.size()
        new_element = self.lst[-1]+1
        self.stack.push(new_element)
        new_sz = self.stack.size()
        self.assertEqual(new_sz-old_sz, 1)
        # tset pop()
        popped_element = self.stack.pop()
        self.assertEqual(new_element, popped_element)
        sz_after_pop = self.stack.size()
        self.assertEqual(new_sz-sz_after_pop, 1)
        # test empty
        for i in range(self.stack.size() - 1):
            self.stack.pop()
        ret = self.stack.pop()
        self.assertIsNotNone(ret)
        self.assertRaises(ValueError, self.stack.pop)

    def test_dunder_methods(self):
        self.stack = stack.Stack(TestStack.lst)
        ret = self.stack.size()
        self.assertEqual(ret, len(self.stack))
