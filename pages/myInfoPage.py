from .basePage import BasePage




class MyInfoPage(BasePage):

    def __init__(self, page):
        super().__init__(page=page)

    def change_employer_full_name(self, first_name:str, second_name:str, last_name:str):
        pass

    def change_employee_id(self, new_id:str):
        pass

    def change_driver_lices_number(self, driver_licence_number:str):
        pass

    def change_gender(self, gender):
        pass
    
    def change_nationality(self, nationality:str):
        pass
    
    def change_maritial_status(self, maritital_status:str):
        pass

    def change_date_of_birth(self, date_of_birth:str):
        pass

    def change_blood_type(self, blood_type:str):
        pass