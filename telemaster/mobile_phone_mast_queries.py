import collections
import datetime
from operator import methodcaller
import time
from telemaster import mobile_phone_mast_repository
from typing import Dict, List


class QueryByAscendingRent:

    ITEM_LIMIT = 5

    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_masts(self) -> List[mobile_phone_mast_repository.MobilePhoneMastRepository]:  
        all_masts = self.__mast_repository.list_all_masts()
        ascending_rent_sorted_masts = sorted(all_masts, key=methodcaller('rent'))
        return ascending_rent_sorted_masts[:QueryByAscendingRent.ITEM_LIMIT]

class QueryBy25LeaseYears:

    _25_LEASE_YEARS = 25

    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_masts(self) -> List[mobile_phone_mast_repository.MobilePhoneMastRepository]:
        all_masts = self.__mast_repository.list_all_masts()
        return [mast for mast in all_masts if mast.lease_years() == QueryBy25LeaseYears._25_LEASE_YEARS]

class QueryTenantMastCounts:

    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_tenant_mast_counts(self) -> Dict[str, int]:
        return collections.Counter( [ row.tenant_name() for row in self.__mast_repository.list_all_masts() ] )

class QueryLeaseIsBetweenDates:
    
    JUNE_1ST_1999 = datetime.date(1999, 6, 1)
    AUGUST_31ST_2007 = datetime.date(2007, 8, 31)

    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_masts(self) -> List[mobile_phone_mast_repository.MobilePhoneMastRepository]:
        start_date = QueryLeaseIsBetweenDates.JUNE_1ST_1999
        end_date = QueryLeaseIsBetweenDates.AUGUST_31ST_2007

        all_masts = self.__mast_repository.list_all_masts()
        return [mast for mast in all_masts if self.__mast_is_within_dates_inclusive(mast, start_date, end_date)]

    def __mast_is_within_dates_inclusive(self, mast, start_date, end_date):
        lease_start_date = mast.lease_start_date()
        if lease_start_date >= start_date and lease_start_date <= end_date:
            return True
        return False