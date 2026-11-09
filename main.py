from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.03, 0.05, 0.10, 1)

class ModMenu(App):
    def build(self):
        root = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15
        )

        root.add_widget(Label(
            text='UIKI LGL MOD MENU',
            font_size=25,
            bold=True
        ))

        self.status = Label(text='STATUS: OFF')

        btn = Button(
            text='ON / OFF',
            size_hint=(1, .3)
        )
        btn.bind(on_press=self.toggle)

        root.add_widget(self.status)
        root.add_widget(btn)

        return root

    def toggle(self, instance):
        if self.status.text == 'STATUS: OFF':
            self.status.text = 'STATUS: ON'
        else:
            self.status.text = 'STATUS: OFF'

ModMenu().run()
