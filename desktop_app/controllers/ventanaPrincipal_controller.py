from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from .registrarCliente_controller import RegistrarClienteController

class VentanaPrincipalController(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()

        ui_file = QFile("ui/ventanaPrincipal.ui")
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file)
        ui_file.close()

        #btn
        self.ui.btnCerrarSesion.clicked.connect(self.close)
        self.ui.btnregistrarCliente.clicked.connect(self.abrirRegistrarCliente)

    def show(self):
        self.ui.show()

    def abrirRegistrarCliente(self):
        self.registrar_cliente_window = RegistrarClienteController()
        self.registrar_cliente_window.show()

    def close(self):
        from .login_controller import LoginController

        self.main_window = LoginController()
        self.main_window.show()
        self.ui.close()