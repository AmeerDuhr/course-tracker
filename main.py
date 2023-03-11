import sqlite3

# Constants
def sep(): print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
courses = []
with open('./tracking.txt','r') as trackingFileRead:
    trackingType = trackingFileRead.readline()
db = sqlite3.connect("./courses.db")
cr = db.cursor()

# Create table
cr.execute(
    "CREATE TABLE if not exists 'courses' (id INTEGER NOT NULL, name TEXT NOT NULL, current INTEGER NOT NULL, goal INTEGER NOT NULL, unit TEXT NOT NULL, CONSTRAINT courses_pk PRIMARY KEY(id));")

# Show list of courses
cr.execute("SELECT * FROM courses")
courses = cr.fetchall()
if len(courses) != 0:
    for c in courses:
        tracking = ""
        if trackingType == "percent":
            if c[3] != 0:
                percent = c[2] * 100 / c[3]
                tracking = "%" + "{:.0f}".format(percent)
            else: tracking = "%100"
        elif trackingType == "star":
            if c[3] != 0:
                starsBefore = c[2] * 5 / c[3]
                starsAfter = float("{:.2f}".format(starsBefore))
                if starsAfter == 0: tracking = "☆☆☆☆☆"
                elif starsAfter >= 1 and starsAfter < 2: tracking = "★☆☆☆☆"
                elif starsAfter >= 2 and starsAfter < 3: tracking = "★★☆☆☆"
                elif starsAfter >= 3 and starsAfter < 4: tracking = "★★★☆☆"
                elif starsAfter >= 4 and starsAfter < 5: tracking = "★★★★☆"
                elif starsAfter == 5: tracking = "★★★★★"
            else: tracking = "★★★★★"
        print(f"{c[0]} {c[1]} \t{c[2]} out of {c[3]} {c[4]} \t{tracking}")
else:
    print("No courses.")
sep()

# Select operation
print("[1] Edit \t[2] Add \t[3] Delete \t[4] Tracking Mode")
index = input("Select an index: ")
operation = int(index)
if operation == 4: # Changing tracking mode/type
    sep()
    print("[1] Percentage \t[2] Stars")
    trackingTypeIndex = input("Index: ")
    trackingFileWrite = open('./tracking.txt','w')
    if int(trackingTypeIndex) == 1:
        trackingFileWrite.write("percent")
        trackingFileWrite.close()
    elif int(trackingTypeIndex) == 2:
        trackingFileWrite.write("star")
        trackingFileWrite.close()
    else: print("Out of index...")
elif operation == 3 or operation == 1: # Not adding a new course
    indexCourse = input("Select course by id: ")
    cr.execute(f"SELECT * FROM courses WHERE id={indexCourse};")
    course = cr.fetchone()
    if str(course) != "None":
        if operation == 3: # Delete
            cr.execute(f"DELETE FROM courses WHERE id={indexCourse};")
            db.commit()
        elif operation == 1: # Edit
            print("Leave empty if you don't want to change...")
            name = input("New name: ")
            if name == '': name = course[1]
            current = input("New current: ")
            if current == '': current = course[2]
            goal = input("New goal: ")
            if goal == '': goal = course[3]
            unit = input("New unit: ")
            if unit == '': unit = course[4]
            cr.execute(f"UPDATE courses SET name='{name}',current={current},goal={goal},unit='{unit}' WHERE id={indexCourse};")
            db.commit()
    else: print("Out of index...")
elif operation == 2: # Add
    name = input("Name: ")
    current = input("Current: ")
    goal = input("Goal: ")
    unit = input("Unit: ")
    cr.execute(f"INSERT INTO courses (name, current, goal, unit) VALUES ('{name}',{current},{goal},'{unit}');")
    db.commit
else:
    print("Out of index...")

# Close DB
db.commit()
db.close()