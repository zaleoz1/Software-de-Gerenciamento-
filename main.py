from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit)
from ui_login import Ui_login
from ui_main import Ui_MainWindow
import sys
from DataBase import DataBase


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
          self.w = MainWindow(autenticado.lower())
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
    def __init__(self,user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")

        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)

                # Botoes de navegação

        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_tableas.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_table))
        self.btn_pg_import.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_import))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contato))
        self.btn_pg_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastrar.clicked.connect(self.subscrible_user)

    def subscrible_user(self):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login() 
    window.show()
    app.exec()
