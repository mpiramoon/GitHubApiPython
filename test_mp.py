import unittest
import mp
import pandas as pd
from pandas.testing import assert_frame_equal


class Testmp(unittest.TestCase):
    def test_successfulpullwithoutToken(self):
        result,end=mp.request("dbt-labs","dbt-core","","pulls")
        data = {'title':['CT-808 more grant adapter tests', 'Proper internal representation', '[Draft] Adding dependency docs and requirements.txt'],
        'number':[5452, 5451, 5450]}
        df = pd.DataFrame(data)
        self.assertEqual(int(end),3)
        assert_frame_equal(result,df)
    
    def test_failpullwithoutToken(self):
       try:
         result,end=mp.request("dbt-labs","dbt-cre","","pulls")
       except:
        pass
        

    def test_successfullReleaseswithoutToken(self):
        result,end=mp.request("dbt-labs","dbt-core","","releases")
        data = {'name':["dbt-core v1.2.0b1", "dbt-core v1.1.1", "dbt-core v1.0.8"]}
        df = pd.DataFrame(data)
        self.assertEqual(int(end),3)
        assert_frame_equal(result,df)

    def test_failReleaseswithoutToken(self):
        try:
          result,end=mp.request("dbt-labs","dbt-co","","releases")
        except:
            pass
    
    def test_failReleaseswithToken(self):
        try:
          result,end=mp.request("dbt-labs","dbt-co","sdfdsfsdfsgdsg","releases")
        except:
            pass

    def test_failPullwithToken(self):
        try:
          result,end=mp.request("dbt-labs","dbt-co","sdfdsfsdfsgdsg","pulls")
        except:
            pass
    
   
    def test_successfulPullsswithToken(self):
            token="validToken"
            owner="validowner"
            repo="validRepository"
            result,end=mp.request(owner,repo,token,"pulls")
            #data is a result of my private repository
            data = {'title':['EditDeletePage', 'HomePageBody', 'change home page'],
            'number':[4, 3, 2]}
            df = pd.DataFrame(data)
            self.assertEqual(int(end),3)

    
   