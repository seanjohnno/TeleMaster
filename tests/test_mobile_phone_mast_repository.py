import datetime
import pathlib
import unittest
from telemaster import mobile_phone_mast_repository

class TestMastRepository(unittest.TestCase):

    EXPECTED_ROW_COUNT = 42
    THEAKER_LANE_CSV_ROW = 9

    def test_expected_row_count_is_loaded(self):
        csv_file_location = self.__get_mobile_phone_mast_csv_path()

        repository = mobile_phone_mast_repository.MobilePhoneMastRepository(csv_file_location)
        mobile_telephone_mast_list = repository.list_all_masts()

        self.assertEqual(len(mobile_telephone_mast_list), TestMastRepository.EXPECTED_ROW_COUNT)

    def test_expected_row_data_is_loaded(self):
        csv_file_location = self.__get_mobile_phone_mast_csv_path()

        repository = mobile_phone_mast_repository.MobilePhoneMastRepository(csv_file_location)
        mobile_telephone_mast_list = repository.list_all_masts()
        theaker_lane_mast = mobile_telephone_mast_list[TestMastRepository.THEAKER_LANE_CSV_ROW]
        
        self.assertEquals(theaker_lane_mast.property_name(), 'Theaker Lane')
        self.assertEquals(theaker_lane_mast.rent(), 12750.0)
        self.assertEquals(theaker_lane_mast.lease_years(), 10)
        self.assertEquals(theaker_lane_mast.tenant_name(), 'Everything Everywhere Ltd')
        self.assertEquals(theaker_lane_mast.lease_start_date(), datetime.date(2008, 4, 29))
        self.assertEquals(theaker_lane_mast.lease_end_date(), datetime.date(2018, 4, 28))  
        self.assertEquals(theaker_lane_mast.property_1st_line_address(), 'Burnsall Grange')  
        self.assertEquals(theaker_lane_mast.property_2nd_line_address(), 'Leeds')  
        self.assertEquals(theaker_lane_mast.property_3rd_line_address(), '')  
        self.assertEquals(theaker_lane_mast.property_4th_line_address(), 'LS12')  
        self.assertEquals(theaker_lane_mast.property_unit_name(), 'Burnsall Grange - WYK0144')  

    def __get_mobile_phone_mast_csv_path(self):
        root_dir = pathlib.Path(__file__).parent.parent
        return root_dir.joinpath("data").joinpath("masts.csv")