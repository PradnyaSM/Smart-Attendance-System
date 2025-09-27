from flask import Flask, render_template, request
from pymongo import MongoClient
from urllib.parse import quote_plus
from flask_socketio import SocketIO
import threading
import datetime

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app)

# MongoDB Connection
username = quote_plus("Tara")
password = quote_plus("Tara@1234")
uri = f"mongodb+srv://{username}:{password}@cluster0.3gsaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["Smart_Attendance"]
print("Connected successfully!")

# Function to monitor MongoDB changes
def monitor_changes():
    """
    Monitor MongoDB Change Streams and notify the frontend on updates.
    """
    pipeline = [{"$match": {"operationType": {"$in": ["insert", "update", "delete"]}}}]
    with db.watch(pipeline) as stream:
        for change in stream:
            print("Change detected:", change)
            socketio.emit('database_update', {'message': 'Database updated', 'change': change}, broadcast=True)

# Start monitoring in a background thread
threading.Thread(target=monitor_changes, daemon=True).start()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check_attendance')
def check_attendance():
    return render_template('years.html')

@app.route('/first_year')
def first_year():
    subjects = ["DBE", "Graphics", "Web Development"]
    return render_template('subjects.html', subjects=subjects)

@app.route('/subject/<subject_name>')
def subject_page(subject_name):
    return render_template('subject_page.html', subject=subject_name)

@app.route('/view_average_attendance/<subject_name>')
def view_average_attendance(subject_name):
    students_collection = db["TY-C"]
    data = list(students_collection.find())
    return render_template('view_average_attendance.html', subject=subject_name, data=data)

@app.route('/show_attendance', methods=['POST'])
def show_attendance():
    selected_date = request.form['attendance_date']
    date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    collection_name = f"attendance_{date_obj.strftime('%Y-%m-%d')}"
    collection = db[collection_name]
    attendance_records = list(collection.find())
    return render_template('attendance_table2.html', records=attendance_records)

if __name__ == '__main__':
    socketio.run(app, debug=True)
