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
        actual_property_name = theaker_lane_mast.property_name()
        expected_property_name = 'Theaker Lane'
        self.assertEqual(actual_property_name, expected_property_name)


    def __get_mobile_phone_mast_csv_path(self):
        root_dir = pathlib.Path(__file__).parent.parent
        return root_dir.joinpath("data").joinpath("masts.csv")