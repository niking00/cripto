from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QIntValidator
from dialog import Ui_Dialog
from datetime import datetime
from sys import argv, exit
from lib import cipher, decipher

class DialogApp(QMainWindow):
    def __init__(self):
        super(DialogApp, self).__init__()
        self.resize(650, 330)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.pIntValidator = QIntValidator(self)
        self.pIntValidator.setRange(1, 9999)

        self.w = self.size().width()
        self.h = self.size().height()

        self.ui.ButCipher.clicked.connect(self.but_cipher)
        self.ui.ButDecipher.clicked.connect(self.but_decipher)
        self.ui.downloadFile.clicked.connect(self.but_download)
        self.ui.loadFile.clicked.connect(self.but_load)
        self.ui.lineEdit.setValidator(self.pIntValidator)
        self.ui.lineEdit.setPlaceholderText("код")

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()

        koefW = width / self.w
        koefH = height / self.h

        self.ui.ButCipher.setGeometry(round(270 * koefW), round(30 * koefH), round(110 * koefW), round(80 * koefH))
        self.ui.ButDecipher.setGeometry(round(270 * koefW), round(170 * koefH), round(110 * koefW), round(80 * koefH))
        self.ui.downloadFile.setGeometry(round(407 * koefW), round(260 * koefH), round(190 * koefW), round(40 * koefH))
        self.ui.loadFile.setGeometry(round(57 * koefW), round(260 * koefH), round(190 * koefW), round(40 * koefH))
        self.ui.textEdit.setGeometry(round(40 * koefW), round(30 * koefH), round(220 * koefW), round(220 * koefH))
        self.ui.textEdit_2.setGeometry(round(390 * koefW), round(30 * koefH), round(220 * koefW), round(220 * koefH))
        self.ui.lineEdit.setGeometry(round(271 * koefW), round(115 * koefH), round(108 * koefW), round(50 * koefH))

    def but_cipher(self):
        code = self.ui.lineEdit.text()
        if code != '' and len(code) == 4:
            text = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(cipher(text, int(code)))
            self.ui.lineEdit.setText('')
        else:
            self.ui.textEdit_2.setText('Введите четырёхзначный код')

    def but_decipher(self):
        code = self.ui.lineEdit.text()
        if code != '' and len(code) == 4:
            text = self.ui.textEdit.toPlainText()
            self.ui.textEdit_2.setText(decipher(text, int(code)))
            self.ui.lineEdit.setText('')
        else:
            self.ui.textEdit_2.setText('Введите четырёхзначный код')

    def but_load(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', "", "*.txt")
            with open(file_name, 'r', encoding='utf-8') as f:
                txt = f.read()
                self.ui.textEdit.setText(txt)
        except Exception:
            pass

    def but_download(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        name = dirlist + '/' + datetime.today().strftime("%d-%m-%Y_%H-%M-%S") + '.txt'
        with open(name, 'w', encoding='utf-8') as f:
            f.write(self.ui.textEdit_2.toPlainText())

if __name__ == '__main__':
    app = QApplication(argv)
    application = DialogApp()
    application.show()
    exit(app.exec())