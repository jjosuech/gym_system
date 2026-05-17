from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class RegistrarClienteController(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()

        ui_file = QFile("ui/registrarCliente.ui")
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file)
        ui_file.close()

        #btn
    
    def show(self):
        self.ui.show()