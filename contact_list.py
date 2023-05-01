from PyQt5.QtWidgets import QListView

class ContactList(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 联系人列表部件，显示所有联系人
