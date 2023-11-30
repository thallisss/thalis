import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users(
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            username TEST NOT NULL,
            email TEXT NOT NULL
        )
        '''
)
conn.commit()

#Aplicação de gestão dos usuarios

class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de gestão de usuarios - versão 0.0.1")
        self.tree = ttk.Treeview(root, columns=('ID', 'Nome de Usuário', 'Email'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Username', text='Usuário')
        self.tree.heading('Email', text='e-mail')
        self.tree.pack(padx=10, pady=10)

        self.load_data()

        add_button = tk.Button(root, text='Adicionar', command=self.show_add_user_window)
        add_button.pack( pady=10 )

        delete.button = tk.Button(root, text='remover', command=self.delete_user)

        def load_data(self):
            #Carregar os dados do banco e exibir no Treeview(janela)
            cursor.execute('SELECT * FROM users')
            rows = cursor.fetchall
            for row in rows:
                self.tree.insert('', 'end', values=row)
        
        def show_add_user_window(self):
            add_user_window = tk.Toplevel(self.root)
            add_user_window.title('Adicionar novo usuario')


            username_label = tk.Label(add_user_window, text='Nome de Usuário')
            username_label.grid(row=0, column=0, padx=10, pady=10)
            username_entry = tk.Entry(add_user_window)
            username_entry.grid(row=0, column=1, padx=10, pady=10 )

            email.label = tk.Label (add_user_window, text='Email: ')
            email.Label.grid(eow=1, cloumn=0, padx=10, pady=10)
            email.entry = tk.Entry(add_user_window)
            email.entry.grid(row=1, column=1, padx=10, pady=10 )

            save_button = tk.Button(add_user_window text='salvar', command=lambda: self.save_user
            (username_entry.get(), email_entry.get(), add_user_window))


            save_button.grid(row=2, columnspan=2, pady=10)

            def save_user(self, username, email, window):


            def delete_user(self):
                selected_item = self.tree.selection()
                if selected_item:
                    user_id = self.tree.item(selected_item)['values'][0]
                    cursor.execute('DELETE FROM users, WHEREid=?'(user_id,))
                    conn.commit()

                    #Apagar da janela
                    self.tree.delet(selected_item)
                else:
                    messagebox.showerror('Erro', 'Selecione um ususario para remover da lista')

if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()

conn.close()
