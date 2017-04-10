# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mypkg
import unittest
import pandas as pd

# Import from our lib
from mypkg.lib import clean_data


class TestUtils(unittest.TestCase):

    # @unittest.skip('')
    def test_clean_data(self):
        datapath = os.path.dirname(os.path.abspath(mypkg.__file__)) + '/data'
        df = pd.read_csv('{}/mon_csv_lingerie.csv'.format(datapath))
        self.assertEqual(df.shape, (97, 3))
        out = clean_data(df)
        self.assertEqual(out.shape, (97, 2))

if __name__ == '__main__':
    unittest.main()
