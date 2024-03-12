import sys
from PyQt5 import  QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel
import tensorflow
import numpy as np
from PIL import Image
model = tensorflow.keras.models.load_model("model.h5")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setFixedSize(560, 720)
        self.setWindowTitle("BTL - AI")
        self.filename=""
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.stacked_widget = QStackedWidget()
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.stacked_widget.addWidget(self.widget1)
        self.stacked_widget.addWidget(self.widget2)
        self.stacked_widget.setStyleSheet("border: 2px  solid black ;border-radius: 10px;background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #000000,  stop:1 #ffffff);")
        
        self.layout_main = QVBoxLayout()
        self.layout_main.addWidget(self.stacked_widget)
        self.central_widget.setLayout(self.layout_main)
        font = QtGui.QFont("roboto", 14)
        font.setBold(True)
        title_label_style = """
            color: white;
            background-color: white;
            margin-left: 120px;
            background-image: url(hinh1.png);
        """
        title_label_style_2 = """
            background-color: black; 
            color: white;
            margin-left: 40px;
            text-align: center;
        """
        button_style="""
            QPushButton {
                background-color:#000;
                color: white;
                font-size: 16px;
                border-radius: 15px;
        
            }
            QPushButton:hover {
                background-color: #333333;
            } 
        
        """
        
        # Trang 1  
        self.layout10 = QtWidgets.QGridLayout()
        self.layout11 = QtWidgets.QGridLayout()
        self.widget1.setLayout(self.layout10)
       
        self.title_label1 = QLabel("            NHÓM 1")
        self.title_label1.setFixedSize(395, 50)
        self.title_label1.setStyleSheet(title_label_style)
        self.title_label1.setFont(font)
        self.layout10.addWidget(self.title_label1,0,0)
        
        self.title_label = QLabel("LÊ ĐÌNH PHÚC          B21DCCN593")
        self.title_label.setFixedSize(480, 50)
        self.title_label.setStyleSheet(title_label_style_2)
        self.title_label.setFont(font)
        self.layout10.addWidget(self.title_label,1,0)
        
        self.title_label = QLabel("NGUYỄN VĂN HẠNH B21DCCN329")
        self.title_label.setFixedSize(480, 50)
        self.title_label.setStyleSheet(title_label_style_2)
        self.title_label.setFont(font)
        self.layout10.addWidget(self.title_label,2,0)
        
        self.title_label = QLabel("ĐÀO HẢI ĐĂNG         B21DCCN197")
        self.title_label.setFixedSize(480, 50)
        self.title_label.setStyleSheet(title_label_style_2)
        self.title_label.setFont(font)
        self.layout10.addWidget(self.title_label,3,0)
        
        self.title_label = QLabel("TRẦN DUY LONG       B21DCCN501")
        self.title_label.setFixedSize(480, 50)
        self.title_label.setStyleSheet(title_label_style_2)
        self.title_label.setFont(font)
        self.layout10.addWidget(self.title_label,4,0)
        
        self.title_label = QLabel("NGUYỄN VĂN SƠN    B21DCCN653")
        self.title_label.setFixedSize(480, 50)
        self.title_label.setStyleSheet(title_label_style_2)
        self.title_label.setFont(font)
        self.layout10.addWidget(self.title_label,5,0)
        
        self.button = QPushButton("Bắt đầu")
        self.button.clicked.connect(self.on_button_clicked)
        self.button.setFixedSize(100, 50)
        self.button.setStyleSheet(button_style)
        self.button.setFont(font)
        self.layout10.addWidget(self.button,6,0) 
        
        self.button_thoat = QtWidgets.QPushButton("Thoát")
        self.layout10.addWidget(self.button_thoat,6,4)
        self.button_thoat.clicked.connect(self.exit_app)
        self.button_thoat.setFixedSize(100, 50)
        self.button_thoat.setStyleSheet(button_style)
        self.button_thoat.setFont(font)
        
        # Trang 2
        self.layout20 = QtWidgets.QVBoxLayout()
        self.layout21 = QtWidgets.QHBoxLayout()
        self.widget2.setLayout(self.layout20)
        
        self.title_label = QLabel("NHẬN DIỆN CHÓ MÈO")
        self.title_label.setFixedSize(395, 50)
        self.title_label.setStyleSheet(title_label_style)
        self.title_label.setFont(font)
        self.layout20.addWidget(self.title_label)
        
        self.image_label = QtWidgets.QLabel()
        self.image_label.setStyleSheet(
           """ background-color:white;
           border: 2px solid black
           """  
        )
        self.layout20.addWidget(self.image_label)
       

        self.prediction_label = QtWidgets.QLabel()
        self.prediction_label.setStyleSheet(
           """ 
           background-color:white;
           font-family:times;
           font-size: 25px;
           border: 2px solid black
           """ 
        )
        self.layout20.addWidget(self.prediction_label)
        
        

        self.file_dialog_button = QtWidgets.QPushButton("Chọn ảnh")
        self.layout21.addWidget(self.file_dialog_button)
        self.file_dialog_button.setFixedSize(100, 50)
        self.file_dialog_button.setFont(font)
        self.file_dialog_button.clicked.connect(self.open_file_dialog)
        self.file_dialog_button.setStyleSheet(button_style)
      
        
        self.file_dialog_button2 = QtWidgets.QPushButton("Dự đoán")
        self.file_dialog_button2.setStyleSheet(button_style)
        self.file_dialog_button2.setFixedSize(100, 50)
        self.file_dialog_button2.setFont(font)
        self.file_dialog_button2.clicked.connect(self.nhan_dien)
        self.layout21.addWidget(self.file_dialog_button2)
        
        self.file_dialog_button3 = QtWidgets.QPushButton("Trở lại")
        self.file_dialog_button3.setStyleSheet(button_style)
        self.file_dialog_button3.setFixedSize(100, 50)
        self.file_dialog_button3.setFont(font)
        self.file_dialog_button3.clicked.connect(self.on_button_clicked_back)
        self.layout21.addWidget(self.file_dialog_button3)
        
        self.layout20.addLayout(self.layout21)
        
    def nhan_dien(self):
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
    def on_button_clicked(self):
            self.stacked_widget.setCurrentIndex(1)
    def on_button_clicked_back(self):
            self.stacked_widget.setCurrentIndex(0)
    def exit_app(self):
        sys.exit()
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    icon = QtGui.QIcon("icon1.png")
    window.setWindowIcon(icon)
    window.setStyleSheet("background-color:#f2f3f7")
    window.show()
    sys.exit(app.exec_())
