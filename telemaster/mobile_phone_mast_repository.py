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

class MobilePhoneMastRepository:
    def __init__(self, csv_file_location: str):
        self.__csv_file_location = csv_file_location

    def list_all_masts(self) -> List[MobilePhoneMastInfo]:
        with open(self.__csv_file_location) as csvfile:
             reader = csv.DictReader(csvfile)
             return [MobilePhoneMastInfo(row) for row in reader]
