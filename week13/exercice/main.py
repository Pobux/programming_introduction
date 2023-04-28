#-*- coding: utf-8 -*-
# Creation Date : 2023-04-21
from app import garden
from app import vegetable
from app import carrot
from app import lettuce
my_new_garden = garden.Garden()
new_vegetable = vegetable.Vegetable()

carrot_days_mature = 30
lettuce_days_mature = 15
vegetables = []

for i in range(0, 10):
    vegetables.append(carrot.Carrot(carrot_days_mature))

for i in range(0, 10):
    vegetables.append(lettuce.Lettuce(lettuce_days_mature))

print(vegetables)

carrot1 = carrot.Carrot(carrot_days_mature)

for vegetable in vegetables:
    my_new_garden.plant_vegetable(vegetable)

print(my_new_garden.vegetables[0].date_to_mature())


