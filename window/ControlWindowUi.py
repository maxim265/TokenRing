from PyQt5 import QtCore, QtGui, QtWidgets


class ControlWindowUi(object):

    def setupUi(self, ControlWindow):
        ControlWindow.setObjectName("ControlWindow")
        ControlWindow.resize(520, 730)
        ControlWindow.setMinimumSize(QtCore.QSize(520, 730))
        ControlWindow.setMaximumSize(QtCore.QSize(520, 730))
        font = QtGui.QFont()
        font.setPointSize(10)
        ControlWindow.setFont(font)
        ControlWindow.setStyleSheet("background-color: rgb(252, 255, 176);")
        self.centralwidget = QtWidgets.QWidget(ControlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_debug = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_debug.setGeometry(QtCore.QRect(30, 470, 461, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_debug.setFont(font)
        self.txt_debug.setStyleSheet("background-color: rgb(255, 254, 202);")
        self.txt_debug.setObjectName("txt_debug")
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create.setGeometry(QtCore.QRect(30, 60, 110, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_create.setFont(font)
        self.btn_create.setStyleSheet("background-color: rgb(85, 255, 0);\n"
                                      "")
        self.btn_create.setObjectName("btn_create")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(30, 150, 110, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_delete.setFont(font)
        self.btn_delete.setAutoFillBackground(False)
        self.btn_delete.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_delete.setAutoRepeat(False)
        self.btn_delete.setAutoExclusive(False)
        self.btn_delete.setObjectName("btn_delete")
        self.lbl_debug = QtWidgets.QLabel(self.centralwidget)
        self.lbl_debug.setGeometry(QtCore.QRect(225, 430, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_debug.setFont(font)
        self.lbl_debug.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_debug.setObjectName("lbl_debug")
        self.lbl_settings = QtWidgets.QLabel(self.centralwidget)
        self.lbl_settings.setGeometry(QtCore.QRect(175, 20, 170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_settings.setFont(font)
        self.lbl_settings.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_settings.setObjectName("lbl_settings")
        self.cmb_box_ports = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_box_ports.setGeometry(QtCore.QRect(330, 99, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmb_box_ports.setFont(font)
        self.cmb_box_ports.setStyleSheet("background-color: rgb(255, 254, 202);")
        self.cmb_box_ports.setEditable(False)
        self.cmb_box_ports.setObjectName("cmb_box_ports")
        self.cmb_box_ports.addItem("")
        self.cmb_box_ports.addItem("")
        self.cmb_box_ports.addItem("")
        self.cmb_box_ports.addItem("")
        self.cmb_box_ports.addItem("")
        self.lbl_ports = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ports.setGeometry(QtCore.QRect(350, 65, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_ports.setFont(font)
        self.lbl_ports.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ports.setObjectName("lbl_ports")
        self.le_create = QtWidgets.QLineEdit(self.centralwidget)
        self.le_create.setGeometry(QtCore.QRect(170, 99, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_create.setFont(font)
        self.le_create.setStyleSheet("background-color: rgb(255, 254, 202);")
        self.le_create.setObjectName("le_create")
        self.lbl_numb1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_numb1.setGeometry(QtCore.QRect(170, 65, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_numb1.setFont(font)
        self.lbl_numb1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_numb1.setObjectName("lbl_numb1")
        self.lbl_numb2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_numb2.setGeometry(QtCore.QRect(170, 155, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_numb2.setFont(font)
        self.lbl_numb2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_numb2.setObjectName("lbl_numb2")
        self.le_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.le_delete.setGeometry(QtCore.QRect(170, 189, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_delete.setFont(font)
        self.le_delete.setStyleSheet("background-color: rgb(255, 254, 202);")
        self.le_delete.setObjectName("le_delete")
        self.bar_maxnumb = QtWidgets.QProgressBar(self.centralwidget)
        self.bar_maxnumb.setGeometry(QtCore.QRect(340, 160, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bar_maxnumb.setFont(font)
        self.bar_maxnumb.setProperty("value", 0)
        self.bar_maxnumb.setObjectName("bar_maxnumb")
        self.txt_stations = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_stations.setGeometry(QtCore.QRect(30, 280, 461, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_stations.setFont(font)
        self.txt_stations.setStyleSheet("background-color: rgb(255, 254, 202);")
        self.txt_stations.setObjectName("txt_stations")
        self.lbl_stations = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stations.setGeometry(QtCore.QRect(190, 240, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stations.setFont(font)
        self.lbl_stations.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_stations.setObjectName("lbl_stations")
        ControlWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlWindow)
        QtCore.QMetaObject.connectSlotsByName(ControlWindow)

    def retranslateUi(self, ControlWindow):
        _translate = QtCore.QCoreApplication.translate
        ControlWindow.setWindowTitle(_translate("ControlWindow", "MainWindow"))
        self.btn_create.setText(_translate("ControlWindow", "Create"))
        self.btn_delete.setText(_translate("ControlWindow", "Delete"))
        self.lbl_debug.setText(_translate("ControlWindow", "Debug"))
        self.lbl_settings.setText(_translate("ControlWindow", "Station settings:"))
        self.cmb_box_ports.setCurrentText(_translate("ControlWindow", "COM1 <-> COM2"))
        self.cmb_box_ports.setItemText(0, _translate("ControlWindow", "COM1 <-> COM2"))
        self.cmb_box_ports.setItemText(1, _translate("ControlWindow", "COM3 <-> COM4"))
        self.cmb_box_ports.setItemText(2, _translate("ControlWindow", "COM5 <-> COM6"))
        self.cmb_box_ports.setItemText(3, _translate("ControlWindow", "COM7 <-> COM8"))
        self.cmb_box_ports.setItemText(4, _translate("ControlWindow", "COM9 <-> COM10"))
        self.lbl_ports.setText(_translate("ControlWindow", "COM-ports:"))
        self.lbl_numb1.setText(_translate("ControlWindow", "Station number"))
        self.lbl_numb2.setText(_translate("ControlWindow", "Station number"))
        self.lbl_stations.setText(_translate("ControlWindow", "Active stations"))
