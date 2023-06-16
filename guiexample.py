import PySimpleGUIQt as gui

# mylayout = [
#     [s.Text("Hello World"), s.Button("OK")],
#     [s.Text("Python is cool"), s.Text("Yes")],
#     [s.Text("Learn PySimpleGUI")],
#     [s.Button("ok"),s.Button("cancel"),s.Button("fine")]
# ]
#
# window = s.Window(title="Hello World", size=(640,480), layout=mylayout)
# window.read()


form=gui.FlexForm("My Windows")
layout=[[gui.Text("Enter Your Name",size=(15,1)),gui.InputText()],
        [gui.Text("Enter Your Country",size=(15,1)),gui.InputText()],
        [gui.Text("Enter your Phone",size=(15,1)),gui.InputText()],
        [gui.Text("Enter your city",size=(15,1)),gui.InputText()],
        [gui.OK(),gui.Cancel()]]

button,values=form.layout(layout).Read()
print(layout)
print(button)
print(values)
name=values[0]
country=values[1]
phone=values[2]
city=values[3]
print(f"name is {name} , country is {country}, phone is {phone} finally city is {city}")
gui.popup(values)

#gui.preview_all_look_and_feel_themes()