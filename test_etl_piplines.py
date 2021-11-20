import unittest
import etl_piplines as etl
class TestPiplines(unittest.TestCase):
    def test_extraction(self):
        self.assertGreaterEqual(len(etl.source_file_txt.index),1)

    def test_remove_null(self):
       self.assertEquals( etl.transform_data.isnull().values.any(),False)

    def test_salary_more_than_25(self):
        self.assertEquals(
            etl.test_salary_more_than_25(etl.df_salary_more_than_25['salary'].astype('int'),24),True)

if __name__ == '__main__':
    unittest.main()