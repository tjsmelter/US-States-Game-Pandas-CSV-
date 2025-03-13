# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


guessed_states = []

while len(guessed_states) < 50:
    # collect user input and save to a variable
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # create conditional for when the user wants to exit the game
    if answer_state == "Exit":
        # create a new list for states that have not been guessed yet
        missing_states = [state for state in all_states if state not in guessed_states]

        # create a new data frame from the list
        new_data = pandas.DataFrame(missing_states)

        # save the new data frame to a csv
        new_data.to_csv("states_to_learn.csv")
        break
        
    # create conditional to check if answer was already guessed or if it was not a valid entry  
    if answer_state in guessed_states:
        print("You already guessed that state")
   
    elif answer_state in all_states:
        # append the input to the guessed states list
        guessed_states.append(answer_state)
        
        # if they get it right, create a turtle at the correct x and y coordinates
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())
    else:
        print(f"Try again, {answer_state} is not a US state.")
