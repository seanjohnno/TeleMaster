import unittest
from unittest import mock

from telemaster import mobile_phone_mast_repository, mobile_phone_mast_info_presenters

class TestMastInfoPresenter(unittest.TestCase):
    
    def test_presenter_formats_data_correctly(self):
        dict_input = {
            'Property Name': 'Theaker Lane',
            'Property Address 1':'Burnsall Grange',
            'Property Address 2':'Leeds',
            'Property Address 3':'',
            'Property Address 4':'LS12',
            'Unit Name':'Burnsall Grange - WYK0144',
            'Tenant Name':'Everything Everywhere Ltd',
            'Lease Start Date':'29 Apr 2008',
            'Lease End Date':'28 Apr 2018',
            'Lease Years':'10',
            'Current Rent':'12750.00'
        }
        presenter = mobile_phone_mast_info_presenters.FullMastInfoPresenter([
            self.__mock_mast_with_dict(dict_input),
            self.__mock_mast_with_dict(dict_input)
        ])
                
        expected_single_output = '\n'.join([
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
        expected_output = '\n'.join([expected_single_output, expected_single_output])

        actual_output = presenter.output_mast_info_items()
        self.assertEqual(actual_output, expected_output)

    def __mock_mast_with_dict(self, dict) -> mobile_phone_mast_repository.MobilePhoneMastInfo:
        return mobile_phone_mast_repository.MobilePhoneMastInfo(dict)


    