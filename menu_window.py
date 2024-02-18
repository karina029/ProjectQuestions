from PyQt5.QtWidgets import *
from main_window import *

menu_win = QWidget()   # Створення вікна
menu_win.resize(400, 300)   # Розмір
menu_win.setWindowTitle('Меню')    # Назва

# Створення написів
lb_quest = QLabel("Ведіть запитання")
lb_right_ans = QLabel("Введіть правильну відповідь")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь")
lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь")
lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь")
# Створення текстових полей
le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()
# Створення кнопок
btn_add_question = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
btn_back = QPushButton("Назад")
# Створення написів та форматування
lb_stat = QLabel("Статистика")
lb_stat.setStyleSheet("font-size: 19px; font-weight: bold;")
lb_statistik = QLabel()
# Вертикальна лінія
vl_labels = QVBoxLayout()
# Розташування об'єктів на лінії
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)
vl_labels.addWidget(btn_add_question)
# Створення вертикальної лінії, розташуванння об'єктів
vl_lineEdit = QVBoxLayout()
vl_lineEdit.addWidget(le_question)
vl_lineEdit.addWidget(le_right_ans)
vl_lineEdit.addWidget(le_wrong_ans1)
vl_lineEdit.addWidget(le_wrong_ans2)
vl_lineEdit.addWidget(le_wrong_ans3)
vl_lineEdit.addWidget(btn_clear)
# Горизонтальна лінія, приєднання вертикальних
hl = QHBoxLayout()
hl.addLayout(vl_labels)
hl.addLayout(vl_lineEdit)
#
vl_main = QVBoxLayout()
vl_main.addLayout(hl)
vl_main.addWidget(lb_stat)
vl_main.addWidget(lb_statistik)
vl_main.addWidget(btn_back)
menu_win.setLayout(vl_main)

menu_win.show() #