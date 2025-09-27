from flask import Flask, render_template, redirect, url_for,request
from pymongo import MongoClient
from urllib.parse import quote_plus
import datetime

app = Flask(__name__,template_folder='templates')

# # Properly escape the username and password
username = quote_plus("Tara")
password = quote_plus("Tara@1234")
uri = f"mongodb+srv://{username}:{password}@cluster0.3gsaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Connect to MongoDB Atlas
client = MongoClient(uri)
db = client["Smart_Attendance"]  # Your database
# students_collection = db["TY-C"]  # Adjust collection as needed
print("connected successfully!")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check_attendance')
def check_attendance():
    return render_template('years.html')

# @app.route('/first_year')
# def first_year():
#     return render_template('subjects.html')

@app.route('/first_year')
def first_year():
    subjects = ["DBE", "Graphics", "Web Developement"]  # Example subjects list
    return render_template('subjects.html', subjects=subjects)
  
@app.route('/subject/<subject_name>')
def subject_page(subject_name):
        return render_template('subject_page.html', subject=subject_name)  

@app.route('/view_average_attendance/<subject_name>')
def view_average_attendance(subject_name):
    # Logic to fetch average attendance data if needed
    # Retrieve all documents from the MongoDB collection
    students_collection = db["TY-C"]  # Adjust collection as needed
    data = list(students_collection.find()) 
    # print(data) # Converts the cursor to a list for easier template rendering
    return render_template('view_average_attendance.html', subject=subject_name,data=data)


@app.route('/view_Daily_attendance/<subject_name>')
def view_Daily_attendance(subject_name):
    return render_template('view_Daily_attendance.html', subject=subject_name)

# Function to determine the collection name based on date
def get_collection_name(selected_date):
    # Assuming you have a naming format for collections like "attendance_YYYYMMDD"
    date_str = selected_date.strftime("%Y-%m-%d")
    return f"attendance_{date_str}"

@app.route('/show_attendance', methods=['POST'])
def show_attendance():
    # Get the selected date from the form
    selected_date = request.form['attendance_date']
    date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")

    # Get the collection name based on the date
    collection_name = get_collection_name(date_obj)
    collection = db[collection_name]

    # Retrieve attendance data from MongoDB
    attendance_records = collection.find()

    # Render the results as a table on the front end
    return render_template('attendance_table.html', records=attendance_records)

if __name__ == '__main__':
    app.run(debug=True)
