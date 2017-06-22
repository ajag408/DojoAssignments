from random import randint

class Patient(object):
    def __init__(self, name, allergies):
        self.id = randint(0, 30)
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def __repr__(self):
        return "<Patient object, name is {}>".format(self.name)



class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, new_patient):
        if len(self.patients) >= self.capacity:
            return 'Hospital is full!'
        else:
            bedNum = randint(0,30)
            notAssigned = True
            for patient in self.patients:
                if bedNum == patient.bed_number:
                    notAssigned = False
            if notAssigned is True:
                new_patient.bed_number = bedNum
                self.patients.append(new_patient)
                return 'Successful admission'
            else:
                self.admit(new_patient)
    def discharge(self, name):
        for patient in self.patients:
            if patient.name == name:
                patient.bed_number = None
                idx = self.patients.index(patient)
        self.patients.pop(idx)
    def testBedNumAssign(self):
        for patient in self.patients:
            print patient.bed_number
    def __repr__(self):
        return "<Hospital object, name is {}, capacity is {}>".format(self.name, self.capacity)


if __name__ == '__main__':
    akash = Patient('Akash', ['Cold water', 'Color weather'])

    charles = Patient('Charlie', [])

    kaiser = Hospital('Kaiser', 30)

    kaiser.admit(akash)
    kaiser.admit(charles)
    kaiser.testBedNumAssign()
    kaiser.discharge('Akash')
    kaiser.testBedNumAssign()
