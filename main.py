import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
data =  pd.read_csv("50_states.csv")
state = data["state"]
state_list = state.to_list()
guessed_states = []
while len(guessed_states)<50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States guessed", prompt="What's another state's name?").title()

    if answer in state_list:


        name = data[data["state"]==answer].index.values
        x_cor = data['x'].loc[data.index[name]]
        x_cor_l = x_cor.to_list()
        y_cor = data['y'].loc[data.index[name]]
        y_cor_l = y_cor.to_list()

        tim.setposition(x_cor_l[0],y_cor_l[0])
        tim.write(f"{answer}",align="left",font=("Verdana",10,"normal"))
    guessed_states.append(answer)
# print(data)

# print(state_list)
# for i in state_list:
#     if answer == i:
#

screen.exitonclick()