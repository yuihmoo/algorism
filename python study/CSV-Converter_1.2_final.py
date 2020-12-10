#-*- coding:utf-8 -*-
#!/usr/bin/env python

import csv
import glob
import os
import os.path
import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 340, 100)
        self.setWindowTitle("CSV-Converter Ver1.2")
        self.setWindowIcon(QIcon('csvicon.png'))

        self.pushButton1 = QPushButton("File Open", self)
        self.pushButton1.resize(130,50)
        self.pushButton1.move(30,25)
        self.pushButton1.clicked.connect(self.pushButton1_Clicked)

        self.pushButton2 = QPushButton("Folder Open", self)
        self.pushButton2.resize(130,50)
        self.pushButton2.move(180,25)
        self.pushButton2.clicked.connect(self.pushButton2_Clicked) 
        #self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        #layout.addWidget(self.label)

        self.show()

    def pushButton1_Clicked(self):
 
        fname = QFileDialog.getOpenFileName(self)
        filename = os.path.basename(fname[0])
        
        if fname[0]:
            f = open(fname[0], 'r')
           	#self.label.setText(filename)

            device_number = f.read(20)
            vehicle_number = f.read(17)
            vehicle_type = f.read(2)
            vehicle_reg_number = f.read(12)
            trans_operator_number = f.read(10)
            if len(filename) == 33:
                driver_code = f.read(18)
            else:
                driver_code = f.read(16)

            datas = f.read()

            data_ = ""
            cnt = 1
            number = 1
            data__ = []
            title = ""
            daily_drive = ""
            stack_drive = ""
            year = ""
            month = ""
            day = ""
            date = ""
            hour = ""
            minute = ""
            second = ""
            time = ""
            speed = ""
            rpm = ""
            brake_signal = ""
            position_xf = ""
            position_xb = ""
            position_x = ""
            position_yf = ""
            position_yb = ""
            position_y = ""
            position_angle = ""
            acc_x = ""
            acc_y = ""
            device_status = ""
            
            for data in datas:
                if cnt < 4:
                    daily_drive = daily_drive + data
                elif cnt < 4+7:
                    stack_drive = stack_drive + data
                elif cnt < 4+7+2:
                    year = year + data
                elif cnt < 4+7+2+2:
                    month = month + data
                elif cnt < 4+7+2+2+2:
                    day = day + data
                elif cnt < 4+7+6+2:
                    hour = hour + data
                elif cnt < 4+7+6+2+2:
                    minute = minute + data
                elif cnt < 4+7+6+2+2+2:
                    second = second + data
                elif cnt < 4+7+14+3:
                    speed = speed + data
                elif cnt < 4+7+14+3+4:
                    rpm = rpm + data
                elif cnt < 4+7+14+3+4+1:
                    brake_signal = brake_signal + data
                elif cnt < 4+7+14+3+4+1+3:
                    position_xf = position_xf + data
                elif cnt < 4+7+14+3+4+1+3+6:
                    position_xb = position_xb + data
                elif cnt < 4+7+14+3+4+1+9+3:
                    position_yf = position_yf + data
                elif cnt < 4+7+14+3+4+1+9+3+6:
                    position_yb = position_yb + data
                elif cnt < 4+7+14+3+4+1+9+9+3:
                    position_angle = position_angle + data
                elif cnt < 4+7+14+3+4+1+9+9+3+6:
                    acc_x = acc_x + data
                elif cnt < 4+7+14+3+4+1+9+9+3+6+6:
                    acc_y = acc_y + data
                elif cnt < 4+7+14+3+4+1+9+9+3+6+6+2:
                    device_status = device_status + data
                cnt = cnt + 1
                title = year + month + day
                date = "/".join([year, month, day])
                time = ":".join([hour, minute, second])
                position_x = ".".join([position_xf, position_xb])
                position_y = ".".join([position_yf, position_yb])
                if cnt == 4+7+14+3+4+1+9+9+3+6+6+2:
                    data__.append({"No":number, "date":date, "time":time, "daily_drive":daily_drive, "stack_drive":stack_drive, "speed":speed, "rpm":rpm, "brake_signal":brake_signal, 
                                   "position_x":position_x, "position_y":position_y, "position_angle":position_angle, "acc_x":acc_x, "acc_y":acc_y, "device_status":device_status})
                    cnt = 0
                    number = number + 1
                    daily_drive = ""
                    stack_drive = ""                    
                    year = ""
                    month = ""
                    day = ""
                    date = ""
                    hour = ""
                    minute = ""
                    second = ""
                    time = ""
                    speed = ""
                    rpm = ""
                    brake_signal = ""
                    position_xf = ""
                    position_xb = ""
                    position_yf = ""
                    position_yb = ""
                    position_x = ""
                    position_y = ""
                    position_angle = ""
                    acc_x = ""
                    acc_y = ""
                    device_status = ""                

            maintitle = 'DTG_' + title + '.csv'
            if os.path.isfile(maintitle):
                self.checkbox = QMessageBox.information(self, 'Error', "이미 파일이 존재합니다!\n" + maintitle, QMessageBox.Ok, QMessageBox.Ok)
            else:
                csv_f = open(maintitle, 'a', newline='')
                wr = csv.writer(csv_f)
                wr.writerow(["No", "Date", "Time", "Daily_drive", "Stack_drive", "Speed", "Rpm", "Brake_signal", "Longitude", "Latitude", "Position_angle", "Acc_x", "Acc_y", "Device_status"])
                for i, t in enumerate(data__):
                    wr.writerow([data__[i]["No"], data__[i]["date"], data__[i]["time"], data__[i]["daily_drive"], data__[i]["stack_drive"], data__[i]["speed"], data__[i]["rpm"], data__[i]["brake_signal"],
                                 data__[i]["position_x"], data__[i]["position_y"], data__[i]["position_angle"], data__[i]["acc_x"], data__[i]["acc_y"], str(data__[i]["device_status"])])
 
                csv_f.close()

                self.checkbox = QMessageBox.information(self, 'OK', "변환 완료되었습니다!\n" + maintitle, QMessageBox.Ok, QMessageBox.Ok)

    def pushButton2_Clicked(self):

        path = QFileDialog.getExistingDirectory(self)
        file_list = os.listdir(path)
        file_list_txt = [file for file in file_list if file.endswith(".TXT")]
        temp = []
        temptrue = []
        
        for i in range(len(file_list_txt)):
             
            f = open(path + '/' + file_list_txt[i], 'r')    
            
            device_number = f.read(20)
            vehicle_number = f.read(17)
            vehicle_type = f.read(2)
            vehicle_reg_number = f.read(12)
            trans_operator_number = f.read(10)
            if len(file_list_txt[i]) == 33:
                driver_code = f.read(18)
            else:
                driver_code = f.read(16)

            datas = f.read()

            data_ = ""
            cnt = 1
            number = 1
            data__ = []
            title = ""
            daily_drive = ""
            stack_drive = ""
            year = ""
            month = ""
            day = ""
            date = ""
            hour = ""
            minute = ""
            second = ""
            time = ""
            speed = ""
            rpm = ""
            brake_signal = ""
            position_xf = ""
            position_xb = ""
            position_x = ""
            position_yf = ""
            position_yb = ""
            position_y = ""
            position_angle = ""
            acc_x = ""
            acc_y = ""
            device_status = ""
            
            for data in datas:
                if cnt < 4:
                    daily_drive = daily_drive + data
                elif cnt < 4+7:
                    stack_drive = stack_drive + data
                elif cnt < 4+7+2:
                    year = year + data
                elif cnt < 4+7+2+2:
                    month = month + data
                elif cnt < 4+7+2+2+2:
                    day = day + data
                elif cnt < 4+7+6+2:
                    hour = hour + data
                elif cnt < 4+7+6+2+2:
                    minute = minute + data
                elif cnt < 4+7+6+2+2+2:
                    second = second + data
                elif cnt < 4+7+14+3:
                    speed = speed + data
                elif cnt < 4+7+14+3+4:
                    rpm = rpm + data
                elif cnt < 4+7+14+3+4+1:
                    brake_signal = brake_signal + data
                elif cnt < 4+7+14+3+4+1+3:
                    position_xf = position_xf + data
                elif cnt < 4+7+14+3+4+1+3+6:
                    position_xb = position_xb + data
                elif cnt < 4+7+14+3+4+1+9+3:
                    position_yf = position_yf + data
                elif cnt < 4+7+14+3+4+1+9+3+6:
                    position_yb = position_yb + data
                elif cnt < 4+7+14+3+4+1+9+9+3:
                    position_angle = position_angle + data
                elif cnt < 4+7+14+3+4+1+9+9+3+6:
                    acc_x = acc_x + data
                elif cnt < 4+7+14+3+4+1+9+9+3+6+6:
                    acc_y = acc_y + data
                elif cnt < 4+7+14+3+4+1+9+9+3+6+6+2:
                    device_status = device_status + data
                cnt = cnt + 1
                title = year + month + day
                date = "/".join([year, month, day])
                time = ":".join([hour, minute, second])
                position_x = ".".join([position_xf, position_xb])
                position_y = ".".join([position_yf, position_yb])
                if cnt == 4+7+14+3+4+1+9+9+3+6+6+2:
                    data__.append({"No":number, "date":date, "time":time, "daily_drive":daily_drive, "stack_drive":stack_drive, "speed":speed, "rpm":rpm, "brake_signal":brake_signal, 
                                   "position_x":position_x, "position_y":position_y, "position_angle":position_angle, "acc_x":acc_x, "acc_y":acc_y, "device_status":device_status})
                    cnt = 0
                    number = number + 1
                    daily_drive = ""
                    stack_drive = ""                    
                    year = ""
                    month = ""
                    day = ""
                    date = ""
                    hour = ""
                    minute = ""
                    second = ""
                    time = ""
                    speed = ""
                    rpm = ""
                    brake_signal = ""
                    position_xf = ""
                    position_xb = ""
                    position_yf = ""
                    position_yb = ""
                    position_x = ""
                    position_y = ""
                    position_angle = ""
                    acc_x = ""
                    acc_y = ""
                    device_status = ""                

            maintitle = 'DTG_' + title + '.csv'
            samefile = os.path.isfile(maintitle)
            
            if samefile:
                temp.append(maintitle)
            else:
                csv_f = open(maintitle, 'a', newline='')
                wr = csv.writer(csv_f)
                wr.writerow(["No", "Date", "Time", "Daily_drive", "Stack_drive", "Speed", "Rpm", "Brake_signal", "Longitude", "Latitude", "Position_angle", "Acc_x", "Acc_y", "Device_status"])
                for i, t in enumerate(data__):
                    wr.writerow([data__[i]["No"], data__[i]["date"], data__[i]["time"], data__[i]["daily_drive"], data__[i]["stack_drive"], data__[i]["speed"], data__[i]["rpm"], data__[i]["brake_signal"],
                                 data__[i]["position_x"], data__[i]["position_y"], data__[i]["position_angle"], data__[i]["acc_x"], data__[i]["acc_y"], str(data__[i]["device_status"])])
 
                csv_f.close()
                temptrue.append(maintitle)
        
        self.checkbox = QMessageBox.information(self, '결과', "변환 완료 : " + str(len(temptrue)) + "\n" + str(temptrue) + "\n" + "변환 실패(중복) :" + str(len(temp)) + "\n" + str(temp), QMessageBox.Ok, QMessageBox.Ok)
        #if temp:
        #    self.checkbox = QMessageBox.information(self, 'Error', "이미 파일이 존재합니다!\n" + str(temp), QMessageBox.Ok, QMessageBox.Ok)
        #else:
        #    self.checkbox = QMessageBox.information(self, 'OK', "변환 완료되었습니다!\n", QMessageBox.Ok, QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()