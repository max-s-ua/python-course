import sys
from PySide2.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QLabel
)
from PySide2.QtCore import Qt

from QtCalculator import QtCalculator

class Qt_Calculator_Gui(QWidget):

    def __init__(self):
        super().__init__()      
        self.initGUI()
        self.calculator = QtCalculator(self.numPanel, self.numDisplay)
        self.initWidgets()      
        
        self.show()

    
    def initGUI(self):        
        self.setFixedWidth(320)
        self.setFixedHeight(200)
        self.setWindowTitle('QT Calculator')
        self.numPanel = QLabel('')
        self.numPanel.setAlignment(Qt.AlignRight)
        self.numDisplay = QLineEdit()
        self.numDisplay.setAlignment(Qt.AlignRight)
        self.numDisplay.setReadOnly(True)
                

    def initWidgets(self):
        button1 = QPushButton('1'); button1.clicked.connect(lambda: self.calculator.digit_on_click(button1)) 
        button2 = QPushButton('2'); button2.clicked.connect(lambda: self.calculator.digit_on_click(button2)) 
        button3 = QPushButton('3'); button3.clicked.connect(lambda: self.calculator.digit_on_click(button3)) 
        button4 = QPushButton('4'); button4.clicked.connect(lambda: self.calculator.digit_on_click(button4)) 
        button5 = QPushButton('5'); button5.clicked.connect(lambda: self.calculator.digit_on_click(button5)) 
        button6 = QPushButton('6'); button6.clicked.connect(lambda: self.calculator.digit_on_click(button6)) 
        button7 = QPushButton('7'); button7.clicked.connect(lambda: self.calculator.digit_on_click(button7)) 
        button8 = QPushButton('8'); button8.clicked.connect(lambda: self.calculator.digit_on_click(button8)) 
        button9 = QPushButton('9'); button9.clicked.connect(lambda: self.calculator.digit_on_click(button9)) 
        button0 = QPushButton('0'); button0.clicked.connect(lambda: self.calculator.digit_on_click(button0)) 
        button_Plus = QPushButton('+'); button_Plus.clicked.connect(lambda: self.calculator.binOp_on_click(button_Plus))
        button_Minus = QPushButton('-'); button_Minus.clicked.connect(lambda: self.calculator.binOp_on_click(button_Minus))
        button_Product = QPushButton('*'); button_Product.clicked.connect(lambda: self.calculator.binOp_on_click(button_Product))
        button_Divide = QPushButton('/'); button_Divide.clicked.connect(lambda: self.calculator.binOp_on_click(button_Divide))
        button_Pi = QPushButton('pi'); button_Pi.clicked.connect(self.calculator.pi_on_click)
        button_Percent = QPushButton('%'); button_Percent.clicked.connect(lambda: self.calculator.binOp_on_click(button_Percent))
        button_Sqrt = QPushButton('sqrt'); button_Sqrt.clicked.connect(lambda: self.calculator.func_on_click(button_Sqrt))
        button_Cos = QPushButton('cos'); button_Cos.clicked.connect(lambda: self.calculator.func_on_click(button_Cos))
        button_AC = QPushButton('AC'); button_AC.clicked.connect(self.calculator.ac_on_click)
        button_Dot = QPushButton('.'); button_Dot.clicked.connect(self.calculator.dot_on_click)
        button_Equal = QPushButton('='); button_Equal.clicked.connect(self.calculator.equal_on_click)
        button_Backsp = QPushButton('<-'); button_Backsp.clicked.connect(self.calculator.bs_on_click)
        button_Sin = QPushButton('sin'); button_Sin.clicked.connect(lambda: self.calculator.func_on_click(button_Sin))
        button_Exp = QPushButton('exp'); button_Exp.clicked.connect(lambda: self.calculator.func_on_click(button_Exp))
        button_Pow2 = QPushButton('^2'); button_Pow2.clicked.connect(lambda: self.calculator.func_on_click(button_Pow2))

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.numPanel)
        vlayout.addWidget(self.numDisplay)
        
        gridLayout = QGridLayout()
        
        gridLayout.addWidget(button1, 0, 0)
        gridLayout.addWidget(button2, 0, 1)
        gridLayout.addWidget(button3, 0, 2)
        gridLayout.addWidget(button_Plus, 0, 3)
        gridLayout.addWidget(button_Pi, 0, 4)
        gridLayout.addWidget(button_Backsp, 0, 5)
        gridLayout.addWidget(button4, 1, 0)
        gridLayout.addWidget(button5, 1, 1)
        gridLayout.addWidget(button6, 1, 2)
        gridLayout.addWidget(button_Minus, 1, 3)
        gridLayout.addWidget(button_Percent, 1, 4)
        gridLayout.addWidget(button_Sqrt, 1, 5)
        gridLayout.addWidget(button7, 2, 0)
        gridLayout.addWidget(button8, 2, 1)
        gridLayout.addWidget(button9, 2, 2)
        gridLayout.addWidget(button_Product, 2, 3)
        gridLayout.addWidget(button_Sin, 2, 4)
        gridLayout.addWidget(button_Exp, 2, 5)
        gridLayout.addWidget(button_AC, 3, 0)
        gridLayout.addWidget(button0, 3, 1)
        gridLayout.addWidget(button_Dot, 3, 2)
        gridLayout.addWidget(button_Divide, 3, 3)
        gridLayout.addWidget(button_Cos, 3, 4)
        gridLayout.addWidget(button_Pow2, 3, 5)
        
        vlayout.addLayout(gridLayout)
        vlayout.addWidget(button_Equal)
        self.setLayout(vlayout)
      


    #@Slot()
    #def on_click(self):
    #    print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Qt_Calculator_Gui()
    sys.exit(app.exec_())