from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QFrame, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from fixed_contacts import FixedContacts
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("聊天应用")
        MainWindow.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget(MainWindow)
        central_layout = QHBoxLayout(central_widget)

        # 联系人列表模块
        contact_list_layout = QVBoxLayout()
        

        # 头像部分
        avatar_layout = QHBoxLayout()
        user_avatar = QLabel()
        pixmap = QPixmap("D:\\DESK\\remHENKEAI-main\\ABC.png")
        user_avatar.setPixmap(pixmap.scaled(32, 32))
        ai_avatar = QLabel()
        pixmap_ai = QPixmap("D:\\DESK\\remHENKEAI-main\\ABC.png")
        ai_avatar.setPixmap(pixmap_ai.scaled(32, 32))
        avatar_layout.addWidget(user_avatar)
        avatar_layout.addWidget(ai_avatar)
        contact_list_layout.addLayout(avatar_layout)

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("搜索联系人")
        contact_list_layout.addWidget(search_bar)

        contact_list = QListWidget()
        contact_list_layout.addWidget(contact_list)
        # 添加固定联系人
        fixed_contacts = FixedContacts(contact_list)    

        add_friend_button = QPushButton("添加好友/新建AI聊天机器人")
        contact_list_layout.addWidget(add_friend_button)

        central_layout.addLayout(contact_list_layout)
        # 聊天窗口模块
        chat_layout = QVBoxLayout()
        chat_history = QTextEdit()
        chat_history.setReadOnly(True)
        chat_layout.addWidget(chat_history)

        input_area_layout = QHBoxLayout()
        input_area = QLineEdit()
        input_area.setPlaceholderText("输入聊天内容")
        input_area_layout.addWidget(input_area)

        send_button = QPushButton("发送")
        input_area_layout.addWidget(send_button)

        chat_layout.addLayout(input_area_layout)

        central_layout.addLayout(chat_layout)


        # 标题栏模块
        title_bar = QLabel("聊天应用")
        title_bar.setAlignment(Qt.AlignCenter)
        title_bar.setFrameShape(QFrame.Box)
        title_bar.setFrameShadow(QFrame.Raised)
        title_bar.setLineWidth(2)
        title_bar.setFixedHeight(50)

        user_avatar = QLabel()
        pixmap = QPixmap("D:\\DESK\\GPT-3.5\\ABC.png")
        user_avatar.setPixmap(pixmap.scaled(32, 32))
        user_nickname = QLabel("用户昵称")

        menu_button = QPushButton("菜单")
        title_bar_layout = QHBoxLayout()
        title_bar_layout.addWidget(user_avatar)
        title_bar_layout.addWidget(user_nickname)
        title_bar_layout.addWidget(menu_button)

        title_bar.setLayout(title_bar_layout)

        # 消息通知模块
        notification_bar = QLabel("新消息通知")
        notification_bar.setAlignment(Qt.AlignCenter)
        notification_bar.setFrameShape(QFrame.Box)
        notification_bar.setFrameShadow(QFrame.Raised)
        notification_bar.setLineWidth(2)
        notification_bar.setFixedHeight(50)

        # 主布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)
        main_layout.addLayout(central_layout)
        main_layout.addWidget(notification_bar)
        central_widget.setLayout(main_layout)

        MainWindow.setCentralWidget(central_widget)
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

