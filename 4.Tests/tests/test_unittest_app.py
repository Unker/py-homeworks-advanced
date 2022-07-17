import unittest
from unittest.mock import patch
import sys
sys.path.append('../src')
import app
from app import documents, directories


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
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

    def test_remove_doc_from_shelf(self):
        num_doc = documents[0]["number"]
        self.assertIsNotNone(self._get_doc_shelf(num_doc))
        ret = app.remove_doc_from_shelf(num_doc)
        self.assertTrue(ret)
        self.assertIsNone(self._get_doc_shelf(num_doc))
        # check not available doc
        num_doc = 'InvalidDocNumber'
        self.assertIsNone(self._get_doc_shelf(num_doc))
        ret = app.remove_doc_from_shelf(num_doc)
        self.assertFalse(ret)

    def test_add_new_shelf(self):
# default val -> input
# new number
# already exist number
# not number


if __name__ == '__main__':
    unittest.main()
