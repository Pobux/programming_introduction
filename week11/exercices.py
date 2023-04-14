# Create a function that add a line in a file
# each time the users run the script, the line should have
# The date, the users name and a message
import datetime #datetime.now() 
import getpass  #getpass.getuser())

# Use the previous function and add an argument called "subfunc"
# Print the subfunc function name and a message to it.
# pass "look_at_photo" to the function
# This is more or less how apps online logs everything you do

def look_at_photo():
    print("User Madame is looking at the photo of her friend")

def look_at_friend():
    print("Friend")

def is_currently_eating():
    print("eating")

def im_watching_you(subfunc):
    # How can I can the function name?
    func_name = subfunc.__name__
    subfunc()
    my_date = str(datetime.datetime.now())
    user = getpass.getuser()
    sentence_to_log = my_date + ": User " + user + " logged in and used function " + func_name + "\n"

    with open("./database.txt", "a") as f:
        f.write(sentence_to_log)

for f in [look_at_photo, look_at_friend, is_currently_eating]:
    im_watching_you(f)

