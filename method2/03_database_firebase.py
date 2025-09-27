import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://attendance-system-real-t-8dbc0-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
       
         "2223000132":{
        "name": "Shantanu Mahadik",
        "total_attendance": 75,
    },
    
        "2223000139":{
        "name": "Pradnya Mahadik",
        "total_attendance": 75,
    },
    
         "2223000872":{
        "name": "Utkarsha Kavathekar",
        "total_attendance": 75,
    },
    
         "2223000185":{
        "name": "Sakshi Nakate",
        "total_attendance": 75,
    },
    
         "2223000383":{
        "name": "Chahat Pathan",
        "total_attendance": 75,
    },
    
         "2223000870":{
        "name": "Sayli Patil",
        "total_attendance": 75,
    }
}
    
for key,value in data.items():
    ref.child(key).set(value)