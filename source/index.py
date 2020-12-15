from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon,QApplication
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from os import path
import sys
from main import Ui_MainWindow
import subprocess
from subprocess import PIPE, run


class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Window()
        self.Handel_Buttons()

    def Handel_Window(self):
        self.setFixedSize(721, 480)
        self.setWindowTitle('System Helper Tool')
        self.setWindowIcon(QtGui.QIcon('img/security-system.ico'))
    
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Commands_Run)
        self.pushButton_2.clicked.connect(self.Clear_Error_and_Results_Sections)
        
    def Clear_Error_and_Results_Sections(self):
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')

    def Commands_Run(self):
        WorkLocation = None
        Command = self.lineEdit_2.text()

        if self.checkBox.isChecked() == True:
            WorkLocation = self.lineEdit.text()
        
        result = run(Command,shell=True,cwd=WorkLocation,stdout=PIPE, stderr=PIPE)
        
        
        str_stdout = str(result.stdout)
        split_it1_str_stdout = str_stdout.split('\'')
        split_it2_str_stdout = split_it1_str_stdout[1].split('\\')
        stdout_final_result = split_it2_str_stdout[0]
        

        str_sterr = str(result.stderr)
        split_it1_str_sterr = str_sterr.split('\'')
        split_it2_str_sterr = split_it1_str_sterr[1].split('\\')
        sterr_final_result = split_it2_str_sterr[0]
        

        self.lineEdit_3.setText(stdout_final_result)
        self.lineEdit_4.setText(sterr_final_result)

        

        

        
            

        
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp() # نأخذ نسخة من الclass الي نقدر ننشأ منه window
    window.show() # لإظهار ال window
    app.exec_() # هذا عبارة عن loop يخلي ال window ظاهرة دائما في الشاشة، إذا لم تكن هذه ال loop رح تظهر ال window و تختفي على طول.


if __name__ == '__main__': # في هذا السطر إحنا بنحدد و نختار السطر الي رح يبدأ منه الكود و في هاذي الأسطر إخترنا أنه يبدأ من ال function 'main'
    main()