
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

GREEN = (0.1, 1, 0.35, 1)
BLACK = (0.015, 0.025, 0.02, 1)

class CyberTerminal(App):

    def build(self):
        Window.clearcolor = BLACK

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="[b]UMAR X1[/b]\nCYBER TERMINAL v1.0",
            markup=True,
            color=GREEN,
            font_size="27sp",
            size_hint_y=0.17
        )
        root.add_widget(title)

        self.output = Label(
            text="SYSTEM INITIALIZED\nWelcome to UMAR X1\nType help to begin.\n",
            color=GREEN,
            halign="left",
            valign="top",
            font_size="14sp"
        )
        self.output.bind(
            size=lambda obj, size:
            setattr(obj, "text_size", size)
        )
        root.add_widget(self.output)

        self.command = TextInput(
            hint_text="Enter command...",
            multiline=False,
            size_hint_y=0.1,
            foreground_color=GREEN,
            background_color=(0.03, 0.08, 0.04, 1),
            cursor_color=GREEN
        )
        self.command.bind(on_text_validate=self.run_command)
        root.add_widget(self.command)

        button = Button(
            text="EXECUTE",
            size_hint_y=0.12,
            background_color=(0.02, 0.3, 0.1, 1),
            color=GREEN
        )
        button.bind(on_press=self.run_command)
        root.add_widget(button)

        return root

    def run_command(self, instance):
        cmd = self.command.text.strip()
        self.command.text = ""

        if not cmd:
            return

        if cmd == "help":
            result = "COMMANDS:\nhelp\nabout\ntime\nstatus\nscan\necho\nclear"

        elif cmd == "about":
            result = "UMAR X1 CYBER TERMINAL\nVersion 1.0\nRootless Android app."

        elif cmd == "time":
            result = datetime.now().strftime("%H:%M:%S")

        elif cmd == "status":
            result = "SYSTEM: ONLINE\nAPP: RUNNING\nSECURITY: ROOTLESS"

        elif cmd == "scan":
            result = "DEMO MODE\nNo real network scan performed."

        elif cmd.startswith("echo "):
            result = cmd[5:]

        elif cmd == "clear":
            self.output.text = ""
            return

        else:
            result = "Unknown command. Type help."

        self.output.text += f"\n> {cmd}\n{result}\n"

CyberTerminal().run()
0

