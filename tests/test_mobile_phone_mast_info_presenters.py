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
    
class TestMastInfoPresenter(unittest.TestCase):
    
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
            '[Current Rent]: 12750.0'
        ])

    SINGLE_PHONE_MAST_INFO_ITEM_WITH_FORMATTED_DATE = '\n'.join([
            '[Property Name]: Theaker Lane',
            '[Property Address 1]: Burnsall Grange',
            '[Property Address 2]: Leeds',
            '[Property Address 3]: -',
            '[Property Address 4]: LS12',
            '[Unit Name]: Burnsall Grange - WYK0144',
            '[Tenant Name]: Everything Everywhere Ltd',
            '[Lease Start Date]: 29/04/2008',
            '[Lease End Date]: 28/04/2018',
            '[Lease Years]: 10',
            '[Current Rent]: 12750.0'
        ])

    def test_presenter_formats_data_correctly(self):
        presenter = mobile_phone_mast_info_presenters.FullMastInfoPresenter([
            mobile_phone_mast_repository.MobilePhoneMastInfo(SharedTestData.CSV_DATA),
            mobile_phone_mast_repository.MobilePhoneMastInfo(SharedTestData.CSV_DATA)
        ])
                
        expected_output = '\n\n'.join([
            TestMastInfoPresenter.SINGLE_PHONE_MAST_INFO_ITEM, 
            TestMastInfoPresenter.SINGLE_PHONE_MAST_INFO_ITEM])

        actual_output = presenter.output_mast_info_items()
        self.assertEqual(actual_output, expected_output)

    def test_presenter_formats_date_when_format_is_supplied(self):
        mast_info_list = [
            mobile_phone_mast_repository.MobilePhoneMastInfo(SharedTestData.CSV_DATA)
        ]

        presenter = mobile_phone_mast_info_presenters.FullMastInfoPresenter(mast_info_list, date_format = "%d/%m/%Y")
                
        expected_output = TestMastInfoPresenter.SINGLE_PHONE_MAST_INFO_ITEM_WITH_FORMATTED_DATE
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
                
        expected_output = "\n\n[TOTAL RENT]: 25500.00"
        actual_output = presenter.output_mast_info_items()
        self.assertEquals(actual_output, expected_output)
    
class TestTenantToMastCountPresenter(unittest.TestCase):
    
    def test_tenant_to_mast_count_is_displayed_correctly(self):

        tenant_to_mast_count_dict = {
            "Tenant 1": 10,
            "Tenant 2": 4
        }

        presenter = mobile_phone_mast_info_presenters.TenantToMastCountPresenter(tenant_to_mast_count_dict)
        actual_output = presenter.output_mast_info_items()
        
        actual_output_lines = actual_output.splitlines()
        self.assertEquals(len(actual_output_lines), 2)
        self.assertTrue("[Tenant Name]: Tenant 1 [Mast Count]: 10" in actual_output_lines)
        self.assertTrue("[Tenant Name]: Tenant 2 [Mast Count]: 4" in actual_output_lines)
        