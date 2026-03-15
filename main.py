import sys
import temp
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtWidgets import QVBoxLayout, QProgressBar, QPushButton
from PyQt6.QtCore import QTimer


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("CPU Temps")
        self.setGeometry(100, 100, 320, 210)

        core_number = temp.core_number()
        self.core_list = []
        for i in range(core_number):
            self.core_list.append(i)

        # creating labels and setting text
        self.label_list = [QLabel() for i in self.core_list]
        for object in self.label_list:
            object.setText("Core " + str(self.label_list.index(object)))

        # defining quit button
        btn_exit = QPushButton("Quit")
        btn_exit.clicked.connect(app.quit)

        # creating and initialising progressbars
        self.cores = [QProgressBar() for i in self.core_list]
        for core in self.cores:
            core.setRange(0, 100)

        combined_list = zip(self.label_list, self.cores)
        print(combined_list)

        # layout of widgets
        layout = QVBoxLayout()
        for item in combined_list:
            layout.addWidget(item[0])
            layout.addWidget(item[1])
        layout.addWidget(btn_exit)
        self.setLayout(layout)
        self.show()

        # repeating call to temperature sensors
        self.core_update = QTimer()
        self.core_update.timeout.connect(self.core_query)
        self.core_update.start()

    def core_query(self):
        core_temps = temp.get_temps()
        for i in range(len(self.cores)):
            self.cores[i].setValue(int(core_temps[i]))
        self.set_caption()

    def set_caption(self):
        for core in self.cores:
            core.setFormat(str(core.value()) + "°C")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
