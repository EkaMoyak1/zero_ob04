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

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Викторина")
        self.root.geometry("400x300")

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=380)
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value="")
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(root, text="Проверить", command=self.check_answer)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option, value=option)

            self.radio_var.set(None)  # Сброс выбора
        else:
            self.show_result()

    def check_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Результат", "Правильно!")
        else:
            messagebox.showinfo("Результат", f"Неправильно! Правильный ответ: {correct_answer}")

        self.current_question += 1
        self.show_question()

    def show_result(self):
        messagebox.showinfo("Итог", f"Викторина завершена!\nПравильных ответов: {self.score} из {len(questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()