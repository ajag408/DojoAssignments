import bike
import car
import product_copy
from store_copy import Store
import animal
import mathDojo
import callCenter
import hospital
import underscore

bike1 = bike.Bike(300, 50)
print bike1

car1 = car.Car(1000, "25mph", "Half-full", "14mpg")
print car1

product1 = product_copy.Product(25, 'undies', '2 kg', 'hanes', 2)
print product1

safeway = Store([], 'Sunnyvale', 'MoolahBaby')
print safeway

animal1 = animal.Animal("animal")
print animal1

dog1 = animal.Dog('dog')
print dog1

dragon1 = animal.Dragon('drodro')
print dragon1

md = mathDojo.MathDojo()
print md

call1 = callCenter.Call('akash', 'to dance')
print call1

att = callCenter.CallCenter()
print att

akash = hospital.Patient('Akash', ['Cold water', 'Color weather'])
print akash

kaiser = hospital.Hospital('Kaiser', 30)
print kaiser

_ = underscore.Underscore()
print _
