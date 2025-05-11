# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 550)
        MainWindow.setMinimumSize(QSize(950, 550))
        MainWindow.setMaximumSize(QSize(950, 550))
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 921, 43))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setGeometry(QRect(10, 6, 75, 31))
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_pg_import = QPushButton(self.frame)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setGeometry(QRect(91, 6, 75, 31))
        self.btn_pg_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pg_import.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_tableas = QPushButton(self.frame)
        self.btn_tableas.setObjectName(u"btn_tableas")
        self.btn_tableas.setGeometry(QRect(172, 6, 75, 31))
        self.btn_tableas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tableas.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_pg_cadastro = QPushButton(self.frame)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setGeometry(QRect(782, 6, 131, 31))
        self.btn_pg_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setGeometry(QRect(253, 7, 75, 31))
        self.btn_contato.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 60, 951, 491))
        font1 = QFont()
        font1.setPointSize(8)
        self.pages.setFont(font1)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 911, 141))
        self.label.setStyleSheet(u"")
        self.label_9 = QLabel(self.pg_home)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(270, 140, 391, 291))
        self.label_9.setPixmap(QPixmap(u"../Software De Gerenciamento/logo/Design sem nome/6.png"))
        self.label_9.setScaledContents(True)
        self.pages.addWidget(self.pg_home)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_4.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.tables)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.tabela_saida = QTreeWidget(self.tables)
        self.tabela_saida.setObjectName(u"tabela_saida")

        self.verticalLayout_5.addWidget(self.tabela_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar_saida = QPushButton(self.frame_2)
        self.btn_gerar_saida.setObjectName(u"btn_gerar_saida")
        self.btn_gerar_saida.setMinimumSize(QSize(100, 27))
        self.btn_gerar_saida.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar_saida.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_gerar_saida)

        self.btn_extorno = QPushButton(self.frame_2)
        self.btn_extorno.setObjectName(u"btn_extorno")
        self.btn_extorno.setMinimumSize(QSize(100, 27))
        self.btn_extorno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_extorno.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_extorno)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setGeometry(QRect(10, 94, 911, 24))
        font2 = QFont()
        font2.setPointSize(11)
        self.txt_filtro.setFont(font2)
        self.txt_filtro.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)
        self.tw_geral = QTableView(self.tab_2)
        self.tw_geral.setObjectName(u"tw_geral")
        self.tw_geral.setGeometry(QRect(10, 130, 911, 321))
        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setGeometry(QRect(470, 60, 451, 28))
        self.btn_excel.setMinimumSize(QSize(123, 28))
        self.btn_excel.setSizeIncrement(QSize(0, 0))
        self.btn_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.btn_chart = QPushButton(self.tab_2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setGeometry(QRect(13, 60, 441, 28))
        self.btn_chart.setMinimumSize(QSize(123, 28))
        self.btn_chart.setSizeIncrement(QSize(0, 0))
        self.btn_chart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_chart.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}\n"
"\n"
"")
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(70, 10, 795, 33))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color:  rgb(0, 170, 127);")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_table)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.frame_4 = QFrame(self.pg_cadastro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(420, 10, 401, 431))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"  border-radius: 20px;\n"
" \n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(70, 80, 281, 31))
        self.txt_nome.setFont(font)
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}\n"
"")
        self.txt_senha = QLineEdit(self.frame_4)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(70, 200, 281, 31))
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}\n"
"")
        self.txt_senha_2 = QLineEdit(self.frame_4)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setGeometry(QRect(70, 254, 281, 31))
        self.txt_senha_2.setFont(font)
        self.txt_senha_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}\n"
