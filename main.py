import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Getting coordinates of mouse click spots

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

score = 0
guessed_states = []
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.pencolor("black")

while score < 50:
    answer_state = screen.textinput(title=f"Guess the State ({score}/50)",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn_list = []
        for state in data.state:
            if state not in guessed_states:
                states_to_learn_list.append(state)
        states_to_learn_df = pandas.DataFrame(states_to_learn_list)
        states_to_learn_df.to_csv("states_to_learn.csv")
        break
    for state in data["state"]:
        if answer_state == state and answer_state not in guessed_states:
            score += 1
            guessed_states.append(answer_state)
            current_state = data[data["state"] == answer_state]
            pen.goto(int(current_state.x), int(current_state.y))
            pen.write(state)

