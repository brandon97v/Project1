from application import db 

class Tasks(db.model):
    id = db.column()            
    description = db.column(db.string(db.string(255), nullable=False, unique=True)
    completed = db.column(db.Bolean, nullable=False)

