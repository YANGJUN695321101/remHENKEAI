from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

from contact_list import ContactList
from search_bar import SearchBar
from new_contact_button import NewContactButton
from chat_area import ChatArea
from user_info_bar import UserInfoBar
from input_area import InputArea

class ChatWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("聊天应用")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        # 联系人列表
        self.contact_list = ContactList()
        main_layout.addWidget(self.contact_list)

        # 搜索栏
        search_bar = SearchBar()
        main_layout.addWidget(search_bar)

        # 新建联系人按钮
        new_contact_button = NewContactButton()
        main_layout.addWidget(new_contact_button)

        # 聊天区域
        chat_area = ChatArea()
        main_layout.addWidget(chat_area)

        # 用户信息栏
        user_info_bar = UserInfoBar()
        main_layout.addWidget(user_info_bar)

        # 消息输入区域
        input_area = InputArea()
        main_layout.addWidget(input_area)

        self.setLayout(main_layout)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
