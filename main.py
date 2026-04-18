from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import csv
from datetime import datetime

FILENAME = "overtime_records.csv"

class OvertimeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.date_input = TextInput(hint_text='日期 YYYY-MM-DD（可空）', multiline=False)
        self.hours_input = TextInput(hint_text='加班小时数', multiline=False)
        self.note_input = TextInput(hint_text='备注', multiline=False)

        self.add_btn = Button(text='添加记录')
        self.add_btn.bind(on_press=self.add_record)

        self.view_btn = Button(text='查看记录')
        self.view_btn.bind(on_press=self.view_records)

        self.output = Label(text='记录显示区', size_hint_y=None, height=200)

        self.layout.add_widget(self.date_input)
        self.layout.add_widget(self.hours_input)
        self.layout.add_widget(self.note_input)
        self.layout.add_widget(self.add_btn)
        self.layout.add_widget(self.view_btn)
        self.layout.add_widget(self.output)

        return self.layout

    def add_record(self, instance):
        date = self.date_input.text or datetime.now().strftime("%Y-%m-%d")
        try:
            hours = float(self.hours_input.text)
        except ValueError:
            self.output.text = "请输入有效数字"
            return
        note = self.note_input.text

        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, hours, note])
        self.output.text = f"已记录: {date}, {hours}小时, {note}"

    def view_records(self, instance):
        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                records = "\n".join([f"{row[0]}: {row[1]}小时, {row[2]}" for row in reader])
                self.output.text = records or "无记录"
        except FileNotFoundError:
            self.output.text = "没有记录文件"

if __name__ == "__main__":
    OvertimeApp().run()
