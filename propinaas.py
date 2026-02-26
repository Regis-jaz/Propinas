import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Servicio"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_total = ft.TextField(
        label="Monto del consumo",
        text_align=ft.TextAlign.CENTER,
        width=200,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    txt_resultado = ft.TextField(
        label="Importe final",
        text_align=ft.TextAlign.CENTER,
        width=200,
        disabled=True
    )

    txt_mensaje = ft.Text("", text_align=ft.TextAlign.CENTER)

    slider_propina = ft.Slider(
        min=0,
        max=25,
        divisions=7,
        value=5,
        label="{value}%",
        width=200
    )

    def calcular(e):
        if txt_total.value == "":
            txt_mensaje.value = "Por favor ingresa un monto"
            page.update()
            return

        total = float(txt_total.value)
        porcentaje = slider_propina.value
        propina = total * (porcentaje / 100)

        txt_resultado.value = f"{total + propina:.2f}"
        txt_mensaje.value = f"El extra por servicio sería {propina:.2f} pesos"
        page.update()

    btn = ft.ElevatedButton("Calcular total", on_click=calcular)

    page.add(
        ft.Column(
            [
                txt_total,
                ft.Text("Elige el porcentaje de servicio"),
                slider_propina,
                btn,
                txt_resultado,
                txt_mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
