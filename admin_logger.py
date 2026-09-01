import sqlite3
from datetime import datetime
# Connect to the database and create an inventory table
# Подключаемся к базе данных и создайте таблицу инвентаризации
conn = sqlite3.connect("actions.db") # переменная с подключением и моздание sql выражения
cursor = conn.cursor() # Создаём пульт управления # Creating a control panel
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    admin_name TEXT,
    action_text TEXT
)
""") # SQL-запрос для создания таблицы # SQL-query to create a table
# Save changes to disk / Сохраняем все изменения в файл базы данных
conn.commit()
conn.close() # закрывает файл базы # closes the database file
print("Database and table ready!")
import tkinter as tk
# create a main window
# создаем галвное окно
root = tk.Tk()
# variable - window title
# переменная - заголовок окна
root.title("DevSecOps Admin Logger")
# window dimensions
# размеры окна 
root.geometry("400x400")
# painting the background black
# покраска фона в черный
root.configure(bg="black")
#creates a text caption
# создает текстовую надпись
lbl_admin = tk.Label(root, text="Admin Name:", bg="black", fg="white")
# place the inscription on the screen
# размещаем надпись на экране
lbl_admin.pack(pady=5)
# field for entering the admin name
# поле для ввода имени админа 
entry_admin = tk.Entry(root, width=30)
# place it on the screen
# размещаем на экране
entry_admin.pack(pady=5)
# create a text field for input
# создаем текстовое поле для ввода 
entry_action = tk.Entry(root, width=40)
# place it on the screen
# размещаем на экране
entry_action.pack(pady=5)
# module for working with the database
# модуль работы с базой 
def save_to_db():
    # we take the text from the input field using the .get method
    # забираем тeкст с поля ввода с помощью метода .get
    admin = entry_admin.get()
    action = entry_action.get()
    # generate exact date and time
    # генерируем точную дату и время 
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # open the database connection window again
    # открываем окно соединения с базой заново
    db_conn = sqlite3.connect("actions.db")
    db_cursor = db_conn.cursor()
    # execute a safe sql query INSERT INTO
    # выполняем безопасный sql-запрос INSERT INTO
    db_cursor.execute("INSERT INTO logs (timestamp, admin_name, action_text) VALUES (?, ?, ?)", (current_time, admin, action))
    # save the changes and close the database
    # сохраняем изменения и закрываем базу
    db_conn.commit()
    db_conn.close()
    # clear the input field for the next entry
    # очищаем поле ввода для следующей записи
    entry_admin.delete(0, tk.END)
    entry_action.delete(0, tk.END)
    print("Action logged securely! / Действие безопасно записано!")
# create a save button
# создаем кнопку сохранения 
btn_save = tk.Button(root, text="Save Action to SQL", bg="gray20", fg="white", command=save_to_db)
# place it on the screen
# размещаем на экране 
btn_save.pack(pady=20)
root.mainloop()