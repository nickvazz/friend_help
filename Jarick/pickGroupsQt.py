import sys
import PyQt5
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QCheckBox, QScrollArea)

from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl



class pickGroupsToPost(QDialog):
    def __init__(self, groups):
        super(pickGroupsToPost, self).__init__()
        self.createFormGroupBox(groups)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()

        scroll = QScrollArea()
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.formGroupBox)

        mainLayout.addWidget(scroll)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)
        self.setWindowTitle("Facebook Box Group Posting")



    def createFormGroupBox(self, groups):
        self.formGroupBox = QGroupBox("Click groups to post to.")
        # self.formGroupBox.setFixedSize(100,10*len(list(groups)))
        # print (list(groups))
        layout = QFormLayout()

        self.checkboxes = []
        self.posts = []
        for idx, (group, url) in enumerate(groups):
            cbox = QCheckBox()
            label = QLabel()
            post = QTextEdit('Enter Post Here')

            label.setText(f' <a href=\"{url}\">{group[0]} </a>')
            label.linkActivated.connect(self.link)
            label.setOpenExternalLinks(True)
            layout.addRow(label)
            layout.addRow(post, cbox)

            self.checkboxes.append(cbox)
            self.posts.append(post)

        # self.formGroupBox.setFixedSize(self.formGroupBox.size())
        self.formGroupBox.setLayout(layout)



    def link(self, linkStr):
        QDesktopServices.openURL(QUrl(linkStr))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pickGroups = pickGroupsToPost(zip('abc'*10,'xyz'*10))

    sys.exit(pickGroups.exec_())
