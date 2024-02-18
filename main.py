# підлючення бібліотек
from random import *
from time import sleep
from PyQt5.QtWidgets import QApplication
app = QApplication([])  # створення додатка
from main_window import *  # підключення модуля
# клас Питання
class Question():
    # Конструктор
    def __init__(self, question, answer, wrong_ans1, wrongans2, wrongans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrongans2
        self.wrong_ans3 = wrongans3

        self.count_ask = 0
        self.count_right = 0
    def got_right(self):  # підрахунок статистики: всі та правильні відповіді
        self.count_right += 1
        self.count_ask += 1
    def got_wrong(self): #
        self.count_ask += 1

#
q = Question('Як створити пустий список?', "list()", "{}", 'print()', 'input()')
q2 = Question('Які типи даних можуть зберігатися у списку?', "Будь-які(Числа, рядки, словники, списки, істина)", "Змінні(списки, рядки, словники)", 'Незмінні(числа, рядки, істина)', 'Ніякі')
q3 = Question('Що таке __init__?', "Конструктор", "Функція", 'Змінна', 'Клас')
q4 = Question('Яка структура словника?', "Ключ-значення", "Різні елементи хаотично", 'Залежні типи даних', 'Хаотично розташовані всі типи даних')
q5 = Question('Яка найпростіша мова програмування?', "Python", "JavaScript", 'Pascal', 'C++')
q6 = Question('Скільки буде 25 * 65?', "1625", "1515", '1725', '1615')
q7 = Question('Скільки буде 110 * 135 ?', "14850", "14950", '14750', '14550')

#
questions = [q, q2, q3, q4, q5, q6, q7]
radio_btn = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]

def new_question():  # Функція нового питання

    global random_q   # Значення змінної одне й те саме
    random_q = choice(questions)  # Рандомний вибір питання
    # зміна тексту
    lb_question.setText(random_q.question)
    lb_right_ans.setText(random_q.answer)
    shuffle(radio_btn)  # перемішка
    # перемішка тексту на радіокнопках
    radio_btn[0].setText(random_q.answer)
    radio_btn[1].setText(random_q.wrong_ans1)
    radio_btn[2].setText(random_q.wrong_ans2)
    radio_btn[3].setText(random_q.wrong_ans3)
new_question()
def win():  #
    message = QMessageBox()
    message.setText("Вітаю! Ви правильно відповіли!")
    message.setIcon(QMessageBox.Information)
    message.exec()
def lose():  #
    message = QMessageBox()
    message.setText("На жаль, ви дали хибну відповідь( Щасти надалі!")
    message.setIcon(QMessageBox.Warning)
    message.exec()
def check():  #
    RadioGroup.setExclusive(False)
    for ans in radio_btn:
        if ans.isChecked():  #
            if ans.text() == lb_right_ans.text():
                win()
                random_q.got_right()
                lb_result.setText("Правильна")
                break
    else: #
        random_q.got_wrong()
        lose()
        lb_result.setText("Хибна")
    RadioGroup.setExclusive(True)


def click_ok(): #

    if btn_next.text() == "Відповісти":  #
        check()  #
        gb_question.hide()  #
        gb_answer.show()  #
        btn_next.setText("Наступне питання")
    else: #
        new_question()  #
        gb_question.show()  #
        gb_answer.hide()  #
        btn_next.setText("Відповісти")  #

btn_next.clicked.connect(click_ok)  #

def click_menuopen ():  #
    if random_q.count_ask == 0:
        c = 0
    else:
        c = (random_q.count_right/random_q.count_ask) * 100
    text = f"Питання:{random_q.question}\n"\
    f"Разів відповіли: {random_q.count_ask}\n"\
    f"Вірниx відповідей: {random_q.count_right}\n"\
    f"Успішність: {round(c,2)}\n"
    lb_statistik.setText(text)
    window.hide()
    menu_win.show()

btn_menu.clicked.connect(click_menuopen)  #

def click_back_menu ():  #
    menu_win.hide()
    window.show()

btn_back.clicked.connect(click_back_menu)  #

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)
def rest():
    n = sp_rest.value()*60
    window.hide()
    menu_win.hide()
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)
window.show()  #
app.exec()