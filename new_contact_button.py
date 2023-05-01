from PyQt5.QtWidgets import QPushButton

class NewContactButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("新建联系人", parent)
        # 新建联系人按钮部件，用于添加新联系人
