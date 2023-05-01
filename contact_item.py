from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QRect, QSize

class ContactItem(QWidget):
    def __init__(self, name, avatar_path):
        super().__init__()

        self.name = name
        self.avatar_path = avatar_path

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

       # 创建圆形头像
        avatar = QLabel()
        pixmap = QPixmap(self.avatar_path)
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        avatar.setPixmap(pixmap)
        avatar.setFixedSize(64, 64)

        # 为头像设置圆角矩形遮罩
        mask = QPixmap(64, 64)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setBrush(QBrush(QColor("white")))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(QRect(0, 0, 64, 64), 32, 32)
        painter.end()

        avatar.setMask(mask.createMaskFromColor(Qt.transparent))

        layout.addWidget(avatar)

        # 联系人名称
        name_label = QLabel(self.name)
        layout.addWidget(name_label)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        self.setLayout(layout)