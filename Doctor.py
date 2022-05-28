"""Создать производный от Person класс Doctor.
Новые поля: номер удостоверения, специальность, список текущих
пациентов (словарь вида номер медицинской книжки: ФИ пациента).
Определить конструктор, с вызовом родительского
конструктора. Определить функции добавления нового пациента, удаления выписанного, форматированной печати
всех пациентов. Переопределить метод преобразования в строку для печати основной информации (ФИ, возраст,
номер удостоверения, специальность).
"""

from Person import Person
from logging import log

class Doctor(Person):
    def __init__(self, arg_name, arg_surname, arg_age, arg_id, arg_special):
        super().__init__(arg_name, arg_surname, arg_age)
        self.id = arg_id
        self.special = arg_special
        self.patient_list = {}
        log("CRE", "Class (Doctor) object", "__init__")

    def new_patient(self, arg_id_patient, arg_patient_fullname):
        self.patient_list.update({arg_id_patient:arg_patient_fullname})
        log("INF", f"Class (Doctor) patient[{arg_id_patient}]", "new_patient", "add")

    def del_patient(self, arg_id_patient):
        self.patient_list.pop(arg_id_patient)
        log("INF", f"Class (Doctor) patient[{arg_id_patient}]", "del_patient", "del")

    def print_patient_list(self):
        s = f'Patient list of {self.special} {self.surname} {self.name}:\n'
        if len(self.patient_list) != 0:
            for i in self.patient_list:
                s += f'Id: {i}   Name of patient: {self.patient_list[i]}\n'
            log("INF", f"Class (Doctor) patient list", "print_patient_list", "ptr")
            return s
        else:
            log("INF", f"Class (Doctor) patient list", "print_patient_list", "ptr")
            return "This doctor doesn't have patients.\n"

    def __str__(self):
        s = f"Doctor's name: {self.surname} {self.name}\nAge: {self.age}   Speciality: {self.special}   Id: {self.id}"
        log("INF", f"Class (Doctor) object", "__str__", "ptr")
        return s
