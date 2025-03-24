import flet as ft

def main(page: ft.Page):
    page.title = "Hello Flet"
    page.add(ft.Text(f"Welcome to {page.title}!"))

if __name__ == '__main__':
    ft.app(target=main)