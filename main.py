from telemaster import telemaster_service

if __name__ == "__main__":
    service = telemaster_service.TelemasterService()    
    should_exit = False

    while not should_exit:
        options = '\n'.join([
            "\t1. Mobile phone masts ordered by ascending rent (5 items)",
            "\t2. Mobile phone masts with a lease of 25 years + tallied rent",
            "\t3. Tenant name > Mast Counts",
            "\t4. Mobile phone masts with a lease start date between 1 st June 1999 and 31st August 2007",
            "\t5. To exit",
            "Enter one of the numbers above to continue: "
        ])
        intput_txt = input (options)

        try:
            selected_option = int(intput_txt)

            if selected_option == 1:
                print(service.masts_by_ascending_rent())

            elif selected_option == 2:
                print(service.masts_with_a_lease_of_25_years())

            elif selected_option == 3:
                print(service.masts_by_tenant_name())

            elif selected_option == 4:
                print(service.masts_with_a_lease_date_between())

            elif selected_option == 5:
                should_exit = True

            else:
                raise ValueError("")

        except:
            print(f"Sorry I didn't understand {intput_txt}. Let's try again...\n")