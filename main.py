import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

# Change shape of the turtle to the picture
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []
points = len(guessed_states)

while points != 50:
    state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name? ").title()
    if state == "Exit":
        states_to_learn = pandas.DataFrame(states_list)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if state in states_list and state not in guessed_states:
        guessed_states.append(state)
        states_list.remove(state)
        points += 1
        coordinates = data[data.state == state]
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(int(coordinates.x), int(coordinates.y))
        state_name.write(state)


# Read the coordinates of the States on the map

# # Function to print the coordinates of the place that user click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# # It will return the coordinates of the place that user click
# turtle.onscreenclick(get_mouse_click_coor)
#
# # loop which will continue after the mouse click
# turtle.mainloop()
