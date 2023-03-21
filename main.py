import sqlite3

class Courses:
    def __init__(self):
        self.db = sqlite3.connect("./courses.db")
        self.cr = self.db.cursor()
        self.cr.execute(
        "CREATE TABLE if not exists 'courses' (id INTEGER NOT NULL, name TEXT NOT NULL, current INTEGER NOT NULL, goal INTEGER NOT NULL, unit TEXT NOT NULL, tracking TEXT NOT NULL, CONSTRAINT courses_pk PRIMARY KEY(id));")

    def getCourses(self):
        # Create table
        self.cr.execute("SELECT * FROM courses")
        courses = self.cr.fetchall()

        filteredCourses = []
        for c in courses:
            if c[5] == "Percent":
                if int(c[3]) != 0:
                    tracking = "%" + str(int(int(c[2]) * 100 / int(c[3])))
                else: tracking = "%100"
            elif c[5] == "Stars":
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
            else: tracking = "Undefined"
            # name, current, goal, unit, tracking, id
            filteredC = [c[1], c[2], c[3], c[4], tracking, c[0]]
            filteredCourses.append(filteredC)

        self.db.commit()
        self.db.close()

        return filteredCourses

    def addCourse(self, name, current, goal, unit, tracking):
        self.cr.execute(f"INSERT INTO courses (name, current, goal, unit, tracking) VALUES ('{name}', {current}, {goal}, '{unit}', '{tracking}');")
        self.db.commit()
        self.db.close()

    def editCourse(self, name, current, goal, unit, tracking, id):
        self.cr.execute(f"UPDATE courses SET name='{name}',current={current},goal={goal},unit='{unit}',tracking='{tracking}' WHERE id={id};")
        self.db.commit()
        self.db.close()

    def deleteCourse(self, id):
        self.cr.execute(f"DELETE FROM courses WHERE id={id};")
        self.db.commit()
        self.db.close()
