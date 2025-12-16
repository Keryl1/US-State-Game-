from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("U.S States Game")
screen.bgpic("blank_states_img.gif")
screen.tracer(1)


# Creates a dataframe from the 50 states csv
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


# Saves all the user guessed to a list and for each guess you get a point that's saved in score
guessed_states = []
score = 0
lives = 10


game_on = True
while game_on:

    answer = screen.textinput(title=f"{score}/{len(data.state)} States Correct", prompt="What is another states name?")

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(new_data)
        break


    if answer in all_states and answer not in guessed_states:
        score += 1
        guessed_states.append(answer)
        state_name = data[data.state == answer]
        x_cord = int(state_name.x.iloc[0])
        y_cord = int(state_name.y.iloc[0])

        state = Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x_cord, y_cord)
        state.write(arg=answer, move=False, align="center", font=('Arial', 8, 'normal'))

    elif answer not in all_states and answer in guessed_states:
        lives -= 1
        if lives == 0:
            game_on = False

screen.exitonclick()
