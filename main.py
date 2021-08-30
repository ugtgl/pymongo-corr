import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import numpy as np
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import pandas
import seaborn as sns
import pymongo

client = pymongo.MongoClient('localhost', 27017)

class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi("tasarim.ui", self)

        self.setWindowTitle("Korelasyon aracı")

        self.pushButton.clicked.connect(self.update_graph)
        self.pushButton_2.clicked.connect(self.calccorr)
        self.comboBox_3.currentIndexChanged.connect(self.update_combobox)
        self.comboBox_4.currentIndexChanged.connect(self.update_combobox2)
        self.addToolBar(NavigationToolbar(self.TheWidget.canvas, self))
        self.comboBox_3.addItems(pymongo.MongoClient('localhost', 27017).list_database_names())

    def update_graph(self):
        self.TheWidget.canvas.axes.clear()
        mask = np.triu(np.ones_like(df3.corr()))
        heatm = sns.heatmap(df3.corr(), vmin=-1, vmax=1, annot=True, annot_kws={"fontsize":8},mask= mask,cmap='coolwarm',ax = self.TheWidget.canvas.axes)
        self.TheWidget.canvas.axes.set_title('Korelasyon', fontdict={'fontsize': 12}, pad=12)
        self.TheWidget.canvas.draw()

    def calccorr(self):
        try:
            corrvalue = df3[self.comboBox.currentText()].corr(df3[self.comboBox_2.currentText()])
            corrvalue = round(corrvalue,2)
            self.label_3.setText(str(corrvalue))
            if (corrvalue < -0.5):
                self.label_4.setText("Negatif yönde güçlü ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(117, 83, 250); }")
            elif (corrvalue < 0):
                self.label_4.setText("Negatif yönde zayıf ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(187, 169, 255); }")
            elif (corrvalue < 0.5):
                self.label_4.setText("Pozitif yönde zayıf ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(255, 124, 128); }")
            elif (corrvalue < 1):
                self.label_4.setText("Pozitif yönde güçlü ilişki.")
                self.label_4.setStyleSheet("QLabel {color : rgb(255, 64, 70); }")
        except:
            print("Veri nümerik olmayabilir.")

    def update_combobox(self):
        self.comboBox_4.clear()
        self.comboBox_4.addItems(pymongo.MongoClient('localhost', 27017)[self.comboBox_3.currentText()].list_collection_names())
    def update_combobox2(self):
        if(self.comboBox_4.currentText()):
            print(self.comboBox_4.currentText())
            db = client[self.comboBox_3.currentText()]
            collection2 = db[self.comboBox_4.currentText()]
            global df3
            df3 = pandas.DataFrame((collection2.aggregate([{"$replaceWith": {
                "$mergeObjects": ["$$ROOT", "$propertyMap"]
            }}])))

            df3 = df3.apply(pd.to_numeric, errors='coerce')
            corr_mat = df3.corr()
            corr_mat = np.abs(corr_mat)
            corr_mat.loc[:, :] = np.tril(corr_mat, k=-1)
            already_in = set()
            result = []
            for col in corr_mat:
                perfect_corr = corr_mat[col][corr_mat[col] > 0.9].index.tolist()
                if perfect_corr and col not in already_in:
                    already_in.update(set(perfect_corr))
                    perfect_corr.append(col)
                    result.append(perfect_corr)
            select_nested = [f[1:] for f in result]
            select_flat = [i for j in select_nested for i in j]
            df3 = df3.drop(select_flat, axis=1)
            df3.corr().to_csv("korelasyon.csv", float_format='%.3f')
            self.comboBox.clear()
            self.comboBox_2.clear()
            self.comboBox.addItems(df3.columns)
            self.comboBox_2.addItems(df3.columns)

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()