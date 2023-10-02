from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QFont

layout = QGridLayout()
widget = QWidget()

b0 = QPushButton()
b0.setFixedSize(180,180)
b1 = QPushButton()
b1.setFixedSize(180,180)
b2 = QPushButton()
b2.setFixedSize(180,180)
b3 = QPushButton()
b3.setFixedSize(180,180)
b4 = QPushButton()
b4.setFixedSize(180,180)
b5 = QPushButton()
b5.setFixedSize(180,180)
b6 = QPushButton()
b6.setFixedSize(180,180)
b7 = QPushButton()
b7.setFixedSize(180,180)
b8 = QPushButton()
b8.setFixedSize(180,180)

layout.addWidget(b0,0,0)
layout.addWidget(b1,0,1)
layout.addWidget(b2,0,2)
layout.addWidget(b3,1,0)
layout.addWidget(b4,1,1)
layout.addWidget(b5,1,2)
layout.addWidget(b6,2,0)
layout.addWidget(b7,2,1)
layout.addWidget(b8,2,2)

font = QFont()
font.setPointSize(50)
b0.setFont(font)
b1.setFont(font)
b2.setFont(font)
b3.setFont(font)
b4.setFont(font)
b5.setFont(font)
b6.setFont(font)
b7.setFont(font)
b8.setFont(font)

widget.setLayout(layout)