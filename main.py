from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow, QWidget, QMessageBox, QLineEdit, QTreeWidgetItem)
from PySide6 import QtCore
from ui_login import Ui_login
from ui_main import Ui_MainWindow
import sys
from DataBase import DataBase
from xml_files import Read_xml
import sqlite3
import pandas as pd 
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date
import matplotlib.pyplot as plt


class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.senha_visivel = False 
        self.btn_login.clicked.connect(self.checkLogin)
        self.btn_visualizar.mousePressEvent = self.toggle_password_visibility  

    def toggle_password_visibility(self, event):
        if self.senha_visivel:
            self.txt_senha.setEchoMode(QLineEdit.Password)  
            self.senha_visivel = False
        else:
            self.txt_senha.setEchoMode(QLineEdit.Normal)  
            self.senha_visivel = True

    def open_system(self):
        if self.txt_senha.text() == "123":
            self.w = MainWindow()
            self.w.show()
            self.close()

        else:
            print("Senha incorreta")

    def checkLogin(self):
      self.users = DataBase()
      self.users.conecta()
      autenticado = self.users.check_user(self.txt_user.text(), self.txt_senha.text())
      print(f"DEBUG: Resultado da autenticação: {autenticado}")
     
      if autenticado.lower() in ["administrador", "user"]:
          self.w = MainWindow(self.txt_user.text(), autenticado.lower())
          self.w.show()
          self.close()

      else:
          if self.tentativas < 3:
              msg = QMessageBox()
              msg.setIcon(QMessageBox.Warning)
              msg.setWindowTitle("Acesso negado")
              msg.setText(f"Usuário ou senha incorretos! \n \n Tentativa: {self.tentativas + 1} de 3")
              msg.exec()
              self.tentativas += 1
          if self.tentativas == 3:
             self.users.close_connection()
             sys.exit(0)

class MainWindow(QMainWindow , Ui_MainWindow):
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")

        self.user = username
        if user.lower() == "username":
            self.btn_pg_cadastro.setVisible(False)

        # Botoes de navegação
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_tableas.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_table))
        self.btn_pg_import.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_import))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contato))
        self.btn_pg_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastrar.clicked.connect(self.my_user)

        # Botoes de importação
        self.btn_opnen_xml.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

        # Filtro
        self.txt_filtro.textChanged.connect(self.update_filter)

        # Saída e estorno
        self.btn_gerar_saida.clicked.connect(self.gerar_saida)
        self.btn_extorno.clicked.connect(self.gerar_estorno)

        # Gerar Excel
        self.btn_excel.clicked.connect(self.excel_files)

        # Gráfico
        self.btn_chart.clicked.connect(self.graphic)

        self.reset_table()

    def my_user(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senha incorreta!")
            msg.setText("As senhas não conferem!")
            msg.exec()
            return None

        nome = self.txt_nome.text()
        user = self.txt_user.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.create_table_users()  # Garante que a tabela 'users' será criada
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Usuário cadastrado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_user.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self,str("Open Directory"),
                                                          "/home",
                                                          QFileDialog.ShowDirsOnly
                                       
                                                          | QFileDialog.DontResolveSymlinks)
        self.txt_file.setText(self.path)
   
    def import_xml_files(self): 

        xml = Read_xml(self.txt_file.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = DataBase()
        db.conecta()
        cont = 1

        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont += 1

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Importação de XML")
            msg.setText("Arquivos importados com sucesso!")
            msg.exec()
            self.progressBar.setValue(0)

    def table_estoque(self):

    
        cn  =  sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida = ''", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            #faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_estoque.setSortingEnabled(True)
   
        for i in range(1,15):
            self.tw_estoque.resizeColumnToContents(i)
     
    def table_saida(self):
        cn  =  sqlite3.connect('system.db')
        result = pd.read_sql_query("""SELECT Nfe, serie, data_importacao, data_saida, usuario
         FROM Notas WHERE data_saida != ''""", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tabela_saida, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tabela_saida.setSortingEnabled(True)
   
        for i in range(1,15):
            self.tabela_saida.resizeColumnToContents(i)
        
    def table_geral(self):

        
        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tw_geral.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()

    def reset_table(self):
        self.tw_estoque.clear()
        self.tabela_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()

    def update_filter(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'Nfe LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def gerar_saida(self):

        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items_out.append(child.text(0))
    
        recurse(self.tw_estoque.invisibleRootItem())

        #Pergunta se usuario realmente deseja fazer isos.
        self.question('saída')

    def gerar_estorno(self):
        
        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))

        recurse(self.tabela_saida.invisibleRootItem())
        self.question('estorno')      

    def question(self, table):

        msgBox = QMessageBox()

        if table == 'estorno':
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText("As selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")

        else:
            msgBox.setText("Deseja Gerar saída das nota selecionadas?")
            msgBox.setInformativeText("As notas abaixo será baixada no estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")

        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_table()

            else:
                data_saida = date.today()
                data_saida = data_saida.strftime('%d/%m/%Y')
                self.db = DataBase()
                self.db.conecta()
                self.db.uptdate_estoque(data_saida, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()

    def excel_files(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Relatório de Notas",
            "",
            "Arquivos Excel (*.xlsx)"
        )

        
        if file_path:
            cnx = sqlite3.connect('system.db')
            result = pd.read_sql_query("SELECT * FROM Notas", cnx)
            result.to_excel(file_path, sheet_name='Notas', index=False)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Relatório de Notas")
            msg.setText("Relatório gerado com sucesso!")
            msg.exec()

    def graphic(self):

        cnx = sqlite3.connect("system.db")
        estoque = pd.read_sql_query('SELECT * FROM Notas', cnx)
        saida = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida != ''", cnx)

        estoque = len(estoque)
        saida = len(saida)

        labels = "Estoque", "Saídas"
        sizes = [estoque, saida]
        fig1, axl = plt.subplots()
        axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        axl.axis("equal")

        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login() 
    window.show()
    app.exec()
