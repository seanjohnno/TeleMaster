import csv
from typing import List

class MobilePhoneMastInfo:
    def __init__(self, csv_row):
        self.__csv_row = csv_row

class MobilePhoneMastRepository:
    def __init__(self, csv_file_location: str):
        self.__csv_file_location = csv_file_location

    def list_all_masts(self) -> List[MobilePhoneMastInfo]:
        with open(self.__csv_file_location) as csvfile:
             reader = csv.DictReader(csvfile)
             return [MobilePhoneMastInfo(row) for row in reader]
