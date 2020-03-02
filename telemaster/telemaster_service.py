import pathlib
from telemaster import mobile_phone_mast_repository, mobile_phone_mast_queries, mobile_phone_mast_info_presenters

class TelemasterService:
    def __init__(self):
        root_dir = pathlib.Path(__file__).parent.parent
        csv_file_location = root_dir.joinpath("data").joinpath("masts.csv")
        self.__mast_repository = mobile_phone_mast_repository.MobilePhoneMastRepository(csv_file_location)
    
    def masts_by_ascending_rent(self) -> str:
        ascending_rent_query = mobile_phone_mast_queries.QueryByAscendingRent(self.__mast_repository)
        returned_mast_items = ascending_rent_query.list_masts()

        presenter = mobile_phone_mast_info_presenters.FullMastInfoPresenter(returned_mast_items)
        return presenter.output_mast_info_items()

    def masts_with_a_lease_of_25_years(self):
        lease_25_years_query = mobile_phone_mast_queries.QueryBy25LeaseYears(self.__mast_repository)
        returned_mast_items = lease_25_years_query.list_masts()

        wrapped_presenter = mobile_phone_mast_info_presenters.FullMastInfoPresenter(returned_mast_items)
        presenter = mobile_phone_mast_info_presenters.TalliedRentPesenterDecorator(wrapped_presenter, returned_mast_items)
        return presenter.output_mast_info_items()

    def masts_by_tenant_name(self):
        tenant_mast_count_query = mobile_phone_mast_queries.QueryTenantMastCounts(self.__mast_repository)
        returned_mast_items = tenant_mast_count_query.list_tenant_mast_counts()

        presenter = mobile_phone_mast_info_presenters.TenantToMastCountPresenter(returned_mast_items)
        return presenter.output_mast_info_items()

    def masts_with_a_lease_date_between(self):
        lease_date_between_query = mobile_phone_mast_queries.QueryLeaseIsBetweenDates(self.__mast_repository)
        returned_mast_items = lease_date_between_query.list_masts()

        presenter = mobile_phone_mast_info_presenters.FullMastInfoPresenter(returned_mast_items, date_format="%d/%m/%Y")
        return presenter.output_mast_info_items()
