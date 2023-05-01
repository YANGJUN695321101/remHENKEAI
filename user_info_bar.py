from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon

class UserInfoBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()

        # 用户头像
        self.user_avatar = QLabel()
        pixmap = QPixmap("D:\\DESK\\remHENKEAI-main\\ABC.png")
        self.user_avatar.setPixmap(pixmap.scaled(32, 32))
        layout.addWidget(self.user_avatar)

        # 用户昵称
        user_nickname = QLabel("昵称")
        layout.addWidget(user_nickname)

        # 设置按钮
        settings_button = QPushButton(QIcon("D:\\DESK\\remHENKEAI-main\\scan.ico"), "")
        layout.addWidget(settings_button)

        self.setLayout(layout)



