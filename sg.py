import PySimpleGUI as sg
import main

sg.set_options(font=("Courier New", 10))
sg.theme('DefaultNoMoreNagging')

units = ["Books", "Videos", "Lessons", "Chapters", "Recordings"]
trackings = ["Stars", "Percent"]
table_headings = ["NAME", "CURRENT", "GOAL", "UNIT", "TRACKING"]

col0_layout = [
    [sg.Button("+1", key="increment_btn"),
     sg.Button("ADD", key="add_btn"),
     sg.Button("EDIT", key="edit_btn"),
     sg.Button("DELETE", key="delete_btn"),
     sg.Button("CLEAR", key="clear_btn")],
    [sg.Text("Name:"), sg.Input(key="name", size=(32,1))],
    [sg.Text("Current:"), sg.Input(key="current", size=(6,1), default_text='0'),
     sg.Text("Goal:"), sg.Input(key="goal", size=(6,1), default_text='0')],
    [sg.Text("Unit:"), sg.OptionMenu(values=units, key="unit", default_value=''),
     sg.Text("Tracking:"), sg.OptionMenu(values=trackings, key="tracking", default_value='')],
    [sg.Table(values=main.Courses().getCourses(), headings=table_headings, key="courses_table",
              auto_size_columns=True, justification='center', expand_x=True)]
]

layout = [
    [sg.Column(col0_layout, scrollable=False, element_justification='center', expand_x=True)]
]

window = sg.Window("Course Tracker", layout, size=(500,300), resizable=False,
                   element_justification='c', use_default_focus=False)

def clear_values():
    window['name'].update(value='')
    window['current'].update(value='0')
    window['goal'].update(value='0')
    window['unit'].update(value='')

while True:
    event, values = window.read()
    if event in ("Exit", sg.WIN_CLOSED):
        break
    elif event == "add_btn":
        try:
            name = values['name']
            current = int(values['current'])
            goal = int(values['goal'])
            unit = values['unit']
            tracking = values['tracking']
            main.Courses().addCourse(name, current, goal, unit, tracking)
            clear_values()
            window['courses_table'].update(main.Courses().getCourses())
        except:
            sg.popup("A value is incorrect.")
    elif event == "edit_btn":
        try:
            if len(values['courses_table']) != 0:
                table_courses = window['courses_table'].get()
                index = values['courses_table'][0]
                name = values['name']
                current = int(values['current'])
                goal = int(values['goal'])
                unit = values['unit']
                tracking = values['tracking']
                if name == '': name = table_courses[index][0]
                if current == 0: current = table_courses[index][1]
                if goal == 0: goal = table_courses[index][2]
                if unit == '': unit = table_courses[index][3]
                if tracking == '': tracking = table_courses[index][4]

                if "★" in tracking or "☆" in tracking: tracking = "Stars"
                elif "%" in tracking: tracking = "Percent"
                else: tracking = "Undefined"

                main.Courses().editCourse(name, current, goal, unit, tracking,
                                          table_courses[index][-1])
                clear_values()
                window['courses_table'].update(main.Courses().getCourses())
        except:
            sg.popup("A value is incorrect.")
    elif event == "delete_btn":
        if len(values['courses_table']) != 0:
            yesNo = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
            if yesNo == "No": continue
            table_courses = window['courses_table'].get()
            for i, v in enumerate(values['courses_table']):
                index = values['courses_table'][i]
                main.Courses().deleteCourse(table_courses[index][-1])
            clear_values()
            window['courses_table'].update(main.Courses().getCourses())
    elif event == "clear_btn":
        clear_values()
    elif event == "increment_btn":
        if len(values['courses_table']) != 0:
            table_courses = window['courses_table'].get()
            index = values['courses_table'][0]
            if table_courses[index][1] == table_courses[index][2]:
                sg.popup("Already reached goal")
                continue

            name = table_courses[index][0]
            current = int(table_courses[index][1]) + 1
            goal = int(table_courses[index][2])
            unit = table_courses[index][3]
            tracking = table_courses[index][4]
            if "★" in tracking or "☆" in tracking: tracking = "Stars"
            elif "%" in tracking: tracking = "Percent"
            else: tracking = "Undefined"
            main.Courses().editCourse(name, current, goal, unit, tracking, table_courses[index][-1])
            clear_values()
            window['courses_table'].Update(values=main.Courses().getCourses(), select_rows=(index, index))
window.close()
