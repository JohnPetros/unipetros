from wtforms.widgets import ListWidget, CheckboxInput
from wtforms import SelectMultipleField


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()
