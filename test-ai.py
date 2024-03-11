import sys
from PyQt5 import  QtGui, QtWidgets
import tensorflow
import numpy as np
from PIL import Image

model = tensorflow.keras.models.load_model("model.h5")

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setFixedSize(560, 720)
        self.setWindowTitle("BTL - AI")
        self.filename=""
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout1 = QtWidgets.QHBoxLayout()
    
        
        
        self.title_label = QtWidgets.QLabel("NHẬN DIỆN CHÓ MÈO")
        self.title_label.setFixedSize(395, 50)
        self.title_label.setStyleSheet("color: white;background-color: #000;margin-left: 120px;")
        font = QtGui.QFont("Roboto", 14)
        font.setBold(True)
        self.title_label.setFont(font)
        self.layout.addWidget(self.title_label)
        self.central_widget.setLayout(self.layout)
        self.central_widget.setStyleSheet("border: 2px solid black;border-radius: 10px;")
        
        self.image_label = QtWidgets.QLabel()
        self.layout.addWidget(self.image_label)
       

        self.prediction_label = QtWidgets.QLabel()
        self.layout.addWidget(self.prediction_label)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("roboto")
        self.prediction_label.setFont(font)
        
       

        self.file_dialog_button = QtWidgets.QPushButton("Chọn ảnh")
        self.file_dialog_button.setStyleSheet("""
            background-color: #000;
            color: #ffffff;
            font-size: 20px;
            border-radius: 10px;
            border: 2px solid #000;
            
        """)
        
        self.file_dialog_button2 = QtWidgets.QPushButton("Dự đoán")
        self.file_dialog_button2.setStyleSheet("""
            background-color: #000;
            color: #ffffff;
            font-size: 20px;
            border-radius: 10px;
            border: 2px solid #000;
        """)
        self.file_dialog_button.setFixedSize(100, 50)
        self.file_dialog_button2.setFixedSize(100, 50)
        self.file_dialog_button.setFont(font)
        self.file_dialog_button2.setFont(font)
        self.file_dialog_button.clicked.connect(self.open_file_dialog)
        self.file_dialog_button2.clicked.connect(self.nhandien)
        self.layout1.addWidget(self.file_dialog_button)
        self.layout1.addWidget(self.file_dialog_button2)
        self.layout.addLayout(self.layout1)
        
    def nhandien(self):
       if self.filename:
            path=self.filename[0]
            image = Image.open(path)
            image = image.resize((128, 128))
            image_data = np.array(image) / 255.0
            image_data = np.expand_dims(image_data, axis=0)
            prediction = model.predict(image_data)
            index=prediction[0]
            class_name= "Mèo" if index[0] > 0.5 else "Chó"    
            tile= index[0] if class_name=="Mèo" else index[1]
            tile="{:.2f}".format(tile*100)+"%"
            self.prediction_label.setText("Dự đoán hình ảnh: " + class_name + "\nXác xuất chính xác: " +tile)    
    def open_file_dialog(self):
        self.filename= QtWidgets.QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.jpg *.jpeg *.png)")
        if self.filename:
            path=self.filename[0]
            image_pixmap = QtGui.QPixmap(path)   
            self.image_label.setPixmap(image_pixmap)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    icon = QtGui.QIcon("icon1.png")
    window.setWindowIcon(icon)
    window.setStyleSheet("background-color:#f2f3f7")
    window.show()
    sys.exit(app.exec_())
