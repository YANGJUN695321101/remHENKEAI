from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QComboBox, QPushButton
from PyQt5.QtGui import QIcon

class InputArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()

        # 表情选择器
        emoji_picker = QComboBox()
        layout.addWidget(emoji_picker)

        # 消息输入
        message_input = QLineEdit()
        layout.addWidget(message_input)

        # 附件按钮
        attachment_button = QPushButton(QIcon("path/to/attachment_icon"), "")
        layout.addWidget(attachment_button)

        # 发送按钮
        send_button = QPushButton("发送")
        layout.addWidget(send_button)

        self.setLayout(layout)
        # 输入区域部件，包含表情选择器、消息输入框、附件按钮和发送按钮
