import flet as ft
import re  # Add this at the top with other imports

def form_submit_function(e):
    form_controls = e.control.parent.controls
    
    # Get references to TextFields
    first_name = form_controls[1]
    email = form_controls[2]
    password = form_controls[3]
    
    # Reset error messages
    first_name.error_text = None
    email.error_text = None
    password.error_text = None
    
    # Validate fields
    has_error = False
    if not first_name.value:
        first_name.error_text = "Please enter your first name"
        has_error = True
    
    # Email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email.value:
        email.error_text = "Please enter your email"
        has_error = True
    elif not re.match(email_pattern, email.value):
        email.error_text = "Please enter a valid email address"
        has_error = True
    
    if not password.value:
        password.error_text = "Please enter your password"
        has_error = True
    
    # Update the UI to show error messages if any
    e.page.update()
    
    # If no errors, print the values
    if not has_error:
        print(f"First Name: {first_name.value}")
        print(f"Email: {email.value}")
        print(f"Password: {password.value}")

form_container = ft.Container(
    ft.Column(
        controls=[
            ft.Text("Login", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),  # Updated to ft.Colors
            ft.TextField(label="First Name", color=ft.Colors.BLACK, border_radius=ft.border_radius.all(14), focused_border_color='#0a85ff'),
            ft.TextField(label="Email", color=ft.Colors.BLACK, border_radius=ft.border_radius.all(14), focused_border_color='#0a85ff'),
            ft.TextField(label="Password", color=ft.Colors.BLACK, border_radius=ft.border_radius.all(14), focused_border_color='#0a85ff', password=True, can_reveal_password=True),
            ft.ElevatedButton(
                text="Login",
                color=ft.Colors.WHITE,
                bgcolor='#0a85ff',
                width=350,
                height=50,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=14),
                    text_style=ft.TextStyle(size=18)
                ),
                # on_click=lambda e: print("Login clicked!")  # Simplified click handler
                on_click=form_submit_function
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Moved from Container to Column
    ),
    width=400,
    height=400,
    bgcolor=ft.Colors.WHITE,
    border_radius=ft.border_radius.all(20),
    padding=ft.padding.only(top=20, left=20, right=20),
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=10,
        color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),  # Updated opacity syntax
        offset=ft.Offset(-5, -5),
    )
)

def main(page: ft.Page):
    page.window.width = 600
    page.window.height = 600
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = '#e6e6eb'
    page.title = "Form Simple"
    page.add(ft.Text(f"Welcome to {page.title}!"),
             form_container)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
