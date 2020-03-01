import unittest
from unittest import mock
from telemaster import mobile_phone_mast_repository, mobile_phone_mast_queries

class TestOrderingByRentQuery(unittest.TestCase):

    def test_masts_ordered_by_rent_in_ascending_order(self):
        mock_mast_repository = mock.MagicMock()
        mock_mast_repository.list_all_masts.return_value = [
            self.__mock_mast_with_rent(3000),
            self.__mock_mast_with_rent(2000),
            self.__mock_mast_with_rent(1000)
        ]

        query_ascending_rent = mobile_phone_mast_queries.QueryByAscendingRent(mock_mast_repository)
        masts = query_ascending_rent.list_masts()

        self.assertEqual(masts[0].rent(), 1000)
        self.assertEqual(masts[1].rent(), 2000)
        self.assertEqual(masts[2].rent(), 3000)

    def test_masts_returned_are_limited_to_5_items(self):
        mock_mast_repository = mock.MagicMock()
        mock_mast_repository.list_all_masts.return_value = [self.__mock_mast_with_rent(rent = (x * 1000)) for x in range(0, 20)]

        query_ascending_rent = mobile_phone_mast_queries.QueryByAscendingRent(mock_mast_repository)
        masts = query_ascending_rent.list_masts()

        self.assertEqual(len(masts), 5)

    def __mock_mast_with_rent(self, rent: int) -> mobile_phone_mast_repository.MobilePhoneMastInfo:
        return mobile_phone_mast_repository.MobilePhoneMastInfo({
            'Current Rent': rent
        })

class TestLeaseYearsEqual25Query(unittest.TestCase):

    def test_masts_ordered_by_rent_in_ascending_order(self):
        mock_mast_repository = mock.MagicMock()
        mock_mast_repository.list_all_masts.return_value = [
            self.__mock_mast_with_lease_years(26),
            self.__mock_mast_with_lease_years(25),
            self.__mock_mast_with_lease_years(24)
        ]

        query_ascending_rent = mobile_phone_mast_queries.QueryBy25LeaseYears(mock_mast_repository)
        masts = query_ascending_rent.list_masts()

        self.assertEqual(len(masts), 1)
        self.assertEqual(masts[0].lease_years(), 25)
    
    def __mock_mast_with_lease_years(self, lease_years: int) -> mobile_phone_mast_repository.MobilePhoneMastInfo:
        return mobile_phone_mast_repository.MobilePhoneMastInfo({
            'Lease Years': lease_years
        })

class TestMastCountByTenantQuery(unittest.TestCase):
    
    def test_correct_mast_counts_are_assigned_to_tenants(self):
        mock_mast_repo = mock.MagicMock()
        mock_mast_repo.list_all_masts.return_value = [
            self.__mock_mast_with_tenant_name('Arqiva Ltd'),
            self.__mock_mast_with_tenant_name('Vodafone Ltd'),
            self.__mock_mast_with_tenant_name('Arqiva Ltd'),
            self.__mock_mast_with_tenant_name('Vodafone Ltd'),
            self.__mock_mast_with_tenant_name('Vodafone Ltd')
        ]

        mast_provider = mobile_phone_mast_queries.QueryTenantMastCounts(mock_mast_repo)
        tenant_to_mastcount_dict = mast_provider.list_tentant_mast_counts()
        
        self.assertEqual(tenant_to_mastcount_dict, {
            'Arqiva Ltd': 2,
            'Vodafone Ltd': 3
        })

    def __mock_mast_with_tenant_name(self, tenant_name: str) -> mobile_phone_mast_repository.MobilePhoneMastInfo:
        return mobile_phone_mast_repository.MobilePhoneMastInfo({
            'Tenant Name': tenant_name
        })

class TestLeaseDateIsBetweenDatesQuery(unittest.TestCase):
    
    START_DATE = '01 Jun 1999'
    END_DATE = '31 Aug 2007'

    def test_masts_with_lease_date_within_date_range_are_returned(self):
        mock_mast_repo = mock.MagicMock()
        mock_mast_repo.list_all_masts.return_value = [
            self.__create_mast_with_lease_start_date('01 Sep 2007'),
            self.__create_mast_with_lease_start_date('21 Mar 2001'),
            self.__create_mast_with_lease_start_date('05 Jul 1994'),
            self.__create_mast_with_lease_start_date('28 Oct 2005')
        ]

        mast_provider = mobile_phone_mast_queries.QueryLeaseIsBetweenDates(mock_mast_repo)
        masts = mast_provider.list_masts()
        
        self.assertEqual(len(masts), 2)
        self.assertEqual(masts[0].lease_start_date(), '21 Mar 2001')
        self.assertEqual(masts[1].lease_start_date(), '28 Oct 2005')


    def __create_mast_with_lease_start_date(self, lease_start_date: str) -> mobile_phone_mast_repository.MobilePhoneMastInfo:
        return mobile_phone_mast_repository.MobilePhoneMastInfo({
            'Lease Start Date': lease_start_date
        })