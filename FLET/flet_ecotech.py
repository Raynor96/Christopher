from ecotech import Auth, Database, Finance
from dotenv import load_dotenv
import flet as ft
import os

load_dotenv()


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Ecotech Solutions"

        self.db = Database(
            username=os.getenv("ORACLE_USER"),
            password=os.getenv("ORACLE_PASSWORD"),
            dsn=os.getenv("ORACLE_DSN")
        )

        try:
            self.db.create_all_tables()
        except Exception as error:
            print(error)

        self.loged_user = ""
        self.loged_user_id = 0
        self.page_register()
        

    # ---------------- REGISTRO ----------------
    def page_register(self):
        self.page.controls.clear()

        self.input_id = ft.TextField(
            label="ID del usuario",
            hint_text="Ingresa un número para el ID del usuario"
        )

        self.input_username = ft.TextField(
            label="Nombre de usuario",
            hint_text="Ingresa un nombre de usuario"
        )

        self.input_password = ft.TextField(
            label="Contraseña",
            hint_text="Ingresa una contraseña",
            password=True,
            can_reveal_password=True
        )

        self.button_register = ft.Button(
            content=ft.Text("Registrarse"),
            on_click=self.handle_register
        )

        self.text_status = ft.Text(value="")

        self.text_login = ft.Text(value="¿Ya tienes una cuenta?")

        self.button_login = ft.Button(
            content=ft.Text("Inicia sesión"),
            on_click=lambda e: self.page_login()
        )

        self.page.add(
            self.input_id,
            self.input_username,
            self.input_password,
            self.button_register,
            self.text_status,
            self.text_login,
            self.button_login
        )

        self.page.update()

    def handle_register(self, e):
        try:
            id_user = int((self.input_id.value or "").strip())
            username = (self.input_username.value or "").strip()
            password = (self.input_password.value or "").strip()

            status = Auth.register(
                db=self.db,
                id=id_user,
                username=username,
                password=password
            )

            self.text_status.value = status["message"]
            self.page.update()

        except ValueError:
            self.text_status.value = "ID sólo debe ser numérico"
            self.page.update()

    # ---------------- LOGIN ----------------
    def page_login(self):
        self.page.controls.clear()

        self.input_username = ft.TextField(
            label="Nombre de usuario",
            hint_text="Ingresa tu nombre de usuario"
        )

        self.input_password = ft.TextField(
            label="Contraseña",
            hint_text="Ingresa tu contraseña",
            password=True,
            can_reveal_password=True
        )

        self.button_login = ft.Button(
            content=ft.Text("Iniciar sesión"),
            on_click=self.handle_login
        )

        self.text_status = ft.Text(value="")

        self.text_register = ft.Text(value="¿Aún no tienes cuenta?")

        self.button_register = ft.Button(
            content=ft.Text("Regístrate"),
            on_click=lambda e: self.page_register()
        )

        self.page.add(
            self.input_username,
            self.input_password,
            self.button_login,
            self.text_status,
            self.text_register,
            self.button_register
        )

        self.page.update()

    def handle_login(self, e):
        username = (self.input_username.value or "").strip()
        password = (self.input_password.value or "").strip()

        status = Auth.login(
            db=self.db,
            username=username,
            password=password
        )

        self.text_status.value = status["message"]
        self.page.update()

        if status["success"]:
            self.loged_user = username
            self.loged_user_id = status["id"]
            self.page_main_menu()

    # ---------------- MENÚ PRINCIPAL ----------------
    def page_main_menu(self):
        self.page.controls.clear()

        self.text_title_main_menu = ft.Text(
            value="Main Menu",
            color="#cc0000",
            size=32,
            weight=ft.FontWeight.BOLD
        )

        self.text_welcome = ft.Text(
            value=f"Hola {self.loged_user}"
        )

        self.button_indicators = ft.Button(
            content=ft.Text("Consultar Indicadores"),
            on_click=lambda e: self.page_indicator_menu()
        )

        self.button_history = ft.Button(
            content=ft.Text("Historial de consultas"),
            on_click=lambda e: self.page_history_menu()
        )

        self.button_logout = ft.Button(
            content=ft.Text("Cerrar sesión"),
            on_click=lambda e: self.handle_logout()
        )
        

        self.page.add(
            self.text_title_main_menu,
            self.text_welcome,
            self.button_indicators,
            self.button_history,
            self.button_logout
        )

        self.page.update()

    # ---------------- SUBMENÚS ----------------
    def page_indicator_menu(self):
        self.page.controls.clear()

        self.text_title_main_menu = ft.Text(
            value="Main Menu",
            color="#cc0000",
            size=32,
            weight=ft.FontWeight.BOLD
            
        )

        self.text_welcome = ft.Text(
            value=f"Hola {self.loged_user}"
        )

        self.page.add(
            self.text_title_main_menu,
            self.text_welcome
        )

        opciones = {
            "1": ("UF (Unidad de Fomento)", "uf"),
            "2": ("IVP (Índice de Valor Promedio)", "ivp"),
            "3": ("IPC (Índice de Precios al Consumidor)", "ipc"),
            "4": ("UTM (Unidad Tributaria Mensual)", "utm"),
            "5": ("Dólar Observado", "dolar"),
            "6": ("Euro", "euro")
        }

        for key, value in opciones.items():

            button = ft.Button(
                content=ft.Text(value[0]),
                on_click=lambda e, indicador=value[1]: self.handle_indicator(indicador)
            )
            self.page.add(button)

        self.button_volver= ft.Button(
                        content=ft.Text("Volver al menú principal"),
                        on_click=lambda e: self.page_main_menu()
                    )
        self.page.add(self.button_volver)
        self.page.update()
                

    def page_history_menu(self):
        self.page.controls.clear()

        title = ft.Text(
            value="Historial de Consultas",
            size=28,
            weight=ft.FontWeight.BOLD
        )

        subtitle = ft.Text(
            value=f"Usuario: {self.loged_user}"
        )

        rows_db = Finance.get_historial(self.loged_user, self.db)

        rows = []
        for fecha, fuente, indicador, valor in rows_db:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(fecha.strftime("%Y-%m-%d %H:%M:%S"))),
                        ft.DataCell(ft.Text(fuente)),
                        ft.DataCell(ft.Text(indicador)),
                        ft.DataCell(ft.Text(str(valor))),
                    ]
                )
            )

        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Fecha")),
                ft.DataColumn(ft.Text("Fuente")),
                ft.DataColumn(ft.Text("Indicador")),
                ft.DataColumn(ft.Text("Valor")),
            ],
            rows=rows
        )

        btn_back = ft.Button(
            content=ft.Text("Volver al menú"),
            on_click=lambda e: self.page_main_menu()
        )

        self.page.add(
            title,
            subtitle,
            table,
            btn_back
        )

        self.page.update()

    def handle_indicator(self, indicador: str):
        finance = Finance()
        valor = None
        if indicador:
            if indicador == "uf":
                valor = finance.get_uf()
            elif indicador == "ivp":
                valor = finance.get_ivp()
            elif indicador == "ipc":
                valor = finance.get_ipc()
            elif indicador == "utm":
                valor = finance.get_utm()
            elif indicador == "dolar":
                valor = finance.get_usd()
            elif indicador == "euro":
                valor = finance.get_eur()
            if valor is not None:
                Finance.guardar_indicadores(
                    db=self.db,
                    username=self.loged_user,
                    fuente="https://mindicador.cl/api",
                    indicador=indicador,
                    valor=valor
                )
                self.page.controls.clear()
                self.text_title_main_menu = ft.Text(
                    value="Main Menu",
                    color="#cc0000",
                    size=32,
                    weight=ft.FontWeight.BOLD
                    
                )
                self.button_volver= ft.Button(
                    content=ft.Text("Volver al menú principal"),
                    on_click=lambda e: self.page_indicator_menu()
                )
                self.text_welcome = ft.Text(
                    value=f"Hola {self.loged_user}"
                )
                self.page.add(
                    self.text_title_main_menu,
                    self.text_welcome,
                    self.button_volver,
                    ft.Text(value=f"El valor de {indicador.upper()} es: {valor}")
                )
                self.page.update()
# ---------------- Cerrar sesión ----------------
    def handle_logout(self):
        
        Auth.logout(
            db=self.db,
            username=self.loged_user,
            id=self.loged_user_id
        )
        self.loged_user = ""
        self.loged_user_id = 0
        self.page_login()



if __name__ == "__main__":
    ft.app(target=App)




