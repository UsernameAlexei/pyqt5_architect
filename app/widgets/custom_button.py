from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton

class ColorButton(QPushButton):
    """
    Кнопка, меняющая цвет и шлющая свой сигнал colorChanged(str).
    """
    colorChanged = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # поддерживаем все стандартные варианты
        self.setCheckable(True)
        self._on = False
        self.toggled.connect(self._on_toggled)
        self._apply_style()

    def _on_toggled(self, checked: bool):
        self._on = checked
        self._apply_style()
        self.colorChanged.emit("green" if self._on else "red")

    def _apply_style(self):
        color = "#2ecc71" if self._on else "#e74c3c"
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 6px 10px;
                border-radius: 6px;
            }}
        """)
