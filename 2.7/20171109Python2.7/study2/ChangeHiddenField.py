import mechanize

form=mechanize.Browser().select_form('')
form.find_control("foo").readonly = False # allow changing .value of control foo
form.set_all_readonly(False) # allow changing the .value of all controls