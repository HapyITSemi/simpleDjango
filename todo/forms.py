# django.forms.ModelFormは
# Modelクラスを元にFieldを自動的に生成してくれるクラスです
# 検索で使う入力項目はFormを、
# 登録・更新で使う入力項目はModelFormを利用する
#

from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'due_date', 'created_at', 'updated_at', 'todo_category_id']


# widgetsで各フィールドのデザインを指定する
