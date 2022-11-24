import numpy as np
import math as m
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    """This class builds the GUI.

    Args:
        QtWidgets (module): The imported module that we need to make the GUI.
    """
    pass

    def __init__(self):
        """Create the widgets.
        """    
        super().__init__()

        # Create the central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # vertical layout
        self.vbox = QtWidgets.QVBoxLayout(central_widget)

        #  make the plot widget and add to vertical layout
        self.plot_widget = pg.PlotWidget()

        self.vbox.addWidget(self.plot_widget)

        # horizontal layout
        hbox = QtWidgets.QHBoxLayout()

        # add horizontal to vertical
        self.vbox.addLayout(hbox)

        # make the horizontal layout later used for the desired parameter change
        self.hbox_confirm = QtWidgets.QHBoxLayout()

        # make a start, stop, numpoints button
        self.start_button = QtWidgets.QSpinBox()
        hbox.addWidget(self.start_button)

        self.stop_button = QtWidgets.QSpinBox()
        hbox.addWidget(self.stop_button)

        self.numpoints_button = QtWidgets.QSpinBox()
        hbox.addWidget(self.numpoints_button)

        # standaardwaarden voor de parameters
        self.start_button.setValue(0)
        self.stop_button.setValue(2 * m.pi)
        self.numpoints_button.setValue(100)

        # give boundaries
        self.start_button.setMinimum(0)
        self.start_button.setMaximum(99)
        self.stop_button.setMinimum(1)
        self.stop_button.setMaximum(100)
        self.numpoints_button.setMinimum(10)
        self.numpoints_button.setMaximum(200)

        # make sure the start value is lower than the stop value and perform the initial plot
        if self.start_button.value() < self.stop_button.value():
            x = np.linspace(self.start_button.value(), self.stop_button.value(), self.numpoints_button.value())
            self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "k", "width": 5})
            self.plot_widget.setLabel("left", "sin(x)")
            self.plot_widget.setLabel("bottom", "x [radians]")

        # Make sure the buttons actually do something
        self.start_button.valueChanged.connect(self.plot_changed)
        self.stop_button.valueChanged.connect(self.plot_changed)
        self.numpoints_button.valueChanged.connect(self.plot_changed)

    @Slot()

    def plot_changed(self):
        """Everytime the value changes, the plot will be performed again.
        """        

        # make sure the start value is lower than the stop value and perform the changed plot
        if self.start_button.value() < self.stop_button.value():
            self.plot_widget.clear() 
            x = np.linspace(self.start_button.value(), self.stop_button.value(), self.numpoints_button.value())
            self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "k", "width": 5})
            self.plot_widget.setLabel("left", "sin(x)")
            self.plot_widget.setLabel("bottom", "x [radians]")
            self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    UserInterface
    main()