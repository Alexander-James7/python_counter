#Created by: Alexander James
#Date: 9/27/2022
#This code sest the variable value to 0 on start

Counter = 0
Counter = 0


# Created by: Alex J
#Date: 9/27/2022
#This code decreases the counter variable by 1

def on_button_pressed_a():
    global counter
    counter += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

#Created by: Alex J
#Date: 9/27/2022
#This code decreaes the variable by 1

def on_button_pressed_b():
    global counter
    counter += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

#Created by: Alex J
#Date: 9/27/2022
#This code displays the value of the variable on the LED screen

def on_button_pressed_ab():
    basic.show_number(counter)
input.on_button_pressed(Button.AB, on_button_pressed_ab)


