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