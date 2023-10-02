from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

layout = QGridLayout()

def set_message(s):
    label.setText(s)

widget2 = QWidget()
label = QLabel("", widget2)

layout.addWidget(label)
label.setAlignment(Qt.AlignCenter)

font = QFont()
font.setPointSize(50)
label.setFont(font)

widget2.setLayout(layout)

