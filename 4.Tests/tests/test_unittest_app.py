import unittest
from unittest.mock import patch
import sys
sys.path.append('../src')
import app
from app import documents, directories


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.new_doc_num = 'testDoc123'
        cls.new_doc_type = 'passport'
        cls.new_doc_owner_name = 'qwert asd'
        cls.new_doc_shelf_num = 'testShelf321'
        print("class setUp")

    @classmethod
    def tearDownClass(cls):
        print("class tearDown")

    def test_check_document_existance(self):
        ret = app.check_document_existance(documents[0]["number"])
        self.assertTrue(ret)
        self.assertFalse(app.check_document_existance('InvalidDocNumber'))

    # @patch('builtins.input', lambda *args: documents[0]["number"])
    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value=documents[0]["number"]):
            self.assertEqual(app.get_doc_owner_name(), documents[0]["name"])
        with unittest.mock.patch('builtins.input', return_value='InvalidDocNumber'):
            self.assertIsNone(app.get_doc_owner_name())

    def test_get_all_doc_owners_names(self):
        names = [doc["name"] for doc in documents]
        names = set(names)
        ret = app.get_all_doc_owners_names()
        self.assertIsNotNone(ret)
        self.assertSetEqual(ret, names)

    def _get_doc_shelf(self, num_doc):
        with unittest.mock.patch('builtins.input', return_value=num_doc):
            return app.get_doc_shelf()

    def test_get_doc_shelf(self):
        num_doc = documents[0]["number"]
        self.assertIsNotNone(self._get_doc_shelf(num_doc))
        self.assertIsNone(self._get_doc_shelf('InvalidDocNum'))

    def test_remove_doc_from_shelf(self):
        num_doc = documents[0]["number"]
        self.assertIsNotNone(self._get_doc_shelf(num_doc))
        ret = app.remove_doc_from_shelf(num_doc)
        self.assertTrue(ret)
        self.assertIsNone(self._get_doc_shelf(num_doc))
        # check not available doc
        bad_num_doc = 'InvalidDocNumber'
        self.assertIsNone(self._get_doc_shelf(bad_num_doc))
        ret = app.remove_doc_from_shelf(bad_num_doc)
        self.assertFalse(ret)

    def test_add_new_shelf(self):
        # default val -> input
        new_shelf = '1234567890'
        is_not_exist = new_shelf not in directories.keys()
        self.assertTrue(is_not_exist)
        with unittest.mock.patch('builtins.input', return_value=new_shelf):
            num_shelf, is_create = app.add_new_shelf()
            self.assertTrue(is_create)
        is_exist = new_shelf in directories.keys()
        self.assertTrue(is_exist)

        # new number
        new_shelf_2 = '987654321'
        is_not_exist = new_shelf_2 not in directories.keys()
        self.assertTrue(is_not_exist)
        num_shelf, is_create = app.add_new_shelf(new_shelf_2)
        self.assertTrue(is_create)
        is_exist = new_shelf_2 in directories.keys()
        self.assertTrue(is_exist)

        # already exist shelf number
        num_shelf, is_create = app.add_new_shelf(new_shelf_2)
        self.assertFalse(is_create)

        # not number
        num_shelf, is_create = app.add_new_shelf('num123')
        self.assertTrue(is_create)

    def test_append_doc_to_shelf(self):
        doc_num = 'testDocDouble'
        shelf_num = 'testShelf321'
        success = app.append_doc_to_shelf(doc_num, shelf_num)
        self.assertTrue(success)
        is_doc_exist = doc_num in directories[shelf_num]
        self.assertTrue(is_doc_exist)
        # duplicate doc to shelf
        success = app.append_doc_to_shelf(doc_num, shelf_num)
        self.assertFalse(success)

    def test_delete_doc(self):
        doc_num = documents[0]["number"]
        with unittest.mock.patch('builtins.input', return_value=doc_num):
            doc_num_ret, is_del = app.delete_doc()
            self.assertTrue(is_del)

        with unittest.mock.patch('builtins.input', return_value='InvalidDocNum'):
            ret = app.delete_doc()
            self.assertIsNone(ret)

    @patch('builtins.input')
    def test_add_new_doc(self, m_input):
        m_input.side_effect = [self.new_doc_num, self.new_doc_type,
                               self.new_doc_owner_name, self.new_doc_shelf_num]
        ret_shelf_number = app.add_new_doc()
        self.assertEqual(self.new_doc_shelf_num, ret_shelf_number)

    @patch('builtins.input')
    def test_move_doc_to_shelf(self, m_input):
        new_shelf_num = 'testNewShelf'
        m_input.side_effect = [self.new_doc_num, new_shelf_num]
        app.move_doc_to_shelf()
        with unittest.mock.patch('builtins.input', return_value=self.new_doc_num):
            shelf = app.get_doc_shelf()
        self.assertEqual(new_shelf_num, shelf)

        shelf_num = 'testShelf321'

if __name__ == '__main__':
    unittest.main()
