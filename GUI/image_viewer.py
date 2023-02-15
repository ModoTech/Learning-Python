import PySimpleGUI as modo
import os.path

# First the window layout in 2 columns

file_list_column = [
    [
        modo.Text("Image Folder"),
        modo.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        modo.FolderBrowse(),
    ],
    [
        modo.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [modo.Text("Choose an image from list on left:")],
    [modo.Text(size=(40, 1), key="-TOUT-")],
    [modo.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        modo.Column(file_list_column),
        modo.VSeperator(),
        modo.Column(image_viewer_column),
    ]
]

window = modo.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == modo.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()