import FreeSimpleGUI as sg
from converters14 import convert

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
result_label = sg.Text(key = "conversion_result", text_color="yellow")
window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button], [result_label]])

while True:
    event, values = window.read()
    print(event, float(values["feet"]), float(values["inches"]))
    feet = float(values["feet"])
    inches = float(values["inches"])
    result = convert(feet, inches)
    window["conversion_result"].update(value = "Conversion result" + str(
        result))

window.close()