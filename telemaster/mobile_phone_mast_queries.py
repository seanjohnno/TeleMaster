from telemaster import mobile_phone_mast_repository

class QueryByAscendingRent:
    def __init__(self, mast_repository: mobile_phone_mast_repository.MobilePhoneMastRepository):
        self.__mast_repository = mast_repository

    def list_masts(self):
        all_masts = self.__mast_repository.list_all_masts()
        ascending_rent_sorted_masts = sorted(all_masts, key=mobile_phone_mast_repository.MobilePhoneMastInfo.rent)
        return ascending_rent_sorted_masts[:5]