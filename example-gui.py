import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

class UserInterface(QtWidgets.QMainWindow):
    pass
    
    def __init__(self):
        super().__init__()

        # Create the central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # vertical layout
        vbox = QtWidgets.QVBoxLayout(central_widget)
        
        # Make a textbox
        self.textedit = QtWidgets.QTextEdit()

        # Add the textbox to the vertical layout
        vbox.addWidget(self.textedit)

        # horizontal layout
        hbox = QtWidgets.QHBoxLayout()

        # add horizontal to vertical
        vbox.addLayout(hbox)

        # another horziontal layout added to vertical
        hbox_2 = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox_2)

        # make a clear button
        clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(clear_button)

        #  make an addtext button
        add_button = QtWidgets.QPushButton("Add text")
        hbox.addWidget(add_button)

        # make hello button
        hello_button = QtWidgets.QPushButton("Hello, world")
        hbox.addWidget(hello_button)

        # make quit button
        quit_button = QtWidgets.QPushButton("Quit")
        hbox_2.addWidget(quit_button)

        # make the buttons actually do something
        clear_button.clicked.connect(self.textedit.clear)
        add_button.clicked.connect(self.add_button_clicked)
        hello_button.clicked.connect(self.hello_button_clicked)
        quit_button.clicked.connect(self.quit_button_clicked)

    @Slot()
    def add_button_clicked(self):
        self.textedit.append("You clicked me.")

    def hello_button_clicked(self):
        self.textedit.append("Hello, world")

    def quit_button_clicked(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    UserInterface
    main()
    

