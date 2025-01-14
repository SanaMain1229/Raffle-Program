import sys
import random
import os

import pandas as pd
import openpyxl

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from PyQt5 import QtCore

from FRaffle_ui import Ui_MainUI
from FRSettings_ui import Ui_SettingUI

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainUI()   
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.r_dict = {}
        self.nr_dict = {}
        
        self.wr_dict = {}
        self.nwr_dict = {}

        self.rItem = {}
        self.nrItem = {}

        self.wrItem = {}
        self.nwrItem = {}
        
        self.rl_row = 0
        self.nrl_row = 0

        self.tQty = 0
        self.iName = ""

        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.curDir = os.path.dirname(os.path.abspath(__file__))
        fileName = "Raffle Test.xlsx"
        borderName = "chborder.gif"
        self.FilePath = os.path.join(self.curDir, fileName)
        self.FileBorder = os.path.join(self.curDir, borderName)

        self.wb = openpyxl.load_workbook(self.FilePath)
        self.rws = self.wb["Regular"]
        self.nrws = self.wb["Non Regular"]

        #self.ui.lblWinners.setText("Welcome to semitec Raffle Program")

        self.ui.lblItem.setText("")
        self.CurFont = self.ui.lblNumWin.font()
        self.CurFont.setPointSize(50)
        self.ui.lblNumWin.setFont(self.CurFont)
        self.ui.lblNumWin.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.lblNumWin.setText("DRAW")
        #self.ui.lblCongrats.setVisible(False)

        self.oEffect = QGraphicsOpacityEffect()
        self.ui.lblCongrats.setGraphicsEffect(self.oEffect)
        self.oEffect.setOpacity(0)

        #self.OAnimation = QPropertyAnimation(self.oEffect, b"opacity")
        #self.ui.lblStatus.setText("RAFFLE DRAW")

        self.getRData()
        self.getNRData()

        self.ui.lblSanta.mousePressEvent = self.cSettings
        self.ui.lblNumWin.mousePressEvent = lambda event: self.spinNow(event)

    def spinNow(self, _):
        
        if self.tQty == 0:
            QMessageBox.critical(self, "Invalid Data", "No more People to spin")
            return

        self.spinCounter = 0
        self.spinName = ""
        self.ui.lblWinners.clear()
        self.ui.lblNumWin.clear()
        self.CurFont = self.ui.lblNumWin.font()
        self.CurFont.setPointSize(125)
        self.ui.lblNumWin.setFont(self.CurFont)
        self.ui.lblNumWin.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.spinTimer = QTimer(self)
        self.spinTimer.timeout.connect(self.startSpin)
        self.spinTimer.start(1500)

    def startSpin(self):

        try:

            if self.spinCounter < self.tQty:
                
                if self.ui.lblStatus.text().strip() == "REGULAR":
                    rkey = random.choice(list(self.r_dict.items()))[0]
                    rval = self.r_dict[rkey]

                    self.wr_dict.update({rkey: rval})
                    self.r_dict.pop(rkey)
                    self.spinCounter += 1
                    self.ui.lblNumWin.setText(str(rkey))

                    self.rws[f"D{self.rl_row}"].value = rkey
                    self.rws[f"E{self.rl_row}"].value = rval
                    self.rws[f"F{self.rl_row}"].value = self.iName

                    self.rl_row += 1

                    if self.spinName == "":
                        self.spinName = rkey
                    else:
                        self.spinName = f"{self.spinName}, {rkey}"

                    self.ui.lblWinners.setText(str(self.spinName))

                    self.wb.save(self.FilePath)

                else:
                    rkey = random.choice(list(self.nr_dict.items()))[0]
                    rval = self.nr_dict[rkey]

                    self.nwr_dict.update({rkey: rval})
                    self.nr_dict.pop(rkey)
                    self.spinCounter += 1
                    self.ui.lblNumWin.setText(str(rkey))

                    self.nrws[f"D{self.nrl_row}"].value = rkey
                    self.nrws[f"E{self.nrl_row}"].value = rval
                    self.nrws[f"F{self.nrl_row}"].value = self.iName

                    self.nrl_row += 1

                    if self.spinName == "":
                        self.spinName = rkey
                    else:
                        self.spinName = f"{self.spinName}, {rkey}"
                    
                    self.ui.lblWinners.setText(str(self.spinName))

                    self.wb.save(self.FilePath)

            else:

                if self.ui.lblStatus.text().strip() == "REGULAR":
                    if self.cLoc != 0:
                        self.rItem.pop(self.rws[f"H{self.cLoc}"].value)
                        self.rws[f"J{self.cLoc}"].value = "Done"
                else:
                    if self.cLoc != 0:
                        self.nrItem.pop(self.nrws[f"H{self.cLoc}"].value)
                        self.nrws[f"J{self.cLoc}"].value = "Done"
                    ""

                self.ui.lblNumWin.setText("DRAW")
                self.CurFont.setPointSize(50)
                self.ui.lblNumWin.setFont(self.CurFont)
                self.ui.lblNumWin.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.ui.lblNumWin.setFont(self.CurFont)

                self.wb.save(self.FilePath)
                #QMessageBox.information(self, "Congratulations", f"Congratulations on the winners")
                self.OAnimation = QPropertyAnimation(self.oEffect, b"opacity")
                self.OAnimation.setDuration(2000)
                self.OAnimation.setStartValue(0)
                self.OAnimation.setEndValue(1)

                self.OAnimation.start()

                self.spinTimer.stop()
                self.tQty = 0

        except Exception as e:
            QMessageBox.critical(self, "Invalid Data", f"{e}")
            self.spinTimer.stop()
            ""
    
    def getNRData(self):
        
        for cRow in range(2,1000):

            cKey = self.nrws[f"D{cRow}"].value
            cVal = self.nrws[f"E{cRow}"].value

            if cKey is not None:
                self.nwr_dict.update({cKey: cVal})
            else:
                self.nrl_row = cRow
                break
        
        for cRow in range(2, 100):
            
            cKey = self.nrws[f"A{cRow}"].value
            cVal = self.nrws[f"B{cRow}"].value

            if cVal is not None and cKey not in self.nwr_dict:
                self.nr_dict.update({cKey: cVal})
            elif cVal is None:
                break
        
        for cRow in range(2, 1000):
            cKey = self.nrws[f"H{cRow}"].value
            cVal = self.nrws[f"I{cRow}"].value

            if cKey is not None and self.nrws[f"J{cRow}"].value is None:
                self.nrItem.update({cKey: cVal})
                self.nwrItem.update({cKey: cRow})
            elif cKey is None:
                break

    def getRData(self):
        # Getting Winners
        for cRow in range(2,1000):

            cKey = self.rws[f"D{cRow}"].value
            cVal = self.rws[f"E{cRow}"].value

            if cKey is not None:
                self.wr_dict.update({cKey: cVal})
            else:
                self.rl_row = cRow
                break

        # Getting Not winners
        for cRow in range(2,1000):
            cKey = self.rws[f"A{cRow}"].value
            cVal = self.rws[f"B{cRow}"].value

            if cVal is not None and cKey not in self.wr_dict:
                self.r_dict.update({cKey: cVal})
            elif cVal is None:
                break
        
        # Getting Raffle Items
        for cRow in range(2,1000):
            cKey = self.rws[f"H{cRow}"].value
            cVal = self.rws[f"I{cRow}"].value
            if cKey is not None and self.rws[f"J{cRow}"].value is None:
                self.rItem.update({cKey: cVal})
                self.wrItem.update({cKey: cRow})
            elif cKey is None:
                break

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:
            # Adjust the size of the background label dynamically
            if hasattr(self, 'bgLbl'):
                self.bgLbl.setGeometry(0, 0, self.width(), self.height())
            #if hasattr(self, 'IFrmLbl'):
            #    self.IFrmLbl.setGeometry(0,0,self.width(), self.height())
        return super().eventFilter(obj, event)

    def cSettings(self, event):
        
        self.sFrm = QDialog(self)
        self.sUI = Ui_SettingUI()
        self.sUI.setupUi(self.sFrm)

        self.borderLbl = QLabel(self.sFrm)
        self.borderLbl.setGeometry(0,0,self.sFrm.width(), self.sFrm.height())
        self.borderLbl.setStyleSheet("background: transparent;")
        self.borderLbl.lower()

        #self.borderMovie = QMovie(r"C:/Users/Programmer/Documents/Raffle Python/chborder.gif")
        self.borderMovie = QMovie(self.FileBorder)
        self.borderMovie.setScaledSize(self.sFrm.size())
        self.borderLbl.setMovie(self.borderMovie)
        self.borderMovie.start()

        self.sFrm.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.sUI.pbClose.clicked.connect(lambda: self.sFrm.close())

        self.sUI.RBReg.clicked.connect(self.RegButton)
        self.sUI.RBIrr.clicked.connect(self.NRegButton)

        self.sUI.pbChange.clicked.connect(self.setDetails)

        self.sUI.comboChoice.currentTextChanged.connect(self.CheckOthers)

        self.sFrm.setModal(True)
        self.sFrm.exec_()

    def NRegButton(self):
        self.sUI.comboChoice.clear()
        self.sUI.leQty.clear()
        self.sUI.leSpecify.clear()

        self.sUI.comboChoice.addItems(self.nrItem.keys())
        self.sUI.comboChoice.addItem("Others")

        self.sUI.comboChoice.setEnabled(True)
        #self.sUI.comboChoice.setEnabled(True)

    def RegButton(self):
        self.sUI.comboChoice.clear()
        self.sUI.leQty.clear()
        self.sUI.leSpecify.clear()

        self.sUI.comboChoice.addItems(self.rItem.keys())
        self.sUI.comboChoice.addItem("Others")

        self.sUI.comboChoice.setEnabled(True)
        #self.sUI.comboChoice.setEnabled(True)
        
    def CheckOthers(self, text):

        if text == "Others":
            self.sUI.leSpecify.setEnabled(True)
            self.sUI.leQty.setEnabled(True)
            self.sUI.leQty.setText("")
        else:

            if self.sUI.RBReg.isChecked():
                self.sUI.leQty.setText(str(self.rItem.get(self.sUI.comboChoice.currentText(), "")))
                self.cLoc = self.wrItem.get(self.sUI.comboChoice.currentText(), "")
            elif self.sUI.RBIrr.isChecked():
                self.sUI.leQty.setText(str(self.nrItem.get(self.sUI.comboChoice.currentText(), "")))
                self.cLoc = self.nwrItem.get(self.sUI.comboChoice.currentText(), "")

            self.sUI.leQty.setDisabled(True)
            self.sUI.leSpecify.setDisabled(True)

    def setDetails(self):
        
        if self.sUI.leSpecify.isEnabled() and not self.sUI.leSpecify.text().strip():
            QMessageBox.critical(self, "Invalid Data", "Add Item Name")
            return
        
        if not self.sUI.leQty.text().strip():
            QMessageBox.critical(self, "Invalid Data", "Input Quantity First")
            return
        try:

            if self.sUI.comboChoice.currentText() != "Others":
                self.iName = self.sUI.comboChoice.currentText().upper()
                self.tQty = int(self.sUI.leQty.text())
            else:
                self.cLoc = 0
                self.iName = self.sUI.leSpecify.text().upper()
                self.tQty = int(self.sUI.leQty.text())
                #self.sUI.leQty.setText(self.tQty)
                
            #self.tQty = int(self.sUI.leQty.text())
            
            if self.sUI.RBReg.isChecked():
                self.ui.lblStatus.setText("REGULAR")
            elif self.sUI.RBIrr.isChecked():
                self.ui.lblStatus.setText("NON REGULAR")
            
            self.ui.lblItem.setText(self.iName)
            self.ItemFont = self.ui.lblItem.font()
            self.ItemFont.setPointSize(50)

            if len(self.iName) >= 20:
                self.ItemFont.setPointSize(25)

            self.ui.lblItem.setFont(self.ItemFont)

            self.ui.lblWinners.clear()
            self.ui.lblRaffle.clear()
            self.ui.lblCongrats.setGraphicsEffect(self.oEffect)
            self.oEffect.setOpacity(0)
            self.sFrm.close()

        except Exception as e:
            QMessageBox.critical(self, "Invalid Data", f"Error Found: {e}")
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


