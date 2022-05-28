"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.

Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""

from Doctor import Doctor
from Nurse import Nurse
from Hospital import Hospital
import pickle

if __name__ == '__main__':
    doctor1 = Doctor("Ivan", "Ivanov", 34, 123, "Doctor")
    doctor2 = Doctor("Petr", "Petrovich", 69, 52, "Doctor")
    doctor3 = Doctor("Ling", "Bimov", 32, 75, "Doctor")
    doctor4 = Doctor("Sang", "Relimi", 20, 35, "Doctor")
    doctor5 = Doctor("Tima", "Colin", 22, 437, "Doctor")
    doctor1.new_patient(1, "Kim Ri")
    doctor1.new_patient(2, "Kate Mi")
    doctor1.new_patient(3, "Rina Ki")
    doctor2.new_patient(4, "Lina Vi")
    doctor1.del_patient(2)
    #print(doctor1.print_patient_list())
    #print(doctor1.patient_list.get(1))
    #print(doctor1)

    nurse1 = Nurse("Kate", "Bi", 22, 120, 6)
    nurse1.update_schedule_day("Monday","12:00-20:00")
    nurse1.update_schedule_day("Tuesday","8:00-16:00")
    nurse1.update_schedule_day("Sunday","11:00-15:00")

    nurse2 = Nurse("Olga", "Vam", 37, 111, 5)
    nurse2.update_schedule_day("Thursday","10:00-20:00")
    nurse2.update_department(3)

    nurse3 = Nurse("Tina", "Rin", 28, 24, 5)
    nurse3.update_schedule_day("Saturday","6:00-18:00")
    nurse3.update_schedule_day("Wednesday","18:00-00:00")

    nurse4 = Nurse("Vera", "Riven", 18, 90, 4)


    Hospital1 = Hospital("ABClinic", "PROSPRCT VERNADSKOGO")

    Hospital1.doctor_list.append(doctor1)
    Hospital1.doctor_list.append(doctor2)
    Hospital1.doctor_list.append(doctor3)
    Hospital1.doctor_list.append(doctor4)

    Hospital1.nurse_list.append(nurse1)
    Hospital1.nurse_list.append(nurse2)
    Hospital1.nurse_list.append(nurse3)
    Hospital1.nurse_list.append(nurse4)
    Hospital1+doctor5


    Hospital1.__delitem__(2)
    #print(Hospital1)
    #Hospital1.get_doctor_by_id(4)

    #TaskD-1
    with open('data.pickle', 'wb') as file:
        pickle.dump(Hospital1, file)

    with open('data.pickle', 'rb') as file:
        Hospital = pickle.load(file)
    print(Hospital1)

    Hospital1.file('myfile.txt')
