# головне вікно
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt   # Підключення бібліотек
from menu_window import *
window = QWidget()   # Створення вікна
window.resize(600, 500)   # Розмір вікна
# Створення кнопок
btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
btn_next = QPushButton("Відповісти")
# Створення радіокнопок(перемикачів)
rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")
# Створення групи та додавання до неї радіокнопок
RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)
# Створення написів
lb_question = QLabel('Питання')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_ans = QLabel('відповідь')
# Створення елементів
sp_rest = QSpinBox()
gb_question = QGroupBox("Варіанти відповідей")
gb_answer = QGroupBox("Правильна відповідь")

# Створення горизонтальних та вертикальної ліній, додавання елементів
rb_h1 = QHBoxLayout()
rb_h2 = QHBoxLayout()
rb_v1 = QVBoxLayout()
rb_h1.addWidget(rb_ans1)
rb_h1.addWidget(rb_ans2)
rb_h2.addWidget(rb_ans3)
rb_h2.addWidget(rb_ans4)
# Додавання горизонтальних ліній на вертикальну
rb_v1.addLayout(rb_h1)
rb_v1.addLayout(rb_h2)
gb_question.setLayout(rb_v1)
# Створення горизонтальних та вертикальної ліній, додавання елементів
v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_ans)
gb_answer.setLayout(v1)
h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()
# Додавання віджетів (кнопок, написів)
h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_rest)
# Додавання та розташування елементів
h2_main.addWidget(lb_question, alignment=Qt.AlignCenter)
h3_main.addWidget(gb_question)
h3_main.addWidget(gb_answer)
gb_answer.hide()

h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)

v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout(h2_main, stretch=2)
v1_main.addLayout(h3_main, stretch=8)
v1_main.addLayout(h4_main, stretch=1)
window.setLayout(v1_main)
