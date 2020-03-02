from typing import List
from telemaster import mobile_phone_mast_repository

class FullMastInfoPresenter:

    def __init__(self, mast_info_items: List[mobile_phone_mast_repository.MobilePhoneMastInfo]):
        self.__mast_info_items = mast_info_items

    def output_mast_info_items(self) -> str:
        return ""