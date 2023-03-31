def check_input_for_number(plant):
    print(plant)


#check_input_for_number("Pissenlit")

def f(x):
    print("I'm inside")
    x = 20
    print(x)

x = 15
#f()
#print(x)

from my_util_folder import utils
result = utils.multiplication(2, 5)
print(result)

def only_numbers(my_list):
    my_new_list = []
    for element in my_list:
        if type(1) == type(element):
            my_new_list.append(element)
    
    return my_new_list

my_list = [1, "A", 3, True, "B"]
#clean_result = only_numbers(my_list)

#print(clean_result)