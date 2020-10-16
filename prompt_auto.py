def prompt_input(prompt, errormsg):
    """
Prompts the user for an integer using the prompt parameter.
If an invalid input is given, an error message is shown using
the error message parameter. A valid input is returned as an
integer.
"""
    
    return usr_input

number = prompt_input(
    "Give an integer: ",
    "You did not give an integer"
)
print("You gave the {} integer! Good job!".format(number))
moogles = prompt_input(
    "How many moogles are in the Moogle Village? ",
    "This is not a valid number of moogles!"
)
print("There are {} moogles in the village.".format(moogles))
