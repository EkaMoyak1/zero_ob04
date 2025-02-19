import tkinter as tk
from tkinter import messagebox

# Вопросы и ответы
questions = [
    {
        "question": "Какой язык программирования используется для создания этого приложения?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "Как называется библиотека для создания графического интерфейса в Python?",
        "options": ["PyQt", "Tkinter", "Kivy", "wxPython"],
        "answer": "Tkinter"
    },
    {
        "question": "Какой тип данных в Python используется для хранения неизменяемых последовательностей?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    }
]

# Глобальные переменные для хранения состояния
current_question = 0
score = 0

# Функция для отображения текущего вопроса
def show_question():
    global current_question
    if current_question < len(questions):
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            radio_buttons[i].config(text=option, value=option)

        # Сброс выбора радиокнопок
        radio_var.set(None)
    else:
        show_result()

# Функция для проверки ответа
def check_answer():
    global current_question, score
    selected_answer = radio_var.get()
    if not selected_answer:
        messagebox.showwarning("Ошибка", "Выберите ответ!")
        return

    correct_answer = questions[current_question]["answer"]

    if selected_answer == correct_answer:
        score += 1
        messagebox.showinfo("Результат", "Правильно!")
    else:
        messagebox.showinfo("Результат", f"Неправильно! Правильный ответ: {correct_answer}")

    current_question += 1
    show_question()

# Функция для отображения итогового результата
def show_result():
    messagebox.showinfo("Итог", f"Викторина завершена!\nПравильных ответов: {score} из {len(questions)}")
    root.destroy()

# Создание графического интерфейса
root = tk.Tk()
root.title("Викторина")
root.geometry("400x300")

# Элементы интерфейса
question_label = tk.Label(root, text="", wraplength=380)
question_label.pack(pady=20)

radio_var = tk.StringVar()
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=radio_var, value="")
    rb.pack(anchor="w")
    radio_buttons.append(rb)

next_button = tk.Button(root, text="Проверить", command=check_answer)
next_button.pack(pady=20)

# Показать первый вопрос
show_question()

# Запуск основного цикла
root.mainloop()