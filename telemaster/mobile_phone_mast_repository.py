import csv
from typing import List

class MobilePhoneMastInfo:
    def __init__(self, csv_row):
        self.__csv_row = csv_row

    def property_name(self):
        return self.__csv_row['Property Name']

    def rent(self):
        return self.__csv_row['Current Rent']

    def lease_years(self):
        return self.__csv_row['Lease Years']

    def tenant_name(self):
        return self.__csv_row['Tenant Name']

    def lease_start_date(self):
        return self.__csv_row['Lease Start Date']

    def property_1st_line_address(self):
        return self.__csv_row['Property Address [1]']
    
    def property_2nd_line_address(self):
        return self.__csv_row['Property  Address [2]']

    def property_3rd_line_address(self):
        return self.__csv_row['Property Address [3]']

    def property_4th_line_address(self):
        return self.__csv_row['Property Address [4]']

    def property_unit_name(self):
        return self.__csv_row['Unit Name']
    
    def lease_end_date(self):
        return self.__csv_row['Lease End Date']
    
    def current_rent(self):
        return self.__csv_row['Current Rent']

class MobilePhoneMastRepository:
    def __init__(self, csv_file_location: str):
        self.__csv_file_location = csv_file_location

    def list_all_masts(self) -> List[MobilePhoneMastInfo]:
        with open(self.__csv_file_location) as csvfile:
             reader = csv.DictReader(csvfile)
             return [MobilePhoneMastInfo(row) for row in reader]
