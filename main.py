from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setFixedSize(600, 600)
window.setWindowTitle("Tic Tac Toe")
stack = QStackedWidget()

import algorithm
import gui
import end_game_gui

stack.addWidget(gui.widget)
stack.addWidget(end_game_gui.widget2)

window.setCentralWidget(stack)
window.show()

def window_1():
    stack.setCurrentIndex(0)

def window_2():
    stack.setCurrentIndex(1)

window_1()

x = algorithm.tic_tac_toe()
current_symbol = 'X'

def toggle_symbol():
    global current_symbol
    if current_symbol == 'X':
        current_symbol = 'O'
    else:
        current_symbol = 'X'

def button_pressed(button):
    button.setText(current_symbol)
    button.setDisabled(True)
    toggle_symbol()
    status = x.check_win()
    if (status==10):
        window_2()
        end_game_gui.set_message("X Won!")
    elif (status==-10):
        window_2()
        end_game_gui.set_message("O Won!")
    elif (status==1):
        window_2()
        end_game_gui.set_message("Tie!")

def button_pressed_0():
    x.move(current_symbol, 0)
    button_pressed(gui.b0)

def button_pressed_1():
    x.move(current_symbol, 1)
    button_pressed(gui.b1)

def button_pressed_2():
    x.move(current_symbol, 2)
    button_pressed(gui.b2)

def button_pressed_3():
    x.move(current_symbol, 3)
    button_pressed(gui.b3)

def button_pressed_4():
    x.move(current_symbol, 4)
    button_pressed(gui.b4)

def button_pressed_5():
    x.move(current_symbol, 5)
    button_pressed(gui.b5)

def button_pressed_6():
    x.move(current_symbol, 6)
    button_pressed(gui.b6)

def button_pressed_7():
    x.move(current_symbol, 7)
    button_pressed(gui.b7)

def button_pressed_8():
    x.move(current_symbol, 8)
    button_pressed(gui.b8)

gui.b0.clicked.connect(button_pressed_0)
gui.b1.clicked.connect(button_pressed_1)
gui.b2.clicked.connect(button_pressed_2)
gui.b3.clicked.connect(button_pressed_3)
gui.b4.clicked.connect(button_pressed_4)
gui.b5.clicked.connect(button_pressed_5)
gui.b6.clicked.connect(button_pressed_6)
gui.b7.clicked.connect(button_pressed_7)
gui.b8.clicked.connect(button_pressed_8)

app.exec_()