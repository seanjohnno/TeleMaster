import collections
from telemaster import mobile_phone_mast_repository
from typing import Dict

class QueryByAscendingRent:

    ITEM_LIMIT = 5

    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_masts(self):
        all_masts = self.__mast_repository.list_all_masts()
        ascending_rent_sorted_masts = sorted(all_masts, key=mobile_phone_mast_repository.MobilePhoneMastInfo.rent)
        return ascending_rent_sorted_masts[:QueryByAscendingRent.ITEM_LIMIT]

class QueryBy25LeaseYears:

    _25_LEASE_YEARS = 25

    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_masts(self):
        all_masts = self.__mast_repository.list_all_masts()
        return [mast for mast in all_masts if mast.lease_years() == QueryBy25LeaseYears._25_LEASE_YEARS]

class QueryTenantMastCounts:

    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_tentant_mast_counts(self) -> Dict[str, int]:
        return collections.Counter( [ row.tenant_name() for row in self.__mast_repository.list_all_masts() ] )