"")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)
        self.txt_user = QLineEdit(self.frame_4)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(70, 140, 281, 31))
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(0, 170, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
" \n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(self.frame_4)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(70, 360, 281, 31))
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.cb_perfil = QComboBox(self.frame_4)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setGeometry(QRect(70, 310, 281, 21))
        self.cb_perfil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_perfil.setStyleSheet(u"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"\n"
"")
        self.btn_visualizar = QLabel(self.frame_4)
        self.btn_visualizar.setObjectName(u"btn_visualizar")
        self.btn_visualizar.setGeometry(QRect(323, 258, 21, 21))
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
        self.btn_visualizar.setPixmap(QPixmap(u"../Software De Gerenciamento/Icones/visualzar.png"))
        self.btn_visualizar.setScaledContents(True)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(29, 88, 41, 21))
        self.label_5.setPixmap(QPixmap(u"../Software De Gerenciamento/Icones/user.png"))
        self.label_5.setScaledContents(True)
        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(29, 147, 41, 21))
        self.label_15.setPixmap(QPixmap(u"../Software De Gerenciamento/Icones/user.png"))
        self.label_15.setScaledContents(True)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(29, 207, 41, 21))
        self.label_7.setPixmap(QPixmap(u"../Software De Gerenciamento/Icones/senha.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(29, 260, 41, 21))
        self.label_8.setPixmap(QPixmap(u"../Software De Gerenciamento/Icones/senha.png"))
        self.label_8.setScaledContents(True)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(29, 310, 41, 21))
        self.label_16.setPixmap(QPixmap(u"../Software De Gerenciamento/Icones/user.png"))
        self.label_16.setScaledContents(True)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 10, 251, 51))
        font4 = QFont()
        font4.setPointSize(18)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.pg_cadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 401, 421))
        self.label_2.setPixmap(QPixmap(u"../Software De Gerenciamento/logo/Design sem nome/2.png"))
        self.label_2.setScaledContents(True)
        self.pages.addWidget(self.pg_cadastro)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.btn_cuser_enviar = QPushButton(self.pg_contato)
        self.btn_cuser_enviar.setObjectName(u"btn_cuser_enviar")
        self.btn_cuser_enviar.setGeometry(QRect(540, 410, 271, 31))
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
        self.label_11 = QLabel(self.pg_contato)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(550, 10, 251, 51))
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.txt_cser_nome = QLineEdit(self.pg_contato)
        self.txt_cser_nome.setObjectName(u"txt_cser_nome")
        self.txt_cser_nome.setGeometry(QRect(540, 90, 271, 31))
        self.txt_cser_nome.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"    \n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.txt_cser_email = QLineEdit(self.pg_contato)
        self.txt_cser_email.setObjectName(u"txt_cser_email")
        self.txt_cser_email.setGeometry(QRect(540, 150, 271, 31))
        self.txt_cser_email.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"    \n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.txt_cser_assunto = QLineEdit(self.pg_contato)
        self.txt_cser_assunto.setObjectName(u"txt_cser_assunto")
        self.txt_cser_assunto.setGeometry(QRect(540, 210, 271, 31))
        self.txt_cser_assunto.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"    \n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.txt_cser_msg = QLineEdit(self.pg_contato)
        self.txt_cser_msg.setObjectName(u"txt_cser_msg")
        self.txt_cser_msg.setGeometry(QRect(540, 270, 271, 121))
        self.txt_cser_msg.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"    \n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(550, 70, 47, 13))
        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(550, 130, 47, 13))
        self.label_22 = QLabel(self.pg_contato)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(550, 190, 47, 13))
        self.label_23 = QLabel(self.pg_contato)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(550, 250, 71, 16))
        self.label_24 = QLabel(self.pg_contato)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(60, 40, 421, 441))
        self.label_24.setPixmap(QPixmap(u"../Software De Gerenciamento/logo/Design sem nome/4.png"))
        self.label_24.setScaledContents(True)
        self.pages.addWidget(self.pg_contato)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.frame_5 = QFrame(self.pg_import)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(480, 20, 351, 391))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"  border-radius: 20px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.txt_file = QLineEdit(self.frame_5)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setGeometry(QRect(20, 90, 291, 31))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(False)
        self.txt_file.setFont(font5)
        self.txt_file.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(240, 240, 240);\n"
"    border-radius: 10px;\n"
" \n"
"}")
        self.btn_opnen_xml = QPushButton(self.frame_5)
        self.btn_opnen_xml.setObjectName(u"btn_opnen_xml")
        self.btn_opnen_xml.setGeometry(QRect(260, 90, 51, 31))
        self.btn_opnen_xml.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_opnen_xml.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 130, 291, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{	background-color: rgba(0, 0, 0,0.1);\n"
"                    	color: rgb(255, 255, 255);\n"
"                		border-style: none;\n"
"                		text-align: center;\n"
"                		border-radius:10px;\n"
"                \n"
"                }\n"
" \n"
"               \n"
"QProgressBar::chunk{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 75, 149, 255), stop:1 rgba(72, 130, 157, 255));\n"
"                				border-radius:10px;\n"
"                                }")
        self.progressBar.setValue(0)
        self.btn_import = QPushButton(self.frame_5)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setGeometry(QRect(40, 320, 271, 31))
        self.btn_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 150, 110); /* Cor mais escura ao passar o mouse */\n"
"}")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 10, 251, 51))
        self.label_12.setFont(font4)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(100, 170, 161, 131))
        self.label_17.setPixmap(QPixmap(u"../Software De Gerenciamento/logo/Design sem nome/3.png"))
        self.label_17.setScaledContents(True)
        self.label_18 = QLabel(self.pg_import)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(60, 50, 351, 341))
        self.label_18.setPixmap(QPixmap(u"../Software De Gerenciamento/logo/Design sem nome/1.png"))
        self.label_18.setScaledContents(True)
        self.pages.addWidget(self.pg_import)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_tableas.setText(QCoreApplication.translate("MainWindow", u"TABELAS", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Us\u00faario", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Kontrolla</span></p><p align=\"center\"><span style=\" font-size:28pt;\">Sistema de gerenciamento</span></p></body></html>", None))
        self.label_9.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ESTOQUE</p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Us\u00faario", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Data importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Valor Nfe", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Especie", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"UN", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cod item", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SA\u00cdDA</p></body></html>", None))
        ___qtreewidgetitem1 = self.tabela_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"DATA SA\u00cdDA", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"US\u00daARIO", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"DATA IMPORTA\u00c7\u00c3O", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"SERIE", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar saida", None))
        self.btn_extorno.setText(QCoreApplication.translate("MainWindow", u"Extorno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"GERAL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Inserir nome ", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Inserir senha", None))
        self.txt_senha_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Inserir senha novamente", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Inserir nome do usu\u00e1rio", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Us\u00faario", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.btn_visualizar.setText("")
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText("")
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText("")
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText("")
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText("")
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_2.setText("")
        self.btn_cuser_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.txt_cser_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Digite seu nome ", None))
        self.txt_cser_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Digite seu E-mail", None))
        self.txt_cser_assunto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Sobre qual assunto voc\u00ea que tratar?", None))
        self.txt_cser_msg.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Assunto", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Mensagem", None))
        self.label_24.setText("")
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"      Selecione a pasta com o arquivo XML -->", None))
        self.btn_opnen_xml.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IPORTAR XML", None))
        self.label_17.setText("")
        self.label_18.setText("")
    # retranslateUi