"""
        self.borderLbl = QLabel(self.ui.borderFrame)
        self.borderLbl.setGeometry(0,0,self.ui.borderFrame.width(), self.ui.borderFrame.height())
        self.borderLbl.setStyleSheet("background: transparent;")
        self.borderLbl.lower()

        self.borderMovie = QMovie(r"C:/Users/Programmer/Documents/Raffle Python/chborder.gif")
        self.borderMovie.setScaledSize(self.ui.borderFrame.size())
        self.borderLbl.setMovie(self.borderMovie)
        self.borderMovie.start()

        self.infoLbl = QLabel(self.ui.infoFrame)
        self.infoLbl.setGeometry(0,0, self.ui.infoFrame.width(), self.ui.infoFrame.height())
        self.infoLbl.setStyleSheet("background: transparent;")
        self.infoLbl.lower()

        self.infoMovie = QMovie(r"C:/Users/Programmer/Documents/Raffle Python/chborder.gif")
        self.infoMovie.setScaledSize(self.ui.infoFrame.size())
        self.infoLbl.setMovie(self.infoMovie)
        self.infoMovie.start() 
    
    def setInfoFrameImage(self):
        self.IFrmLbl = QLabel(self.ui.infoFrame)
        self.IFrmLbl.setPixmap(QPixmap(self.ifrmPath))
        self.IFrmLbl.setScaledContents(True)
        self.IFrmLbl.setGeometry(0,0, self.ui.infoFrame.width(), self.ui.infoFrame.height())
        self.IFrmLbl.lower()
        self.installEventFilter(self)
    

    def setBackGroundImage(self):
        self.bgLbl = QLabel(self)
        self.bgLbl.setPixmap(QPixmap(self.i_path))
        self.bgLbl.setScaledContents(True)
        self.bgLbl.setGeometry(0,0, self.width(), self.height())
        self.bgLbl.lower()
        self.installEventFilter(self)
    
    
    def setBFrame(self):
        self.fLbl = QLabel(self.ui.bFrame)
        self.fLbl.setPixmap(QPixmap(self.b_path))
        self.fLbl.setScaledContents(True)
        self.fLbl.setGeometry(0,0,self.ui.bFrame.width(), self.ui.bFrame.height())
        #self.fLbl.lower()
        self.installEventFilter(self)
    
    def setNumPlayer(self):
        self.numLbl = QLabel(self.ui.NumFrame)
        self.numLbl.setGeometry(0,0, self.ui.NumFrame.width(), self.ui.NumFrame.height())
        self.numLbl.lower()

        self.numMovie = QMovie(self.movBorder)
        self.numMovie.setScaledSize(self.ui.NumFrame.size())
        self.numLbl.setMovie(self.numMovie)
        self.numMovie.start()
        
    def setWinPlayer(self):
        self.winLbl = QLabel(self.ui.WinFrame)
        self.winLbl.setGeometry(0,0, self.ui.WinFrame.width(), self.ui.WinFrame.height())
        self.winLbl.lower()

        self.winMovie = QMovie(self.movBorder)
        self.winMovie.setScaledSize(self.ui.WinFrame.size())
        self.winLbl.setMovie(self.winMovie)
        self.winMovie.start()
    """   