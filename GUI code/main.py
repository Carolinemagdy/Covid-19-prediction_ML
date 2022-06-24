import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from os import path
from matplotlib.pyplot import imshow, new_figure_manager
import numpy as np 
import matplotlib
matplotlib.use('Qt5Agg')
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split
import numpy as np
# models used
from sklearn.svm import SVC
# data visualization library 



ui,_ = loadUiType(path.join(path.dirname(__file__),'image_viewer_ui.ui'))

class Image_Viewer_App(QMainWindow , ui):
    def __init__(self , parent=None):
        super(Image_Viewer_App , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.x_test=np.zeros(14).astype(int)
        self.btn_grp_0 = QButtonGroup()
        self.btn_grp_0.addButton(self.yes_button_0,0)
        self.btn_grp_0.addButton(self.no_button_0,1)
        self.btn_grp_0.addButton(self.yes_button_1,2)
        self.btn_grp_0.addButton(self.no_button_1,3)
        self.btn_grp_0.addButton(self.yes_button_2,4)
        self.btn_grp_0.addButton(self.no_button_2,5)
        self.btn_grp_0.addButton(self.yes_button_3,6)
        self.btn_grp_0.addButton(self.no_button_3,7)
        self.btn_grp_0.addButton(self.yes_button_4,8)
        self.btn_grp_0.addButton(self.no_button_4,9)
        self.btn_grp_0.addButton(self.yes_button_5,10)
        self.btn_grp_0.addButton(self.no_button_5,11)
        self.btn_grp_0.addButton(self.yes_button_6,12)
        self.btn_grp_0.addButton(self.no_button_6,13)
        self.btn_grp_0.addButton(self.yes_button_7,14)
        self.btn_grp_0.addButton(self.no_button_7,15)
        self.btn_grp_0.addButton(self.yes_button_8,16)
        self.btn_grp_0.addButton(self.no_button_8,17)
        self.btn_grp_0.addButton(self.yes_button_9,18)
        self.btn_grp_0.addButton(self.no_button_9,19)
        self.btn_grp_0.addButton(self.yes_button_10,20)
        self.btn_grp_0.addButton(self.no_button_10,21)
        self.btn_grp_0.addButton(self.yes_button_11,22)
        self.btn_grp_0.addButton(self.no_button_11,23)
        self.btn_grp_0.addButton(self.yes_button_12,24)
        self.btn_grp_0.addButton(self.no_button_12,25)
        self.btn_grp_0.addButton(self.yes_button_13,26)
        self.btn_grp_0.addButton(self.no_button_13,27)
        
        self.yes_button_0.setCheckable(True)
        self.no_button_0.setCheckable(True)
        self.yes_button_1.setCheckable(True)
        self.no_button_1.setCheckable(True)
        self.yes_button_2.setCheckable(True)
        self.no_button_2.setCheckable(True)
        self.yes_button_3.setCheckable(True)
        self.no_button_3.setCheckable(True)
        self.yes_button_4.setCheckable(True)
        self.no_button_4.setCheckable(True)
        self.yes_button_5.setCheckable(True)
        self.no_button_5.setCheckable(True)
        self.yes_button_6.setCheckable(True)
        self.no_button_6.setCheckable(True)
        self.yes_button_7.setCheckable(True)
        self.no_button_7.setCheckable(True)
        self.yes_button_8.setCheckable(True)
        self.no_button_8.setCheckable(True)
        self.yes_button_9.setCheckable(True)
        self.no_button_9.setCheckable(True)
        self.yes_button_10.setCheckable(True)
        self.no_button_10.setCheckable(True)
        self.yes_button_11.setCheckable(True)
        self.no_button_11.setCheckable(True)
        self.yes_button_12.setCheckable(True)
        self.no_button_12.setCheckable(True)
        self.yes_button_13.setCheckable(True)
        self.no_button_13.setCheckable(True)
        self.Handle_Buttons()
        self.update()
        self.show()
        

    def Handle_Buttons(self):
        '''Initializing interface buttons'''
        self.btn_grp_0.buttonClicked.connect(self.select_option_0)
        self.diagnose_button.clicked.connect(self.diagnose)
        self.reset_button.clicked.connect(self.reset)

    def select_option_0(self,x):
        id = self.btn_grp_0.id(x)
        btn = self.btn_grp_0.button(id)
        if id == 0:
                self.x_test[0]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(1).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 1:
            if btn.isChecked():
                self.x_test[0]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(0).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 2:
                self.x_test[1]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(3).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 3:
            if btn.isChecked():
                self.x_test[1]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(2).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 4:
                self.x_test[2]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(5).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 5:
            if btn.isChecked():
                self.x_test[2]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(4).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 6:
                self.x_test[3]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(7).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 7:
            if btn.isChecked():
                self.x_test[3]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(6).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
                     
        if id == 8:
                self.x_test[4]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(9).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 9:
            if btn.isChecked():
                self.x_test[4]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(8).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 10:
                self.x_test[4]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(11).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 11:
            if btn.isChecked():
                self.x_test[4]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(10).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 12:
                self.x_test[5]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(13).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 13:
            if btn.isChecked():
                self.x_test[5]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(12).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 14:
                self.x_test[6]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(15).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 15:
            if btn.isChecked():
                self.x_test[7]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(14).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        
        if id == 16:
                self.x_test[8]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(17).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 17:
            if btn.isChecked():
                self.x_test[8]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(16).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 18:
                self.x_test[9]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(19).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 19:
            if btn.isChecked():
                self.x_test[9]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(18).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 20:
                self.x_test[10]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(21).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 21:
            if btn.isChecked():
                self.x_test[10]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(20).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 22:
                self.x_test[11]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(23).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 23:
            if btn.isChecked():
                self.x_test[11]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(22).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 24:
                self.x_test[12]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(25).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 25:
            if btn.isChecked():
                self.x_test[12]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(24).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")

        if id == 26:
                self.x_test[13]=1
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(27).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        elif id == 27:
            if btn.isChecked():
                self.x_test[13]=0
                btn.setDown(True)
                btn.setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(255, 107, 88);")
                self.btn_grp_0.button(26).setStyleSheet("font: 12pt ""Broadway""; color: rgb(255, 255, 255); background-color: rgb(85, 85, 127);")
        # print(self.x_test)
    def diagnose(self):
        df=pd.read_csv('Covid Dataset.csv')
        columns=df.columns
        label_encoder = LabelEncoder()
        for col in columns:  
            df[col]= label_encoder.fit_transform(df[col])

        df=df.drop(['Wearing Masks','Sanitization from Market'], axis=1)
        x=df.drop('COVID-19',axis=1)
        y=df['COVID-19']
        mutual_info = mutual_info_classif(x, y,random_state=30)
        mutual_info = pd.Series(mutual_info)
        mutual_info.index = x.columns
        # sort values descending
        mutual_info=mutual_info.sort_values(ascending=False)
        
        # get features' names of the max 14 ones
        features_selected=(mutual_info[:14]).index
        # drop any other feature from our dataset
        x = x.drop(x.columns.difference(features_selected), axis=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,random_state=30)

        svc = SVC(kernel='rbf',C=10,gamma=0.1) # Linear Kernel
        #Train the model using the training sets
        svc.fit(x_train, y_train)
        #Predict the response for test dataset
        y_pred = svc.predict([self.x_test])
        
        
        if y_pred[0] == 1:
            self.answer_text.setStyleSheet("font: 16pt ""Arial""; color: rgb(255, 255, 255); background-color: rgb(255, 0, 0);text-align: center;")
            self.answer_text.setText("Unfortunately , you have COVID 19  (POSITIVE)")
        else:
            self.answer_text.setStyleSheet("font: 16pt ""Arial""; color: rgb(255, 255, 255); background-color: rgb(19, 149, 0);text-align: center;")
            self.answer_text.setText("You are COVID 19 Free  (NEGATIVE)")

    def reset(self):
        pass
        
        

       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Image_Viewer_App()
    window.show()
    app.exec_()
