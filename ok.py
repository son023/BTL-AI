from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo layout chính
        layout = QVBoxLayout()

        # Tạo widget cha cho layout
        main_widget = QWidget()

        # Đặt background cho widget cha
        main_widget.setStyleSheet("background-image: url(background.png);")

        # Thêm layout vào widget cha
        main_widget.setLayout(layout)

        # Tạo label
        label = QLabel("Đây là label")

        # Thêm label vào layout
        layout.addWidget(label)

        # Cài đặt layout cho widget
        self.setLayout(main_widget)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
