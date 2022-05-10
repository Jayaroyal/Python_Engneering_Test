import csv
import unittest
import writecsv


class TestWritecsv(unittest.TestCase):
    def read_csv_file(self):
        self.assertEqual(writecsv.read_csv_file('Asia Prod 1.csv','Combined.csv')
        self.assertEqual(writecsv.read_csv_file('Asia Prod 2.csv','Combined.csv')
        self.assertEqual(writecsv.read_csv_file('Asia Prod 3.csv','Combined.csv')
        self.assertEqual(writecsv.read_csv_file('NA Prod.csv','Combined.csv')

if __name__ == "__main__":
   unittest.main()