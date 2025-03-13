# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

import turtle
import pandas
from states import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
print(screen.screensize())

data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)

states_correct = 0

states_list = []

# create a while loop to continue playing the game

game_is_on = True

while game_is_on:

    # collect the user input and save to a variable
    answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?").lower().capitalize()

    # create a variable storing the row of data from the data frame based that matches the user input
    answer_state_row = df[df.state == answer_state]
    print(answer_state_row)

    # check if the user input is contained in the data frame
    # mask will return a boolean for each value in the data frame based on if it matches or not
    # matches = True , does not match = False
    mask = df.isin([answer_state])
    print(mask)
    # checks the mask to see whether there are any pieces of data met the criteria and if the state has already been guessed
    # if yes, run the program. if no, inform the user that the input was not valid.
    if mask.any().any() and answer_state not in states_list:
        # remove the "dtype" and extra information that was accompanying the state name
        answer_state_var = str(answer_state_row.state.values)
        # remove the brackets and apostrophes that were accompanying the value
        answer_state_final =answer_state_var.strip("['']")

        # save the x and y coordinates from the guessed state into their own values
        answer_state_x = int(answer_state_row.x)
        answer_state_y = int(answer_state_row.y)

        # create a state and place it in the correct position
        state = State(answer_state_final,answer_state_x,answer_state_y)

        # add correctly guessed state to states list
        states_list.append(answer_state)

        # add a score to the title screen
        states_correct += 1
    else:
        print(f"Try Again, {answer_state} is not a US state.")

screen.exitonclick()
