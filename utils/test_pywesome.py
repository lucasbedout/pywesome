import pywesome as _
import unittest
import json

class TestCollectutilsMethods(unittest.TestCase):

    def test_map(self):
    	col = [1, 2, 3, 4]
    	mapped_col = _.map(col, lambda n: n + 1)
    	self.assertEquals(mapped_col, [2, 3, 4, 5])

    	col = [{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name'}]
    	mapped_col = _.map(col, lambda o: o['id'])
    	self.assertEquals(mapped_col, [1, 2])

    def test_reduce(self):
        col = [1, 2, 3, 4]
        self.assertEquals(_.reduce(col, lambda t, n: t + n), 10)

        # Test with a function
        def concat(a, b):
            return a + b
        col = ['a', 'b', 'c', 'd', 'e']
        self.assertEquals(_.reduce(col, concat, 'z'), 'zabcde')

        # Test with more complex operations
        def json_merge(json_list, obj):
            d = json.loads(json_list)
            d.append(obj)
            return json.dumps(d)

        col = [{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name'}, {'id': 3, 'name': 'Name'}]
        self.assertEquals(_.reduce(col, json_merge, json.dumps([])), json.dumps(col))

    def test_filter(self):
    	col = [1, 2, 3, 4]
    	filtered_col = _.filter(col, lambda n: n < 3)
    	self.assertEquals(filtered_col, [1, 2])

    	col = [{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name', 'prop': 'value'}]
    	filtered_col = _.filter(col, lambda o: 'prop' in o)
    	self.assertEquals(filtered_col, [{'id': 2, 'name': 'Name', 'prop': 'value'}])

    def test_reject(self):
        col = [1, 2, 3, 4]
        filtered_col = _.reject(col, lambda n: n < 3)
        self.assertEquals(filtered_col, [3, 4])

        col = [{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name', 'prop': 'value'}]
        filtered_col = _.reject(col, lambda o: 'prop' in o)
        self.assertEquals(filtered_col, [{'id': 1, 'name': 'Name'}])

    def test_contains(self):
    	col = [1, 2, 3, 4]
    	self.assertTrue(_.contains(col, 2))
    	self.assertFalse(_.contains(col, 8))

    	col = [{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name', 'prop': 'value'}]
    	self.assertTrue(_.contains(col, lambda o: 'prop' in o))
    	self.assertFalse(_.contains(col, lambda o: 'noprop' in o))

    def test_search(self):
        col = [1, 2, 3, 4]
        self.assertEquals(_.search(col, 3), 2)
        self.assertEquals(_.search(col, lambda n: n > 2), 2)

        col = [{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name', 'prop': 'value'}]
        self.assertEquals(_.search(col, {'id': 1, 'name': 'Name'}), 0)

    def test_random(self):
        col = [1, 2, 3, 4]
        # Test 10 times
        for i in range(10):
            self.assertTrue(_.random(col) in col)

        self.assertEquals(len(_.random(col, 2)), 2)


class TestHelpersMethods(unittest.TestCase):

    def test_random_number(self):
        for i in range(10):
            i = _.random_number(0, 6)
            self.assertTrue(i >= 0 and i <= 6)


if __name__ == '__main__':
    unittest.main()