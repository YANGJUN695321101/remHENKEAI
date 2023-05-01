from PyQt5.QtWidgets import QLineEdit

class SearchBar(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText("搜索联系人")
        # 搜索栏部件，用于搜索联系人
