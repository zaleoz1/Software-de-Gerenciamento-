# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(600, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QSize(600, 350))
        login.setMaximumSize(QSize(600, 350))
        login.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        login.setStyleSheet(u"background-color: #fff;")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 231, 351))
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(72, 159, 120)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 181, 181))
        self.label_2.setPixmap(QPixmap(u"logo/1.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 110, 31, 31))
        self.label_3.setPixmap(QPixmap(u"Icones/user.png"))
        self.label_3.setScaledContents(True)
        self.txt_user = QLineEdit(login)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(320, 110, 211, 31))
        font = QFont()
        font.setPointSize(11)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}\n"
"")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(320, 210, 211, 31))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.label_4 = QLabel(login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 160, 31, 31))
        self.label_4.setPixmap(QPixmap(u"Icones/senha.png"))
        self.label_4.setScaledContents(True)
        self.txt_senha = QLineEdit(login)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(320, 160, 211, 31))
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(346, 40, 151, 51))
        font1 = QFont()
        font1.setPointSize(25)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_visualizar = QLabel(login)
        self.btn_visualizar.setObjectName(u"btn_visualizar")
        self.btn_visualizar.setGeometry(QRect(506, 164, 21, 21))
        self.btn_visualizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_visualizar.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 6px;      \n"
"   }\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.btn_visualizar.setPixmap(QPixmap(u"Icones/visualzar.png"))
        self.btn_visualizar.setScaledContents(True)
        self.btn_esqueceu_senha = QLabel(login)
        self.btn_esqueceu_senha.setObjectName(u"btn_esqueceu_senha")
        self.btn_esqueceu_senha.setGeometry(QRect(328, 250, 201, 20))
        self.btn_esqueceu_senha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_esqueceu_senha.setAlignment(Qt.AlignCenter)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.txt_user.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("login", u"Us\u00faario", None))
        self.btn_login.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.label_4.setText("")
        self.txt_senha.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("login", u"Senha", None))
        self.label.setText(QCoreApplication.translate("login", u"Kontrolla", None))
        self.btn_visualizar.setText("")
        self.btn_esqueceu_senha.setText(QCoreApplication.translate("login", u"Esqueceu a senha?", None))
    # retranslateUi

