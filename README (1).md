# 🎓 Student Management System

> 🚀 A learning project built while practising Full Stack Development
> using **Python, FastAPI, SQLite, HTML, CSS, and Jinja2 Templates**.

This application provides a web interface to manage student information,
track attendance, view course-wise records, manage marks, and identify
top-performing students.

------------------------------------------------------------------------

## ✨ Key Features

### 👨‍🎓 Student Management (CRUD)

-   ➕ **Create:** Add new student records.
-   🔍 **Read:** View all registered students.
-   👤 View individual student details using Student ID.
-   ✏️ **Update:** Edit existing student information.
-   🗑️ **Delete:** Remove student records.

### 📋 Attendance Management

-   👥 View total student count.
-   ✅ View present student count.
-   ❌ View absent student count.
-   📊 Filter students based on attendance status (Present / Absent).

### 📚 Course Management

-   📖 View students based on different courses.
-   🔍 Filter students course-wise.
-   👨‍🎓 Display student details according to the selected course.

### 📝 Marks Management

-   📊 View course-wise student marks.
-   🏆 Display the Top 3 students based on marks.
-   🔄 Sort student records based on highest and lowest marks.

### 📑 Student Records

-   📋 View all student records.
-   🔢 Display total student count.
-   🏅 Identify top-performing students.
-   🔃 Sort records based on Student ID, highest marks, and lowest
    marks.

------------------------------------------------------------------------

## 🛠️ Technologies & Concepts Used

  Technology    Purpose
  ------------- -------------------------------------------
  🐍 Python     Application logic and backend programming
  ⚡ FastAPI    Backend development and routing
  🗄️ SQLite     Database connectivity and data storage
  🌐 HTML       Web page structure
  🎨 CSS        Styling and page design
  📄 Jinja2     Dynamic HTML templates
  ✅ Pydantic   Student data model and validation
  🚀 Uvicorn    Running the FastAPI application

------------------------------------------------------------------------

## 🗄️ Database Structure

The application uses an SQLite database named `students.db`. The
`students` table is created automatically if it does not already exist.

  Column     Data Type
  ---------- ---------------------------------------
  `id`       INTEGER (Primary Key, Auto Increment)
  `name`     TEXT
  `age`      INTEGER
  `marks`    INTEGER
  `image`    TEXT
  `gender`   TEXT
  `status`   TEXT
  `course`   TEXT

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Student-Management-System/
│
├── 🐍 main.py
├── 🗄️ students.db
│
├── 📂 templates/
│   ├── homepage.html
│   ├── home.html
│   ├── add.html
│   ├── edit-std.html
│   ├── single-std.html
│   ├── attendance.html
│   ├── courses.html
│   ├── marks.html
│   └── records.html
│
└── 📂 static/
    └── CSS, images, and other static files
```

*The template names above are based on the names referenced in
`main.py`. Adjust the structure if your actual filenames differ.*

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone or download the repository

``` bash
git clone <your-repository-url>
cd Student-Management-System
```

### 2️⃣ Create a virtual environment

``` bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

**Windows**

``` bash
venv\Scripts\activate
```

**macOS / Linux**

``` bash
source venv/bin/activate
```

### 4️⃣ Install the required packages

``` bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 5️⃣ Run the application

``` bash
uvicorn main:app --reload
```

### 6️⃣ Open the application in your browser

🌐 **Application:** http://127.0.0.1:8000/

📖 **FastAPI API Documentation:** http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🔗 Main Application Routes

  -----------------------------------------------------------------------------
  Method                  Route                         Functionality
  ----------------------- ----------------------------- -----------------------
  GET                     `/`                           Display the homepage

  GET                     `/home`                       Display all students

  GET                     `/students/add`               Display the add-student
                                                        form

  POST                    `/students/add`               Save student details

  GET                     `/students/{std_id}`          View individual student
                                                        details

  GET                     `/students/update/{std_id}`   Display the update form

  POST                    `/students/update/{std_id}`   Save updated student
                                                        details

  GET                     `/students/delete/{std_id}`   Delete a student

  GET                     `/students/attendance`        Display attendance
                                                        information

  GET                     `/students/courses`           Display course-wise
                                                        students

  GET                     `/students/marks`             Display course-wise
                                                        marks

  GET                     `/students/records`           Display student
                                                        records, sorting, and
                                                        top-three ranking
  -----------------------------------------------------------------------------

------------------------------------------------------------------------

## 💡 Learning Outcomes

Through this project, I am practising:

-   🧩 Building backend routes with FastAPI.
-   🔌 Connecting Python applications to an SQLite database.
-   🔄 Performing CRUD operations using SQL queries.
-   📝 Handling HTML form submissions.
-   🧱 Passing database records to Jinja2 templates.
-   🖥️ Displaying dynamic student information.
-   📊 Implementing attendance management and course-wise filtering.
-   🏆 Displaying marks, ranking students, and sorting records.

------------------------------------------------------------------------

## 🚧 Project Status

This is a learning project that I am developing step by step as part of
my Full Stack Development learning journey. I am implementing features
gradually to strengthen my practical understanding of backend
development, database operations, and frontend-backend integration.
