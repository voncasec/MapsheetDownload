# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mapsheetdownload.ui'
#
# Created: Thu Sep 19 11:38:16 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MapsheetDownload(object):
    def setupUi(self, MapsheetDownload):
        MapsheetDownload.setObjectName(_fromUtf8("MapsheetDownload"))
        MapsheetDownload.resize(552, 359)
        self.buttonBox = QtGui.QDialogButtonBox(MapsheetDownload)
        self.buttonBox.setGeometry(QtCore.QRect(370, 280, 171, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.input50k = QtGui.QLineEdit(MapsheetDownload)
        self.input50k.setGeometry(QtCore.QRect(10, 35, 250, 30))
        self.input50k.setObjectName(_fromUtf8("input50k"))
        self.group_250k = QtGui.QGroupBox(MapsheetDownload)
        self.group_250k.setGeometry(QtCore.QRect(280, 70, 260, 100))
        self.group_250k.setObjectName(_fromUtf8("group_250k"))
        self.downloadNTDB250k = QtGui.QCheckBox(self.group_250k)
        self.downloadNTDB250k.setGeometry(QtCore.QRect(0, 20, 200, 20))
        self.downloadNTDB250k.setObjectName(_fromUtf8("downloadNTDB250k"))
        self.downloadDEM250k = QtGui.QCheckBox(self.group_250k)
        self.downloadDEM250k.setGeometry(QtCore.QRect(0, 40, 200, 20))
        self.downloadDEM250k.setObjectName(_fromUtf8("downloadDEM250k"))
        self.downloadTopo250k = QtGui.QCheckBox(self.group_250k)
        self.downloadTopo250k.setGeometry(QtCore.QRect(0, 60, 200, 20))
        self.downloadTopo250k.setObjectName(_fromUtf8("downloadTopo250k"))

        self.downloadCanVec_plus = QtGui.QCheckBox(self.group_250k)
        self.downloadCanVec_plus.setGeometry(QtCore.QRect(0, 80, 200, 20))
        self.downloadCanVec_plus.setObjectName(_fromUtf8("downloadCanVec_plus"))        
        #self.downloadCanVec_plus.setChecked(False)
        
        self.label_250k = QtGui.QLabel(MapsheetDownload)
        self.label_250k.setGeometry(QtCore.QRect(280, 13, 250, 20))
        self.label_250k.setObjectName(_fromUtf8("label_250k"))
        self.group_50k = QtGui.QGroupBox(MapsheetDownload)
        self.group_50k.setGeometry(QtCore.QRect(10, 70, 250, 100))
        self.group_50k.setObjectName(_fromUtf8("group_50k"))

        self.downloadCanVec = QtGui.QCheckBox(self.group_50k)
        self.downloadCanVec.setGeometry(QtCore.QRect(0, 20, 200, 20))
        self.downloadCanVec.setToolTip(_fromUtf8(""))
        #self.downloadCanVec.setChecked(False)
        self.downloadCanVec.setObjectName(_fromUtf8("downloadCanVec"))

        #self.downloadCanVecNew = QtGui.QCheckBox(self.group_50k)
        #self.downloadCanVecNew.setGeometry(QtCore.QRect(0, 20, 200, 20))
        #self.downloadCanVecNew.setToolTip(_fromUtf8(""))
        #self.downloadCanVecNew.setChecked(True)
        #self.downloadCanVecNew.setObjectName(_fromUtf8("downloadCanVecNew"))


        self.downloadNTDB50k = QtGui.QCheckBox(self.group_50k)
        self.downloadNTDB50k.setGeometry(QtCore.QRect(0, 40, 200, 20))
        self.downloadNTDB50k.setObjectName(_fromUtf8("downloadNTDB50k"))
        self.downloadDEM50k = QtGui.QCheckBox(self.group_50k)
        self.downloadDEM50k.setGeometry(QtCore.QRect(0, 60, 200, 20))
        self.downloadDEM50k.setObjectName(_fromUtf8("downloadDEM50k"))
        self.downloadTopo50k = QtGui.QCheckBox(self.group_50k)
        self.downloadTopo50k.setGeometry(QtCore.QRect(0, 80, 200, 20))
        self.downloadTopo50k.setObjectName(_fromUtf8("downloadTopo50k"))
        self.label_50k = QtGui.QLabel(MapsheetDownload)
        self.label_50k.setGeometry(QtCore.QRect(10, 13, 250, 20))
        self.label_50k.setObjectName(_fromUtf8("label_50k"))
        self.outputDir = QtGui.QLineEdit(MapsheetDownload)
        self.outputDir.setGeometry(QtCore.QRect(10, 180, 351, 30))
        self.outputDir.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.outputDir.setObjectName(_fromUtf8("outputDir"))
        


        self.input250k = QtGui.QLineEdit(MapsheetDownload)
        self.input250k.setGeometry(QtCore.QRect(280, 35, 250, 30))
        self.input250k.setObjectName(_fromUtf8("input250k"))
        self.browserButton = QtGui.QPushButton(MapsheetDownload)
        self.browserButton.setGeometry(QtCore.QRect(365, 180, 180, 30))
        self.browserButton.setObjectName(_fromUtf8("browserButton"))
        self.Status = QtGui.QPlainTextEdit(MapsheetDownload)
        self.Status.setGeometry(QtCore.QRect(10, 260, 351, 91))
        self.Status.setObjectName(_fromUtf8("Status"))
        self.progressBar = QtGui.QProgressBar(MapsheetDownload)
        self.progressBar.setGeometry(QtCore.QRect(365, 235, 180, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.addMapLayers = QtGui.QCheckBox(MapsheetDownload)
        self.addMapLayers.setGeometry(QtCore.QRect(50, 230, 300, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addMapLayers.sizePolicy().hasHeightForWidth())
        self.addMapLayers.setSizePolicy(sizePolicy)
        self.addMapLayers.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addMapLayers.setAutoFillBackground(False)
        self.addMapLayers.setChecked(False)
        self.addMapLayers.setObjectName(_fromUtf8("addMapLayers"))

        self.retranslateUi(MapsheetDownload)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MapsheetDownload.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MapsheetDownload.reject)
        QtCore.QMetaObject.connectSlotsByName(MapsheetDownload)

    def retranslateUi(self, MapsheetDownload):
        MapsheetDownload.setWindowTitle(QtGui.QApplication.translate("MapsheetDownload", "NTS Data Download", None, QtGui.QApplication.UnicodeUTF8))
        self.input50k.setToolTip(QtGui.QApplication.translate("MapsheetDownload", "<html><head/><body><p>Separate multiple 50k NTS mapsheets with a comma.</p><p>Each mapsheet must be 6 characters long.</p><p>Example: <span style=\" font-weight:600;\">092h12,092I10</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.input50k.setPlaceholderText(QtGui.QApplication.translate("MapsheetDownload", "Example: 092h12, 092I10", None, QtGui.QApplication.UnicodeUTF8))
        self.group_250k.setTitle(QtGui.QApplication.translate("MapsheetDownload", "1:250000 NTS Datasets to Download", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadNTDB250k.setText(QtGui.QApplication.translate("MapsheetDownload", "NTDB Vector Data", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadDEM250k.setText(QtGui.QApplication.translate("MapsheetDownload", "DEM Raster Data", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTopo250k.setText(QtGui.QApplication.translate("MapsheetDownload", "Topographic Raster Maps", None, QtGui.QApplication.UnicodeUTF8))

        self.downloadCanVec_plus.setText(QtGui.QApplication.translate("MapsheetDownload", "CanVec Plus Vector Data (Archived)", None, QtGui.QApplication.UnicodeUTF8))        
        
        self.label_250k.setText(QtGui.QApplication.translate("MapsheetDownload", "250k Mapsheets to Download", None, QtGui.QApplication.UnicodeUTF8))
        self.group_50k.setTitle(QtGui.QApplication.translate("MapsheetDownload", "1:50000 NTS Datasets to Download", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadCanVec.setText(QtGui.QApplication.translate("MapsheetDownload", "CanVec Vector Data (Archived)", None, QtGui.QApplication.UnicodeUTF8))
        #self.downloadCanVecNew.setText(QtGui.QApplication.translate("MapsheetDownload", "CanVec (Current)", None, QtGui.QApplication.UnicodeUTF8))
        
        self.downloadNTDB50k.setText(QtGui.QApplication.translate("MapsheetDownload", "NTDB Vector Data", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadDEM50k.setText(QtGui.QApplication.translate("MapsheetDownload", "DEM Raster Data", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTopo50k.setText(QtGui.QApplication.translate("MapsheetDownload", "Topographic Raster Maps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50k.setText(QtGui.QApplication.translate("MapsheetDownload", "50k Mapsheets to Download", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDir.setPlaceholderText(QtGui.QApplication.translate("MapsheetDownload", "Directory where data will be saved", None, QtGui.QApplication.UnicodeUTF8))
        self.input250k.setToolTip(QtGui.QApplication.translate("MapsheetDownload", "<html><head/><body><p>Separate multiple 250k NTS mapsheets with a comma.</p><p>Each mapsheet must be 4 characters long.</p><p>Example: <span style=\" font-weight:600;\">092H,092i</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.input250k.setPlaceholderText(QtGui.QApplication.translate("MapsheetDownload", "Example: 092H,092i", None, QtGui.QApplication.UnicodeUTF8))
        self.browserButton.setText(QtGui.QApplication.translate("MapsheetDownload", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.addMapLayers.setText(QtGui.QApplication.translate("MapsheetDownload", "Add downloaded files into the layer tree", None, QtGui.QApplication.UnicodeUTF8))

        #self.outputDir.setText(QtGui.QApplication.translate("MapsheetDownload", "C:\Users\cvandenberg\Desktop\NTS_Test", None, QtGui.QApplication.UnicodeUTF8))
        #self.input250k.setText(QtGui.QApplication.translate("MapsheetDownload", "092h", None, QtGui.QApplication.UnicodeUTF8))
        
        