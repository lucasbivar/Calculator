import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(350, 500)
        self.setStyleSheet("background-color: black;")
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            ' * {background: black; color: white; font-size: 45px; border: 0;}'
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(
            QPushButton('AC'), 1, 0, 1, 1,
            lambda: self.display.setText(''),
            style='functionalities'
        )
        self.add_btn(
            QPushButton('Del'), 1, 1, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            style='functionalities'
        )
        self.add_btn(
            QPushButton('**'), 1, 2, 1, 1)
        self.add_btn(QPushButton('/'), 1, 3, 1, 1, style='operator')

        self.add_btn(QPushButton('7'), 2, 0, 1, 1, style='number')
        self.add_btn(QPushButton('8'), 2, 1, 1, 1, style='number')
        self.add_btn(QPushButton('9'), 2, 2, 1, 1, style='number')
        self.add_btn(QPushButton('*'), 2, 3, 1, 1, style='operator')

        self.add_btn(QPushButton('4'), 3, 0, 1, 1, style='number')
        self.add_btn(QPushButton('5'), 3, 1, 1, 1, style='number')
        self.add_btn(QPushButton('6'), 3, 2, 1, 1, style='number')
        self.add_btn(QPushButton('-'), 3, 3, 1, 1, style='operator')

        self.add_btn(QPushButton('1'), 4, 0, 1, 1, style='number')
        self.add_btn(QPushButton('2'), 4, 1, 1, 1, style='number')
        self.add_btn(QPushButton('3'), 4, 2, 1, 1, style='number')
        self.add_btn(QPushButton('+'), 4, 3, 1, 1, style='operator')

        self.add_btn(QPushButton('0'), 5, 0, 1, 2, style='number')
        self.add_btn(QPushButton('.'), 5, 2, 1, 1, style='number')
        self.add_btn(
            QPushButton('='), 5, 3, 1, 1,
            self.eval_equal,
            style='operador'
                     )

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style == 'operator':
            btn.setStyleSheet('background: #fd9701; color: #ffffff; font-size: 20px; border-radius: 30px;')
        elif style == 'functionalities':
            btn.setStyleSheet('background:#a4a4a4; color:#000000; font-weight:300; font-size:20px; border-radius:30px;')
        elif style == 'number':
            btn.setStyleSheet('background: #333333; color: #ffffff; font-size: 20px; border-radius: 30px;')
        else:
            btn.setStyleSheet('background: #a4a4a4; color: #000000; font-size: 20px; border-radius: 30px;')

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_equal(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Invalid.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()