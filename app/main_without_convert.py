from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
# импортируем кастомный виджет, чтобы uic мог его создать из .ui:
from widgets.custom_button import ColorButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = Path(__file__).with_name("ui") / "MainWindow.ui"
        uic.loadUi(str(ui_file), self)  # все объекты доступны как self.btnHello и т.д.

        # Соединяем сигналы со слотами (логика здесь)
        self.btnHello.clicked.connect(self.on_hello_clicked)
        self.editName.textChanged.connect(self.on_name_changed)

        # кастомный сигнал из промотируемой кнопки:
        self.btnColor.colorChanged.connect(self.on_color_changed)

        # базовые состояния UI
        self.btnHello.setEnabled(False)

    # Слоты (обработчики)
    def on_hello_clicked(self):
        name = self.editName.text().strip() or "мир"
        self.lblResult.setText(f"Привет, {name}!")

    def on_name_changed(self, text: str):
        self.btnHello.setEnabled(bool(text.strip()))

    def on_color_changed(self, color_name: str):
        # статусбар есть у QMainWindow по умолчанию
        self.statusbar.showMessage(f"Цвет: {color_name}", 2000)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
