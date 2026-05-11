from PySide6.QtWidgets import QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from  .ventanaPrincipal_controller import VentanaPrincipalController

class LoginController(QDialog):

    def __init__(self):
        super().__init__()

        loader = QUiLoader()

        ui_file = QFile("ui/login.ui")
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file)
        ui_file.close()

        #btn
        self.ui.btnIngresar.clicked.connect(self.login)
        self.ui.btnCancelar.clicked.connect(self.close)

    def show(self):
        self.ui.show()

    
    def login(self):
        #Aun Falta logica
        self.main_window = VentanaPrincipalController()
        self.main_window.show()
        #cerrar login ventana
        self.ui.close()
    
    def close(self):
        self.ui.close()