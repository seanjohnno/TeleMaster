from typing import List
from telemaster import mobile_phone_mast_repository

class FullMastInfoPresenter:

    def __init__(self, mast_info_items: List[mobile_phone_mast_repository.MobilePhoneMastInfo]):
        self.__mast_info_items = mast_info_items

    def output_mast_info_items(self) -> str:
        return '\n'.join(self.__mast_info_to_str(mast_info_item) for mast_info_item in self.__mast_info_items)

    def __mast_info_to_str(self, mast_info_item: mobile_phone_mast_repository.MobilePhoneMastInfo) -> str:
        return '\n'.join([
            f'[Property Name]: {self.__replace_empty_str_with_dash(mast_info_item.property_name())}',
            f'[Property Address 1]: {self.__replace_empty_str_with_dash(mast_info_item.property_1st_line_address())}',
            f'[Property Address 2]: {self.__replace_empty_str_with_dash(mast_info_item.property_2nd_line_address())}',
            f'[Property Address 3]: {self.__replace_empty_str_with_dash(mast_info_item.property_3rd_line_address())}',
            f'[Property Address 4]: {self.__replace_empty_str_with_dash(mast_info_item.property_4th_line_address())}',
            f'[Unit Name]: {self.__replace_empty_str_with_dash(mast_info_item.property_unit_name())}',
            f'[Tenant Name]: {self.__replace_empty_str_with_dash(mast_info_item.tenant_name())}',
            f'[Lease Start Date]: {self.__replace_empty_str_with_dash(mast_info_item.lease_start_date())}',
            f'[Lease End Date]: {self.__replace_empty_str_with_dash(mast_info_item.lease_end_date())}',
            f'[Lease Years]: {self.__replace_empty_str_with_dash(mast_info_item.lease_years())}',
            f'[Current Rent]: {self.__replace_empty_str_with_dash(mast_info_item.rent())}'
        ])

    def __replace_empty_str_with_dash(self, input) -> str:
        return input if input else '-'
