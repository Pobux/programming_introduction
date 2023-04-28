import datetime

class ItWasTooLongException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

def quiz(question, response, n_secs):
    quiz_begin_at = datetime.datetime.now()
    time_n_secs = datetime.timedelta(seconds=n_secs)

    timeout_at = quiz_begin_at + time_n_secs

    while timeout_at > datetime.datetime.now():
        user_response = input("Your answer?: ")

        if user_response == response:
            print("You win")
            return
        else:
            print("Wrong answer")

    raise ItWasTooLongException("Too much time")


quiz("I'm a cegep in Quebec city, who am I", "Garneau", 1)
