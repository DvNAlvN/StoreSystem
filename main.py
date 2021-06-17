import sys
import tkinter as tk
from tkinter import messagebox as msg
from login import LoginPage
from settings import Settings
from app_page import AppPage

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_menus()

		self.create_container()

		self.pages = {}
		self.create_appPage()
		self.create_loginPage()

	def change_page(self, page):
			page = self.pages[page]
			page.tkraise()


	def create_menus(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
		self.fileMenu.add_command(label="Add New Items", command=lambda:self.pages['app_page'].clicked_add_new_btn())
		self.fileMenu.add_command(label="Exit", command=self.exit_program)

		self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
		self.helpMenu.add_command(label="About", command=self.show_about_info)

		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)


	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)


	def create_appPage(self):
		self.pages["app_page"] = AppPage(self.container, self.app)

	def create_loginPage(self):
		self.pages['login'] = LoginPage(self.container, self)



	def show_about_info(self):
		msg.showinfo("About Contact App", "This apps created by\n1. Davin A\n2. Migel.O.F\n\nCopyright-2021")
		#msg.showwarning("About Contact App", "This apps created by\n1. Ali\n2. Budi\n\nCopyright-2021")
		#msg.showerror("About Contact App", "This apps created by\n1. Ali\n2. Budi\n\nCopyright-2021")

	def exit_program(self):
		respond = msg.askyesnocancel("Exit Program", "Are you sure and really sure to close the program ?")
		if respond:
			sys.exit()
		


class ContactApp:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myContactApp = ContactApp()
	myContactApp.run()