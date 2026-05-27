from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication


class OverlayWindow(QWidget):

    def __init__(self):

        super().__init__()

        screens = QGuiApplication.screens()

        # for screen in screens:
        #     print(screen.geometry())

        self.setWindowTitle("Yomiscope")

        print(self.geometry())
        # (x, y, width, height)
        second_screen = screens[0]

        geometry = second_screen.geometry()
        self.setGeometry(geometry.x() + 100, geometry.y() + 100, 800, 200)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        layout = QVBoxLayout()

        self.label = QLabel("Waiting for text...")

        self.label.setWordWrap(True)

        self.label.setStyleSheet("""
            font-size: 28px;
            color: white;
        """)

        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setStyleSheet("""
            background-color: black;
        """)

    def update_text(self, text):

        self.label.setText(text)