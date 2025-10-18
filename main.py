from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class GradeCalculator(App):
    def build(self):
        # قائمة المواد الدراسية
        self.subjects = [
            "القرآن الكريم", "التربية الإسلامية", "اللغة العربية", 
            "اللغة الإنجليزية", "الرياضيات", "الكيمياء", "الفيزياء", 
            "الأحياء", "التاريخ", "الجغرافيا", "الحاسوب", "مجتمع", 
            "سلوك", "مادة إضافية"
        ]
        
        # الواجهة الرئيسية
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # منطقة التمرير
        scroll_view = ScrollView(size_hint=(1, 0.85))
        subjects_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        subjects_layout.bind(minimum_height=subjects_layout.setter('height'))

        self.inputs = {}
        for subject in self.subjects:
            row = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=None, height=40)
            row.add_widget(Label(text=subject + ":", size_hint_x=0.4))
            grade_input = TextInput(
                input_type='number', 
                multiline=False, 
                size_hint_x=0.6,
                hint_text='أدخل الدرجة'
            )
            self.inputs[subject] = grade_input
            row.add_widget(grade_input)
            subjects_layout.add_widget(row)
        
        scroll_view.add_widget(subjects_layout)
        main_layout.add_widget(scroll_view)

        # زر الحساب
        calculate_button = Button(text='احسب المعدل', size_hint_y=None, height=50)
        calculate_button.bind(on_press=self.calculate_result)
        main_layout.add_widget(calculate_button)

        # عرض النتيجة
        self.result_label = Label(text='الناتج النهائي: 0.00', font_size=20, size_hint_y=None, height=50)
        main_layout.add_widget(self.result_label)

        return main_layout

    def calculate_result(self, instance):
        total_grade = 0.0
        valid_grades_count = 0
        
        try:
            for subject, input_widget in self.inputs.items():
                grade_str = input_widget.text.strip()
                if grade_str:
                    grade = float(grade_str)
                    if 0 <= grade <= 100:
                        # إضافة 20 درجة لكل مادة
                        adjusted_grade = grade + 20
                        total_grade += adjusted_grade
                        valid_grades_count += 1
                    else:
                        self.result_label.text = f'خطأ: درجة {subject} خارج النطاق (0-100)'
                        return
            
            if valid_grades_count > 0:
                final_average = total_grade / valid_grades_count
                self.result_label.text = f'الناتج النهائي: {final_average:.2f}'
            else:
                self.result_label.text = 'خطأ: الرجاء إدخال درجات!'

        except ValueError:
            self.result_label.text = 'خطأ: الرجاء إدخال أرقام فقط!'

if __name__ == '__main__':
    GradeCalculator().run()
#yas
