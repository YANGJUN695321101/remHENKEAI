from PyQt5.QtWidgets import QPlainTextEdit

class ChatArea(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 聊天区域部件，显示聊天记录
