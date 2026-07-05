import sys
import psutil
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtWidgets import QVBoxLayout, QProgressBar, QPushButton
from PyQt6.QtCore import QTimer

# This is a testing version only, it returns dummy temperatures for testing with different core numbers. See line 52.

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("CPU Temps")
        self.setGeometry(100, 100, 320, 210)

        self.core_number = len(self.get_temps())

        # creating labels and setting text
        self.label_list = [QLabel() for i in range(self.core_number)]
        for i, label in enumerate(self.label_list):
            label.setText("Core " + str(i))

        # defining quit button
        btn_exit = QPushButton("Quit")
        btn_exit.clicked.connect(app.quit)

        # creating and initialising progressbars
        self.cores = [QProgressBar() for i in range(self.core_number)]
        for core in self.cores:
            core.setRange(0, 100)

        combined_list = zip(self.label_list, self.cores)

        # layout of widgets
        layout = QVBoxLayout()
        for label, core in combined_list:
            layout.addWidget(label)
            layout.addWidget(core)
        layout.addWidget(btn_exit)
        self.setLayout(layout)
        self.show()

        # repeating call to temperature sensors
        self.core_update = QTimer()
        self.core_update.timeout.connect(self.core_query)
        self.core_update.start(1000)

    def get_temps(self):
        
        # adjust this variable to adjust cores for testing
        core_num = 2

        core_list = []
        for i in range(core_num):
            core_list.append(50 + random.randint(-5, 5))
        return core_list

    def core_query(self):
        core_temps = self.get_temps()
        for i, core in enumerate(self.cores):
            core.setValue(int(core_temps[i]))
        self.set_caption()

    def set_caption(self):
        for core in self.cores:
            core.setFormat(str(core.value()) + "°C")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
