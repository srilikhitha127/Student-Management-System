from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import sqlite3

def get_connection():
    connection=sqlite3.connect(
        "students.db"
    )
    return connection
        
get_connection()
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    marks INTEGER NOT NULL,
    image TEXT,
    gender TEXT NOT NULL,
    status TEXT NOT NULL,
    course TEXT NOT NULL
    )
    """
    cursor.execute(q)
    connection.commit()
    connection.close()
create_table()


templates=Jinja2Templates(
    directory="templates"
)

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")  

@app.get("/")
def homepage(req: Request):
    return templates.TemplateResponse(
    request= req,
    name="homepage.html",
    context={}
    )
    
@app.get('/home')
def students(req:Request):
    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM students"
    students = cursor.execute(q).fetchall()
    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"stds": students}
    )
    
@app.get("/students/add")
def sending_student_form(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="add.html",
        context={}
        
    )
    

@app.get("/students/attendance")
def student_attendance(req: Request, status: str = "present"):

    connection = get_connection()
    cursor = connection.cursor()

    # Total students count
    cursor.execute("SELECT COUNT(*) FROM students")
    all_count = cursor.fetchone()[0]

    # Present students count
    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE status = ?",
        ("1",)
    )
    present_count = cursor.fetchone()[0]

    # Absent students count
    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE status = ?",
        ("0",)
    )
    absent_count = cursor.fetchone()[0]

    # Display students according to selected status
    if status == "absent":

        cursor.execute(
            "SELECT * FROM students WHERE status = ? ORDER BY id",
            ("0",)
        )

    else:

        status = "present"

        cursor.execute(
            "SELECT * FROM students WHERE status = ? ORDER BY id",
            ("1",)
        )

    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="attendance.html",
        context={
            "students": students,
            "all_count": all_count,
            "present_count": present_count,
            "absent_count": absent_count,
            "status": status
        }
    )

    
@app.get("/students/courses")
def courses(req: Request, course: str = "PYTHON"):

    connection = get_connection()
    cursor = connection.cursor()

    q = """
    SELECT * FROM students
    WHERE UPPER(course) = ?
    """

    cursor.execute(q, (course.upper(),))
    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="courses.html",
        context={
            "students": students,
            "selected_course": course.upper()
        }
    )
    
@app.get("/students/marks")
def student_marks(req: Request, course: str = "PYTHON"):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM students WHERE course = ?"
    cursor.execute(q, (course.upper(),))

    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="marks.html",
        context={
            "students": students,
            "course": course.upper()
        }
    )
@app.get("/students/records")
def student_records(req: Request, sort: str = "all"):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()

    connection.close()

    # Top 3 students based on marks
    top_three = sorted(
        all_students,
        key=lambda std: int(std[3] or 0),
        reverse=True
    )[:3]

    # Sorting options
    if sort == "top":
        students = sorted(
            all_students,
            key=lambda std: int(std[3] or 0),
            reverse=True
        )

    elif sort == "bottom":
        students = sorted(
            all_students,
            key=lambda std: int(std[3] or 0)
        )

    else:
        students = sorted(
            all_students,
            key=lambda std: int(std[0])
        )

    return templates.TemplateResponse(
        request=req,
        name="records.html",
        context={
            "students": students,
            "top_three": top_three,
            "sort": sort,
            "total_students": len(all_students),
            "course_icons": {
                "PYTHON": "🐍",
                "MERN": "🌐",
                "FULL STACK": "💻",
                "JAVA": "☕",
                "HTML": "🌐",
                "CSS": "🎨"
            }
        }
    )
@app.get("/students/{std_id}")
def single_student_details(req: Request,std_id: int):
    connection=get_connection()
    cursor=connection.cursor()
    q="select * from students where id=?"
    cursor.execute(q,(std_id,))
    students=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={
            "std":students
        }
    )
    
    
@app.post("/students/add")
def create_student_form(
    name=Form(),
    age=Form(),
    marks=Form(),
    image=Form(),
    gender=Form(),
    status=Form(),
    course= Form()
):
    class Student(BaseModel):
        name: str
        age: int
        marks: int
        image: str
        gender: str
        status: str
        course: str

    student_data = Student(
        name=name,
        age=int(age),
        marks=int(marks),
        image=image,
        gender=gender,
        status=status,
        course=course
    )
    values = (
        student_data.name,
        student_data.age,
        student_data.marks,
        student_data.image,
        student_data.gender,
        student_data.status,
        student_data.course
    )
    connection = get_connection()
    q = """
    INSERT INTO students(name, age, marks, image, gender, status,course)
    VALUES (?, ?, ?, ?, ?, ?,?)
    """
    connection.execute(q, values)
    connection.commit()
    connection.close()

    return RedirectResponse(url="/home", status_code=303)


@app.get("/students/delete/{std_id}")
def delete_student(std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "DELETE FROM students WHERE id = ?"
    cursor.execute(q, (std_id,))

    connection.commit()
    connection.close()

    return RedirectResponse(url="/home", status_code=303)

@app.get("/students/update/{std_id}")
def update_student(req: Request ,std_id: int):
    connection=get_connection()
    cursor=connection.cursor()
    q="SELECT * FROM students WHERE id=?"
    cursor.execute(q,(std_id,))
    student=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
            request=req,
            name="edit-std.html",
            context={
                "std":student
            }
        ) 

@app.post("/students/update/{std_id}")
def update_student_details(
    std_id: int,
    name= Form(),
    age= Form(),
    marks: int = Form(),
    image= Form(),
    gender = Form(),
    status= Form(),
    course= Form()
):

    connection = get_connection()
    cursor = connection.cursor()

    q = """
    UPDATE students
    SET name=?, age=?, marks=?, image=?,
        gender=?, status=?, course=?
    WHERE id=?
    """

    values = (
        name,
        age,
        marks,
        image,
        gender,
        status,
        course,
        std_id
    )

    cursor.execute(q, values)

    connection.commit()
    connection.close()

    return RedirectResponse(url="/home", status_code=303)
