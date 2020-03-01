import csv

class MobilePhoneMastRepository:
    def __init__(self, csv_file_location: str):
        self.__csv_file_location = csv_file_location

    def list_all_masts(self):
        return []