
import PySimpleGUI as sg

layout = [[sg.Text("Hello from ModoTech Softwares")], [sg.Button("Cool")],[sg.Button("Nope")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Nope" or event == "Cool" or event == sg.WIN_CLOSED:
        break

window.close()