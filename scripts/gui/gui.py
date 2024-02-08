import flet

def ControlPanel():
    items = []

    #add "New file" button

    items.append(flet.Container(content=flet.IconButton(icon=flet.icons.ADD, on_click=lambda e: print("ADD NEW ONE"))))

    #add "Open File"
    items.append(flet.Container(content=flet.IconButton(icon=flet.icons.FOLDER_OPEN, on_click=lambda e: print("OPEN NEW ONE"))))

    #add "Run"
    items.append(flet.Container(content=flet.IconButton(icon=flet.icons.PLAY_ARROW, on_click=lambda e: print("RUN"))))


    panel = flet.Row(controls=items)

    return panel

def CodePlace():

    text_field = flet.TextField(multiline=True, border="NONE", label="Code")

    return text_field

def Console():

    return flet.Text("IDK")

def CreateWorkflow():

    return flet.Column(controls=[flet.Container(flet.Icon(flet.icons.CIRCLE))])


def main(page: flet.Page):
    def CreateLeftColumn():
        items = []
        items.append(ControlPanel())
        items.append(CodePlace())
        #items.append(Console())

        return items

    left_column = flet.Column(controls=CreateLeftColumn())

    main_row = flet.Row(controls=[left_column, CreateWorkflow()])

    page.add(main_row)

    


flet.app(target=main)