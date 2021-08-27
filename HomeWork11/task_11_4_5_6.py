"""
Реализовать работу над проектом «Склад оргтехники».
1. Создать класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
2. Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
3. Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class OfficeEquipmentWarehouse:
    data_of_office_equipment_by_department_of_the_company = {
        'My_small_company':
            {'department1': 0, 'department2': 0},
        'My_big_company':
            {'department1': 0, 'department2': 0, 'department3': 0, 'department4': 0}
    }
    office_equipment_warehouse_data = {
        'Printer': 400,
        'Scanner': 200,
        'Copier': 300,
        'Fax': 100
    }

    def __init__(self, capacity_of_office_equipment_units):
        self.capacity = capacity_of_office_equipment_units

    def get_a_list_of_company_names(self):
        return self.data_of_office_equipment_by_department_of_the_company.keys()

    def get_a_list_of_departments_of_this_company(self, company):
        return self.data_of_office_equipment_by_department_of_the_company[company].keys()

    def get_a_list_of_office_equipment(self):
        return self.office_equipment_warehouse_data.keys()

    def print_office_equipment(self):
        for key, value in self.office_equipment_warehouse_data.items():
            print(f'{key}: {value}')

    def print_office_equipment_by_department_of_the_company(self):
        for key, value in self.data_of_office_equipment_by_department_of_the_company.items():
            print(f'{key}: {value}')

    @property
    def total_office_equipment(self):
        total = 0
        for key, value in self.office_equipment_warehouse_data.items():
            total += value
        return total

    def is_valid_data(self, name, number, *args):
        if args:
            company_name, department_name = args
            if company_name not in self.get_a_list_of_company_names() or \
                    department_name not in self.get_a_list_of_departments_of_this_company(company_name):
                print('Such company or department is not listed')
                return False
        if name in self.get_a_list_of_office_equipment() and type(number) == int:
            return True
        else:
            print('Refine the data. Data is not correct')
            return False

    def acceptance_of_office_equipment_to_the_warehouse(self, *args):
        for office_equipment_name, number_of_units in args:
            if self.is_valid_data(office_equipment_name, number_of_units):
                if (self.total_office_equipment + number_of_units) <= self.capacity:
                    self.office_equipment_warehouse_data[office_equipment_name] += number_of_units
                else:
                    print(f'Capacity of office equipment warehouse {self.capacity} units.\nThe warehouse '
                          f'is unable to accept additional {number_of_units} units of {office_equipment_name}')
            else:
                print('Unable to perform the operation of receiving office equipment.')

    def transfer_to_a_division_of_the_company(self, company, department, *args):
        for office_equipment_name, number_of_units in args:
            if self.is_valid_data(office_equipment_name, number_of_units, company, department):
                self.data_of_office_equipment_by_department_of_the_company[company][department] += number_of_units
                self.office_equipment_warehouse_data[office_equipment_name] -= number_of_units
            else:
                print('Unable to perform office equipment transfer operation.')


class OfficeEquipment:
    def __init__(self, printed_form_of_the_information, digital_form_of_the_information, speed, resolution,
                 color='black_and_white', press_a_button_to_start_the_process=False):
        self.push_a_button = press_a_button_to_start_the_process
        self.speed = speed
        self.print_quality = resolution
        self.color = color
        self.hard_copy = printed_form_of_the_information
        self.soft_copy = digital_form_of_the_information


class Printer(OfficeEquipment):
    def __init__(self, *args, select_soft_copy_for_process=True, copy_onto='paper', size_of_paper='A4',
                 number_of_copies=1):
        super().__init__(*args)
        self.select_soft_copy = select_soft_copy_for_process
        self.printer_connectivity_type = ('USB', 'Ethernet', 'Bluetooth')
        self.printer_features = ('automatic_two_sided', 'printing', 'Network_ready', 'CD_printing', 'sticker_printing')
        self.copy_onto = copy_onto
        self.size_of_paper = size_of_paper
        self.number_of_copies = number_of_copies

    def process_the_soft_copy_and_produces_its_hard_copy(self, *args):
        pass


class Scanner(OfficeEquipment):
    def __init__(self, *args, place_a_hard_copy_on_the_platen=True):
        super().__init__(*args)
        self.control_the_input_settings = True
        self.place_a_hard_copy = place_a_hard_copy_on_the_platen
        self.stores_a_digital_copy = ('on_a_memory_card', 'on_a_USB_device', 'transmits_to_a_computer_via_email',
                                      'transmits_to_a_computer_via_network', 'transmit_wireless_to_portable_devices')

    def process_the_hard_copy_and_produces_its_soft_copy(self, *args):
        pass

    def store_of_the_soft_copy(self, *args):
        pass


class Copier(OfficeEquipment):
    def __init__(self, *args, place_a_hard_copy_on_the_platen=True, copy_onto='paper', size_of_paper='A4',
                 number_of_copies=1):
        super().__init__(*args)
        self.place_a_hard_copy = place_a_hard_copy_on_the_platen
        self.copy_onto = copy_onto
        self.size_of_paper = size_of_paper
        self.number_of_copies = number_of_copies

    def prints_duplicates_of_the_hard_copy(self, *args):
        pass


stockroom = OfficeEquipmentWarehouse(1200)
stockroom.print_office_equipment()
print('Total: ', stockroom.total_office_equipment)
print()
stockroom.acceptance_of_office_equipment_to_the_warehouse(('Printer', 70), ('Scanner', 80), ('Copier', 60), ('Fax', 5))
stockroom.print_office_equipment()
print('Total: ', stockroom.total_office_equipment)
print()
stockroom.acceptance_of_office_equipment_to_the_warehouse(('Printer', 50), ('Scanner', 20), ('Copier', 10), ('Fax', 5))
stockroom.print_office_equipment()
print('Total: ', stockroom.total_office_equipment)
print()
stockroom.acceptance_of_office_equipment_to_the_warehouse(('Pr', 50))
print()
stockroom.transfer_to_a_division_of_the_company('My_small_company', 'department1',
                                                ('Printer', 30), ('Scanner', 20), ('Copier', 10), ('Fax', 5))
stockroom.transfer_to_a_division_of_the_company('My_big_company', 'department1',
                                                ('Printer', 30), ('Scanner', 20), ('Copier', 10), ('Fax', 5))
stockroom.transfer_to_a_division_of_the_company('My_big_company', 'department2',
                                                ('Printer', 30), ('Scanner', 20), ('Copier', 10), ('Fax', 5))
stockroom.print_office_equipment_by_department_of_the_company()
stockroom.print_office_equipment()
print('Total: ', stockroom.total_office_equipment)
print()
stockroom.transfer_to_a_division_of_the_company('My_big_company', 'department3', ('Printer', '50units'))
print()
stockroom.transfer_to_a_division_of_the_company('My_loser_company', 'department1', ('Printer', 20))
print()
stockroom.transfer_to_a_division_of_the_company('My_big_company', 'department10', ('Copier', 60))
