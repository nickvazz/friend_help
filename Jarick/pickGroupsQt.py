import sys
import PyQt5
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QCheckBox, QScrollArea)

from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
import numpy as np

class pickGroupsToPost(QDialog):
    def __init__(self, groups, urls, load_data=False, posts=[]):
        super(pickGroupsToPost, self).__init__()
        self.groups = groups
        self.urls = urls
        self.posts = posts
        self.load_data = load_data
        self.createFormGroupBox(self.groups, self.urls, self.load_data, self.posts)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        scroll = QScrollArea()
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.formGroupBox)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(scroll)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)
        self.setWindowTitle("Facebook Box Group Posting")

    def createFormGroupBox(self, groups, urls, load_data=False, posts=[]):

        self.formGroupBox = QGroupBox("Click groups to post to.")
        layout = QFormLayout()

        self.checkboxes = []
        new_posts = []
        if not load_data:
            groups = [item for sublist in groups for item in sublist]
        print (groups)
        print (urls)

        for idx, (group, url) in enumerate(zip(groups, urls)):
            cbox = QCheckBox()
            label = QLabel()


            if load_data:
                post = QTextEdit(self.posts[idx])
            else:
                post = QTextEdit('Enter Post Here')


            label.setText(f' <a href=\"{url}\">{group} </a>')
            label.linkActivated.connect(self.link)
            label.setOpenExternalLinks(True)
            layout.addRow(label)
            layout.addRow(post, cbox)

            self.checkboxes.append(cbox)
            new_posts.append(post)

        self.formGroupBox.setLayout(layout)
        self.posts = new_posts

    def link(self, linkStr):
        QDesktopServices.openURL(QUrl(linkStr))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pickGroups = pickGroupsToPost(zip('abc'*10,'xyz'*10))

    sys.exit(pickGroups.exec_())
