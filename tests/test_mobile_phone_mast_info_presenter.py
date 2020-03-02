import unittest
from unittest import mock

from telemaster import mobile_phone_mast_repository, mobile_phone_mast_info_presenters

class SharedTestData:
    CSV_DATA = {
            'Property Name': 'Theaker Lane',
            'Property Address [1]':'Burnsall Grange',
            'Property  Address [2]':'Leeds',
            'Property Address [3]':'',
            'Property Address [4]':'LS12',
            'Unit Name':'Burnsall Grange - WYK0144',
            'Tenant Name':'Everything Everywhere Ltd',
            'Lease Start Date':'29 Apr 2008',
            'Lease End Date':'28 Apr 2018',
            'Lease Years':'10',
            'Current Rent':'12750.00'
        }
    
    SINGLE_PHONE_MAST_INFO_ITEM = '\n'.join([
            '[Property Name]: Theaker Lane',
            '[Property Address 1]: Burnsall Grange',
            '[Property Address 2]: Leeds',
            '[Property Address 3]: -',
            '[Property Address 4]: LS12',
            '[Unit Name]: Burnsall Grange - WYK0144',
            '[Tenant Name]: Everything Everywhere Ltd',
            '[Lease Start Date]: 29 Apr 2008',
            '[Lease End Date]: 28 Apr 2018',
            '[Lease Years]: 10',
            '[Current Rent]: 12750.00'
        ])

class TestMastInfoPresenter(unittest.TestCase):
    
    def test_presenter_formats_data_correctly(self):
        presenter = mobile_phone_mast_info_presenters.FullMastInfoPresenter([
            mobile_phone_mast_repository.MobilePhoneMastInfo(SharedTestData.CSV_DATA),
            mobile_phone_mast_repository.MobilePhoneMastInfo(SharedTestData.CSV_DATA)
        ])
                
        expected_output = '\n'.join([
            SharedTestData.SINGLE_PHONE_MAST_INFO_ITEM, 
            SharedTestData.SINGLE_PHONE_MAST_INFO_ITEM])

        actual_output = presenter.output_mast_info_items()
        self.assertEqual(actual_output, expected_output)

    def __mock_mast_with_dict(self, dict) -> mobile_phone_mast_repository.MobilePhoneMastInfo:
        return mobile_phone_mast_repository.MobilePhoneMastInfo(dict)

class TestTalliedRentDecorator(unittest.TestCase):

    def test_presenter_correctly_appends_rent(self):

        mast_info_items = [
            mobile_phone_mast_repository.MobilePhoneMastInfo(SharedTestData.CSV_DATA),
            mobile_phone_mast_repository.MobilePhoneMastInfo(SharedTestData.CSV_DATA)
        ]

        mock_presenter = mock.MagicMock()
        mock_presenter.output_mast_info_items.return_value = ""

        presenter = mobile_phone_mast_info_presenters.TalliedRentPesenterDecorator(mock_presenter, mast_info_items)
                
        expected_output = "\n[TOTAL RENT]: 25500.00"
        actual_output = presenter.output_mast_info_items()
        self.assertEquals(actual_output, expected_output)