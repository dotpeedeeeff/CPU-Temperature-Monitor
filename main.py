import sys, temp
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar, QPushButton
from PyQt6.QtCore import QTimer


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("CPU Temps")
        self.setGeometry(100, 100, 320, 210)

        label_0 = QLabel("Core 0")
        label_1 = QLabel("Core 1")
        label_2 = QLabel("Core 2")
        label_3 = QLabel("Core 3")

        self.core_0 = QProgressBar()
        self.core_0.setRange(0, 100)
        self.core_1 = QProgressBar()
        self.core_1.setRange(0, 100)
        self.core_2 = QProgressBar()
        self.core_2.setRange(0, 100)
        self.core_3 = QProgressBar()
        self.core_2.setRange(0, 100)

        btn_exit = QPushButton("Quit")
        btn_exit.clicked.connect(app.quit)

        layout = QVBoxLayout()
        layout.addWidget(label_0)
        layout.addWidget(self.core_0)
        layout.addWidget(label_1)
        layout.addWidget(self.core_1)
        layout.addWidget(label_2)
        layout.addWidget(self.core_2)
        layout.addWidget(label_3)
        layout.addWidget(self.core_3)
        layout.addWidget(btn_exit)
        self.setLayout(layout)
        self.show()

        self.set_caption()

        self.core_update = QTimer()
        self.core_update.timeout.connect(self.core_query)
        self.core_update.start()
    
    def core_query(self):
        core_temps = temp.get_temps()
        temp_0, temp_1, temp_2, temp_3 = core_temps

        self.core_0.setValue(int(temp_0))
        self.core_1.setValue(int(temp_1))
        self.core_2.setValue(int(temp_2))
        self.core_3.setValue(int(temp_3))
        self.set_caption()

    def set_caption(self):
        self.core_0.setFormat(str(self.core_0.value()) + "°C")
        self.core_1.setFormat(str(self.core_1.value()) + "°C")
        self.core_2.setFormat(str(self.core_2.value()) + "°C")
        self.core_3.setFormat(str(self.core_3.value()) + "°C")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
