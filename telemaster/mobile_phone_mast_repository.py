import csv
import datetime
import time
from typing import List

class MobilePhoneMastInfo:
    def __init__(self, csv_row):
        self.__csv_row = csv_row

    def property_name(self):
        return self.__csv_row['Property Name']

    def rent(self):
        return float(self.__csv_row['Current Rent'])

    def lease_years(self):
        return int(self.__csv_row['Lease Years'])

    def tenant_name(self):
        return self.__csv_row['Tenant Name']

    def lease_start_date(self):
        date = self.__csv_row['Lease Start Date']
        return self.__parse_date(date)

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
        date = self.__csv_row['Lease End Date']
        return self.__parse_date(date)
    
    def __parse_date(self, date):
        parsed_date_struct = time.strptime(date, '%d %b %Y')
        return datetime.date(parsed_date_struct[0], parsed_date_struct[1], parsed_date_struct[2])

class MobilePhoneMastRepository:
    def __init__(self, csv_file_location: str):
        self.__csv_file_location = csv_file_location

    def list_all_masts(self) -> List[MobilePhoneMastInfo]:
        with open(self.__csv_file_location) as csvfile:
             reader = csv.DictReader(csvfile)
             return [MobilePhoneMastInfo(row) for row in reader]
