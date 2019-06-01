
from collective.dot import Dot as DictDot
import unittest


class TestDot(unittest.TestCase):

    def test_dict_dot(self):
        self.assertEqual(DictDot().dot('key', {'key': 'value'}), 'value')
        self.assertEqual(DictDot().dot(
            'key.test', {'key': {'test': 'value'}}), 'value')
        self.assertEqual(DictDot().dot('key.test.layer', {
                         'key': {'test': {'layer': 'value'}}}), 'value')
        self.assertEqual(DictDot().dot(
            'key.none', {'key': {'test': {'layer': 'value'}}}), None)
        self.assertEqual(DictDot().dot('key', {'key': {'test': {'layer': 'value'}}}), {
                         'test': {'layer': 'value'}})
