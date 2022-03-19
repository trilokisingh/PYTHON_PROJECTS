import turtle
import pandas


map = turtle.Turtle()
screen = turtle.Screen()
screen.setup(height=750)
screen.title("Indian States")
image = "blank_img.gif"
screen.addshape(image)
map.shape(image)


data = pandas.read_csv("in.csv")
All_State_Name = data.state.to_list()  # store all the state name in All State name file with method

guessed_State = []  # initialise a blank list for tracking score

while len(guessed_State) <= 36: # loop will run until all 36 state note completed

    answer_State = screen.textinput(title=f"{len(guessed_State)}/50 are the correct guesses",
                                    prompt="Enter the name of State").title()

    if answer_State == "Exit":
        missing_State = []
        for state in All_State_Name:
            if state not in guessed_State:
                missing_State.append(state)
                new_Data = pandas.DataFrame(missing_State)
                new_Data.to_csv("States to learn.csv")
        break

    if answer_State in All_State_Name:  # if Input is in answersate then gueessed number will append for tracking Score

        guessed_State.append(answer_State)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        #t.pencolor("red")
        state_Data = data[data.state == answer_State] # will store row corresponding to that particular state
        t.goto(int(state_Data.lat), int(state_Data.lng))  # turtle will jump to that particular cordinate
        t.write(answer_State)






#screen.exitonclick()


#
# # this will track coordinate on terminal
# def get_coordinate_mouse_clic(lat, lng):
#     print(lat, lng)
#
# turtle.onscreenclick(get_coordinate_mouse_clic)
#
# turtle.mainloop()
