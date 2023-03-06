# Creation Date : 2023-03-05
# Created by : Antoine LeBel

# Provide a list of dictionnary to better work with the class information
# The format should be:

# Using that list, find student that has a composite first name (ex.: José Antonio)
#[
#    {
#        "first_name": "Karina",
#        "last_name": "Dieck Elizondo",
#        "id": 3912
#    },
#    {
#        "first_name": "Gerardo",
#        "last_name": "Mier Soria",
#        "id": 6293
#    },
#]


my_data = []

# Open the file
with open("gr1.csv", encoding="ISO-8859-1") as f:
    lines = f.readlines() # this is a list of lines

    # For each line, build the data struct
    for line in lines:
        # Skip the first line
        # Split at ";="
        # Set each index to it's right key
        # Add the new dict to "my_data" using my_data.append({"the": "dict"})
        print(line)


# Iterate the dictionnary
# Look for the condition
# Print the names that are targeted
