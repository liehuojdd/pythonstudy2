import bisect
import mechanize

def closest_int_value(form, ctrl_name, value):
    values = map(int, [item.name for item in form.find_control(ctrl_name).items])
    return str(values[bisect.bisect(values, value) - 1])

form=mechanize.Browser().select_form('')
form["distance"] = [closest_int_value(form, "distance", 23)]