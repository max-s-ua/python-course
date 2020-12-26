from PySide2.QtWidgets import QLineEdit, QLabel
from PySide2.QtCore import Slot
from math import sin, cos, exp, sqrt

class QtCalculator():
    def __init__(self, bufferLabel, displayText):
        self.bufferLabel = bufferLabel
        self.displayText = displayText
        self.displayText.setText('0')
        self.operator = ''
        self.buffer = 0

    def toCalc(self):        
        value = float(self.displayText.text())
        result = 0
        if self.operator == '+': result = self.buffer + value
        elif self.operator == '-': result = self.buffer - value
        elif self.operator == '*': result = self.buffer * value
        elif self.operator == '/': result = self.buffer / value
        elif self.operator == '%': result = self.buffer / value * 100
        else: result = 0
        self.operator = ''
        self.buffer = 0
        self.bufferLabel.setText('')
        self.displayText.setText('{}'.format(result))

    
    @Slot()
    def digit_on_click(self, button):
        if self.displayText.text() == '0': self.displayText.setText('')
        text = self.displayText.text()
        text = text + button.text()
        self.displayText.setText(text)

    @Slot()
    def dot_on_click(self):
        text = self.displayText.text()
        if '.' not in text:
            if text == '':
                text = '0.'
            else:
                text = text + '.'
            self.displayText.setText(text)

    @Slot()
    def binOp_on_click(self, button):
        self.operator = button.text()
        self.buffer = float(self.displayText.text())
        self.bufferLabel.setText('{} {}'.format(self.buffer, self.operator))
        self.displayText.setText('0')
        

    @Slot()
    def equal_on_click(self):
        self.toCalc()
        
    @Slot()
    def pi_on_click(self):
        self.displayText.setText('3.1415')

    @Slot()
    def func_on_click(self, button):
        arg = float(self.displayText.text())
        result = 0
        fnc = button.text()
        if fnc == 'sin': result = sin(arg)
        elif fnc == 'cos': result = cos(arg)
        elif fnc == 'exp': result = exp(arg)
        elif fnc == 'sqrt': result = sqrt(arg)
        elif fnc == '^2': result = arg*arg
        else: return

        self.displayText.setText('{}'.format(result))
        self.bufferLabel.setText('{}({})='.format(fnc,arg))

    @Slot()
    def ac_on_click(self):
        self.bufferLabel.setText('')
        self.displayText.setText('0')
        self.buffer = 0
        self.operator = ''

    @Slot()
    def bs_on_click(self):
        txt = self.displayText.text()
        if len(txt) <= 1: 
            self.displayText.setText('0')
            return
        self.displayText.setText(txt[:-1])
