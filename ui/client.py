# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 961, 122))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_account = QtWidgets.QLabel(self.groupBox)
        self.label_account.setObjectName("label_account")
        self.horizontalLayout.addWidget(self.label_account)
        self.label_account_content = QtWidgets.QLabel(self.groupBox)
        self.label_account_content.setObjectName("label_account_content")
        self.horizontalLayout.addWidget(self.label_account_content)
        self.pushButton_change = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_change.setObjectName("pushButton_change")
        self.horizontalLayout.addWidget(self.pushButton_change)
        self.pushButton_getAccount = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_getAccount.setObjectName("pushButton_getAccount")
        self.horizontalLayout.addWidget(self.pushButton_getAccount)
        spacerItem = QtWidgets.QSpacerItem(480, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_logout = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_logout.setEnabled(False)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout.addWidget(self.pushButton_logout)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 390, 961, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 861, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.progressBar_chapter = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_chapter.setProperty("value", 0)
        self.progressBar_chapter.setObjectName("progressBar_chapter")
        self.gridLayout_2.addWidget(self.progressBar_chapter, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)
        self.spinBox_crawlMaximum = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_crawlMaximum.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.spinBox_crawlMaximum.setMinimum(1)
        self.spinBox_crawlMaximum.setMaximum(5000)
        self.spinBox_crawlMaximum.setProperty("value", 100)
        self.spinBox_crawlMaximum.setObjectName("spinBox_crawlMaximum")
        self.gridLayout_2.addWidget(self.spinBox_crawlMaximum, 1, 1, 1, 1)
        self.progressBar_crawler = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_crawler.setMaximumSize(QtCore.QSize(500, 16777215))
        self.progressBar_crawler.setProperty("value", 0)
        self.progressBar_crawler.setObjectName("progressBar_crawler")
        self.gridLayout_2.addWidget(self.progressBar_crawler, 1, 2, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 891, 53))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_details = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_details.setMaximum(1000)
        self.spinBox_details.setProperty("value", 100)
        self.spinBox_details.setObjectName("spinBox_details")
        self.horizontalLayout_4.addWidget(self.spinBox_details)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.progressBar_details = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar_details.setProperty("value", 0)
        self.progressBar_details.setObjectName("progressBar_details")
        self.horizontalLayout_4.addWidget(self.progressBar_details)
        self.pushButton_start_details = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_start_details.setObjectName("pushButton_start_details")
        self.horizontalLayout_4.addWidget(self.pushButton_start_details)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 30, 861, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progressBar_crawler_chapter = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar_crawler_chapter.setMaximumSize(QtCore.QSize(500, 16777215))
        self.progressBar_crawler_chapter.setProperty("value", 0)
        self.progressBar_crawler_chapter.setObjectName("progressBar_crawler_chapter")
        self.gridLayout_5.addWidget(self.progressBar_crawler_chapter, 0, 0, 1, 1)
        self.pushButton_start_chapter = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_start_chapter.setObjectName("pushButton_start_chapter")
        self.gridLayout_5.addWidget(self.pushButton_start_chapter, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 140, 961, 221))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 40, 911, 145))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_10.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.comboBox_level = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_level.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBox_level.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_level.setObjectName("comboBox_level")
        self.gridLayout.addWidget(self.comboBox_level, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(30, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.comboBox_grade = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_grade.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_grade.setObjectName("comboBox_grade")
        self.gridLayout.addWidget(self.comboBox_grade, 0, 3, 1, 1)
        self.pushButton_loaddata = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_loaddata.setObjectName("pushButton_loaddata")
        self.gridLayout.addWidget(self.pushButton_loaddata, 0, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.comboBox_subject = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_subject.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_subject.setObjectName("comboBox_subject")
        self.gridLayout.addWidget(self.comboBox_subject, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_3.addWidget(self.label_20)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.comboBox_teaching = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_teaching.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_teaching.setObjectName("comboBox_teaching")
        self.gridLayout.addWidget(self.comboBox_teaching, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)
        self.comboBox_chapter = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_chapter.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_chapter.setObjectName("comboBox_chapter")
        self.gridLayout.addWidget(self.comboBox_chapter, 2, 1, 1, 1)
        self.lcdNumber_chapter = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.lcdNumber_chapter.setObjectName("lcdNumber_chapter")
        self.gridLayout.addWidget(self.lcdNumber_chapter, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 41))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAccessibleName("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDB = QtWidgets.QAction(MainWindow)
        self.actionDB.setObjectName("actionDB")
        self.actionUpgrade = QtWidgets.QAction(MainWindow)
        self.actionUpgrade.setObjectName("actionUpgrade")
        self.menu.addAction(self.actionDB)
        self.menu.addAction(self.actionUpgrade)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_change, self.pushButton_getAccount)
        MainWindow.setTabOrder(self.pushButton_getAccount, self.pushButton_logout)
        MainWindow.setTabOrder(self.pushButton_logout, self.comboBox_level)
        MainWindow.setTabOrder(self.comboBox_level, self.spinBox_crawlMaximum)
        MainWindow.setTabOrder(self.spinBox_crawlMaximum, self.pushButton_start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "账号信息"))
        self.label_account.setText(_translate("MainWindow", "账号："))
        self.label_account_content.setText(_translate("MainWindow", "未知"))
        self.pushButton_change.setText(_translate("MainWindow", "切换"))
        self.pushButton_getAccount.setText(_translate("MainWindow", "获取账号"))
        self.pushButton_logout.setText(_translate("MainWindow", "注销"))
        self.groupBox_2.setTitle(_translate("MainWindow", "操作分类"))
        self.label.setText(_translate("MainWindow", "章节进度"))
        self.checkBox.setText(_translate("MainWindow", "包含子章节"))
        self.label_19.setText(_translate("MainWindow", "次数"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "题库"))
        self.label_2.setText(_translate("MainWindow", "数量："))
        self.label_4.setText(_translate("MainWindow", "进度："))
        self.pushButton_start_details.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "详情页"))
        self.pushButton_start_chapter.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "章节"))
        self.groupBox_3.setTitle(_translate("MainWindow", "筛选条件"))
        self.label_10.setText(_translate("MainWindow", "学级"))
        self.label_12.setText(_translate("MainWindow", "年级"))
        self.pushButton_loaddata.setText(_translate("MainWindow", "加载数据"))
        self.label_11.setText(_translate("MainWindow", "学科"))
        self.label_20.setText(_translate("MainWindow", "教材"))
        self.label_18.setText(_translate("MainWindow", "章节"))
        self.label_3.setText(_translate("MainWindow", "已有数据量："))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.actionDB.setText(_translate("MainWindow", "数据库"))
        self.actionUpgrade.setText(_translate("MainWindow", "检查更新"))

