import sys
import webbrowser

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon, QDesktopServices

import test


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        # self.statusBar()

    def initUI(self):
        self.window()
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()
        # self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,
                                                "QFileDialog.getOpenFileNames()",
                                                "",
                                                "All Files (*);;Python Files (*.py)",
                                                options=options)
        if files:
            print(files)
            test.main(files)
            # self.completed = 0
            # while self.completed < 100:
            #     self.completed += 0.0001
            #     self.progress.setValue(self.completed)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def window(self):
        app = QApplication(sys.argv)
        widget = QWidget()

        button1 = QPushButton(widget)
        button1.setText("Button")
        button1.move(64, 32)
        button1.clicked.connect(self.openFileNamesDialog)

        button2 = QPushButton(widget)
        button2.setText("Login")
        button2.move(64, 64)
        button2.clicked.connect(self.auth)

        widget.setGeometry(50, 50, 320, 200)
        widget.setWindowTitle("PyQt5 Button Click Example")
        widget.show()
        sys.exit(app.exec_())

    def auth(self):
        url = "https://oauth.yandex.ru/authorize?response_type=token&client_id=f93c10ef8e2f42708d0f186eaf4997eb"
        QDesktopServices.openUrl(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
