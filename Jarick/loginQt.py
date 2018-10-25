import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QDialogButtonBox, QDialog
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QFormLayout, QGroupBox, QCheckBox
from PyQt5.QtCore import QSize

class loginCredentials(QDialog):
    def createLoginGroupBox(self):
        self.formGroupBox = QGroupBox("Login to Facebook Group Post Bot")
        layout = QFormLayout()

        login = QLineEdit()
        layout.addRow("Facebook Login Email", login)

        pw = QLineEdit()
        pw.setEchoMode(QLineEdit.Password)
        layout.addRow("Password", pw)

        self.load_data = QCheckBox()
        layout.addRow("Load Data?", self.load_data)

        self.login_creds = [login, pw]
        self.formGroupBox.setLayout(layout)

    def __init__(self):
        super(loginCredentials, self).__init__()
        self.createLoginGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Facebook Box Group Posting")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = loginCredentials()
    result = login.exec_()
    sys.exit(result)
