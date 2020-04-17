"""
TODO : There are also some arithmetic unimplemented, they are:
    - Rad
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from src.myCalcUI import Ui_MainWindow
import functools, random
from calculator import calculate
import qdarkstyle
import qtmodern.styles
import qtmodern.windows
from utils import wrapper_inverse, History
from PyQt5.QtCore import pyqtSlot


class MyCalcWindow(Ui_MainWindow, QMainWindow):
    numbers = {str(i): str(i) for i in range(10)}
    science_numbers = {'pi': 'π', 'e': 'e'}
    number_keys = dict(numbers.items() | science_numbers.items())

    operators = {"plus": "+", "sub": "-", "mul": "×", "div": "÷",
                 "point": ".", "square": "²", "exp": "exp(", "sqrt": "√(",
                 "log": "log(", "ln": "ln(", "leftpart": "(", "rightpart": ")",
                 "sin": "sin(", "cos": "cos(", "tan": "tan(", "power": "^(",
                 "factorial": "!", }

    operations = {"DEL": "DEL", "AC": "AC",
                  "equal": "equal", "rand": "rand",
                  "inverse": "inverse", "percent": "percent", }

    def __init__(self):
        super(MyCalcWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # lock the window size
        ##################################
        self.PRECISION = self.verticalSlider.value()
        self.history = ""
        self._history = History(parent=self)
        self.compute_times = 0
        self.lcdNumber.display(self.PRECISION)
        self.connecter()
        self.show()
        self.press_AC()

    def keyPressEvent(self, event):
        # 这里event.key（）显示的是按键的编码
        # print("按下：" + str(event.key()))

        if QApplication.keyboardModifiers() == Qt.ShiftModifier:

            if event.key() == Qt.Key_J:
                print("press J")
                self._history.next()
            elif event.key() == Qt.Key_K:
                print("press K")
                self._history.last()

    def update_history(self, equation):
        self.compute_times += 1
        if self.history == "":
            self.history += "[{}] : {}".format(self.compute_times, equation)
        else:
            self.history = "\n[{}] : {}".format(self.compute_times, equation)
        self.textBrowser.insertPlainText(self.history)
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def valueChanged(self):
        self.PRECISION = self.verticalSlider.value()
        self.lcdNumber.display(self.PRECISION)

    def connect(self, keys_dict, use_func=False, set_shortcut=False):
        """ Use specific key-value to connect button clicked response
        :param keys_dict:
        :param use_func: if True, use `press_value` function
        """
        for button_name, button_text in keys_dict.items():
            btn = self.__dict__['pushButton_' + button_name]
            if use_func:
                func = eval("self.press_" + button_name)
                btn.clicked.connect(func)
            else:
                btn.clicked.connect(functools.partial(self.press, button_text))

    def set_shortcut(self, buttons_dict):
        for button_name, button_text in buttons_dict.items():
            btn = self.__dict__['pushButton_' + button_name]
            btn.setShortcut(button_name[0])

    def connecter(self):
        # 1. numbers

        self.connect(self.number_keys)
        self.set_shortcut(self.number_keys)
        # 2. operators

        self.connect(self.operators)
        self.pushButton_mul.setShortcut("*")
        self.pushButton_div.setShortcut("/")
        self.pushButton_plus.setShortcut("+")
        self.pushButton_sub.setShortcut("-")
        self.pushButton_leftpart.setShortcut("(")
        self.pushButton_rightpart.setShortcut(")")
        self.pushButton_power.setShortcut("^")
        self.pushButton_factorial.setShortcut("!")
        self.pushButton_point.setShortcut(".")
        self.pushButton_sin.setShortcut("S")
        self.pushButton_cos.setShortcut("C")
        self.pushButton_tan.setShortcut("T")
        self.pushButton_sqrt.setShortcut("shift+^")
        self.pushButton_square.setShortcut("shift+2")
        self.pushButton_log.setShortcut("l")
        self.pushButton_ln.setShortcut("n")
        self.pushButton_rand.setShortcut("r")
        self.pushButton_inverse.setShortcut("shift+/")
        # 3. operations

        self.connect(self.operations, use_func=True)
        self.pushButton_equal.setShortcut("return")
        self.pushButton_DEL.setShortcut("backspace")
        self.pushButton_AC.setShortcut("shift+l")
        # 4. other functions
        self.verticalSlider.valueChanged.connect(self.valueChanged)

    def press_inverse(self):
        self.press_equal(reciprocal=True, percent=False)

    def press_percent(self):
        self.press_equal(reciprocal=False, percent=True)

    def press_rand(self):
        self.lineEdit.insert(str(random.random()))

    def press(self, button_key):
        self.lineEdit.insert(button_key)

    def press_DEL(self):
        self.lineEdit.backspace()

    def press_AC(self):
        self.lineEdit.setText("")

    def press_equal(self, reciprocal=False, percent=False):
        text = self.lineEdit.text()
        if reciprocal:
            text = wrapper_inverse(text)
        try:
            result, equation = calculate(text, self.PRECISION, percent)

            self.lineEdit.setText(str(result))
            self.update_history(equation)
            self._history.append(text)
        except Exception as e:
            self.lineEdit.setText(str(e))


def main():
    app = QApplication(sys.argv)
    Calc = MyCalcWindow()
    # METHOD1 : import qdarkstyle
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    #qtmodern.styles.dark(app)
    #mw = qtmodern.windows.ModernWindow(Calc)
    #mw.show()
    Calc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
