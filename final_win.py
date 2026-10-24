from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self): 
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self): 
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.btn_restart = QPushButton("Retake Test")

        self.layout_line = QVBoxLayout()

        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_restart, alignment = Qt.AlignCenter)

        self.setLayout(self.layout_line)

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "there is no data for this age"

        self.index = (4 * (self.exp.t1 + self.exp.t2 + self.exp.t3) - 200) / 10

        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif 17 <= self.index < 21:
                return txt_res2
            elif 12 <= self.index < 17:
                return txt_res3
            elif 6.5 <= self.index < 12:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif 15.5 <= self.index < 19.5:
                return txt_res2
            elif 10.5 <= self.index < 15.5:
                return txt_res3
            elif 5 <= self.index < 10.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif 14 <= self.index < 18:
                return txt_res2
            elif 9 <= self.index < 14:
                return txt_res3
            elif 3.5 <= self.index < 9:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif 12.5 <= self.index < 16.5:
                return txt_res2
            elif 7.5 <= self.index < 12.5:
                return txt_res3
            elif 2 <= self.index < 7.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif 11 <= self.index < 15:
                return txt_res2
            elif 6 <= self.index < 11:
                return txt_res3
            elif 0.5 <= self.index < 6:
                return txt_res4
            else:
                return txt_res5

    def restart_click(self):
        from second_win import TestWin
        self.hide()
        self.tw = TestWin()

    def connects(self):
        self.btn_restart.clicked.connect(self.restart_click)