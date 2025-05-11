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
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

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
        self.pagesloguin = QStackedWidget(login)
        self.pagesloguin.setObjectName(u"pagesloguin")
        self.pagesloguin.setGeometry(QRect(0, -15, 591, 371))
        self.pagina_login = QWidget()
        self.pagina_login.setObjectName(u"pagina_login")
        self.txt_user = QLineEdit(self.pagina_login)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(320, 120, 211, 31))
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
        self.label_3 = QLabel(self.pagina_login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(289, 123, 30, 31))
        self.label_3.setPixmap(QPixmap(u"Icones/user.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.pagina_login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(288, 172, 31, 31))
        self.label_4.setPixmap(QPixmap(u"Icones/senha.png"))
        self.label_4.setScaledContents(True)
        self.label = QLabel(self.pagina_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 60, 151, 51))
        font1 = QFont()
        font1.setPointSize(25)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.pagina_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(320, 220, 211, 31))
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
        self.txt_senha = QLineEdit(self.pagina_login)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(320, 170, 211, 31))
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
        self.btn_esqueceu_senha = QLabel(self.pagina_login)
        self.btn_esqueceu_senha.setObjectName(u"btn_esqueceu_senha")
        self.btn_esqueceu_senha.setGeometry(QRect(330, 260, 201, 21))
        self.btn_esqueceu_senha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_esqueceu_senha.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_esqueceu_senha.setAlignment(Qt.AlignCenter)
        self.btn_visualizar = QLabel(self.pagina_login)
        self.btn_visualizar.setObjectName(u"btn_visualizar")
        self.btn_visualizar.setGeometry(QRect(505, 175, 21, 21))
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
        self.frame = QFrame(self.pagina_login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 241, 371))
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(72, 159, 120)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 181, 181))
        self.label_2.setPixmap(QPixmap(u"../Users/Isal\u00e9o Guimar\u00e3es/Desktop/Software/logo/1.png"))
        self.label_2.setScaledContents(True)
        self.pagesloguin.addWidget(self.pagina_login)
        self.pagina_rsenha = QWidget()
        self.pagina_rsenha.setObjectName(u"pagina_rsenha")
        self.txt_cser_nome = QLineEdit(self.pagina_rsenha)
        self.txt_cser_nome.setObjectName(u"txt_cser_nome")
        self.txt_cser_nome.setGeometry(QRect(300, 40, 271, 31))
        self.txt_cser_nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.txt_cser_email = QLineEdit(self.pagina_rsenha)
        self.txt_cser_email.setObjectName(u"txt_cser_email")
        self.txt_cser_email.setGeometry(QRect(300, 95, 271, 31))
        self.txt_cser_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.txt_cser_assunto = QLineEdit(self.pagina_rsenha)
        self.txt_cser_assunto.setObjectName(u"txt_cser_assunto")
        self.txt_cser_assunto.setGeometry(QRect(300, 150, 271, 31))
        self.txt_cser_assunto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.txt_cser_msg = QLineEdit(self.pagina_rsenha)
        self.txt_cser_msg.setObjectName(u"txt_cser_msg")
        self.txt_cser_msg.setGeometry(QRect(300, 203, 271, 91))
        self.txt_cser_msg.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.btn_cuser_enviar = QPushButton(self.pagina_rsenha)
        self.btn_cuser_enviar.setObjectName(u"btn_cuser_enviar")
        self.btn_cuser_enviar.setGeometry(QRect(301, 300, 271, 31))
        self.btn_cuser_enviar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cuser_enviar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_ct_voltar = QLabel(self.pagina_rsenha)
        self.btn_ct_voltar.setObjectName(u"btn_ct_voltar")
        self.btn_ct_voltar.setGeometry(QRect(360, 331, 161, 21))
        font2 = QFont()
        font2.setBold(False)
        self.btn_ct_voltar.setFont(font2)
        self.btn_ct_voltar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ct_voltar.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_ct_voltar.setAlignment(Qt.AlignCenter)
        self.label_24 = QLabel(self.pagina_rsenha)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 59, 281, 261))
        self.label_24.setPixmap(QPixmap(u"logo/Design sem nome/4.png"))
        self.label_24.setScaledContents(True)
        self.label_11 = QLabel(self.pagina_rsenha)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(36, 43, 231, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.pagina_rsenha)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(305, 24, 47, 13))
        self.label_21 = QLabel(self.pagina_rsenha)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(305, 79, 47, 13))
        self.label_22 = QLabel(self.pagina_rsenha)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(305, 134, 47, 13))
        self.label_23 = QLabel(self.pagina_rsenha)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(305, 186, 71, 16))
        self.label_5 = QLabel(self.pagina_rsenha)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(43, 298, 221, 41))
        self.label_6 = QLabel(self.pagina_rsenha)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(34, 311, 241, 16))
        self.pagesloguin.addWidget(self.pagina_rsenha)

        self.retranslateUi(login)

        self.pagesloguin.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.txt_user.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("login", u"Us\u00faario", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("login", u"Kontrolla", None))
        self.btn_login.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.txt_senha.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("login", u"Senha", None))
        self.btn_esqueceu_senha.setText(QCoreApplication.translate("login", u"Esqueceu a senha?", None))
        self.btn_visualizar.setText("")
        self.label_2.setText("")
        self.txt_cser_nome.setPlaceholderText(QCoreApplication.translate("login", u"   Digite seu nome ", None))
        self.txt_cser_email.setPlaceholderText(QCoreApplication.translate("login", u"   Digite seu E-mail", None))
        self.txt_cser_assunto.setPlaceholderText(QCoreApplication.translate("login", u"  Sobre qual assunto voc\u00ea que tratar?", None))
        self.txt_cser_msg.setPlaceholderText("")
        self.btn_cuser_enviar.setText(QCoreApplication.translate("login", u"Enviar", None))
        self.btn_ct_voltar.setText(QCoreApplication.translate("login", u"Clique para voltar", None))
        self.label_24.setText("")
        self.label_11.setText(QCoreApplication.translate("login", u"RECUPERAR SENHA ", None))
        self.label_20.setText(QCoreApplication.translate("login", u"Nome:", None))
        self.label_21.setText(QCoreApplication.translate("login", u"E-mail:", None))
        self.label_22.setText(QCoreApplication.translate("login", u"Assunto:", None))
        self.label_23.setText(QCoreApplication.translate("login", u"Mensagem:", None))
        self.label_5.setText(QCoreApplication.translate("login", u"<html><head/><body><p align=\"center\">Para recuperar sua senha voc\u00ea deve</p><p align=\"center\"><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("login", u"<html><head/><body><p align=\"center\">entrar em contato com Administrador</p></body></html>", None))
    # retranslateUi

