from dbModel import db, localDb

#Creates all the tables from dbModels.py

db.create_all()

lokal1 = localDb(8)
lokal2 = localDb(2)

print(lokal1.local_id)
print(lokal2.local_id)

db.session.add_all([lokal1, lokal2])
db.session.commit()

print(f"{lokal1.id} och {lokal1.local_id}")

print(lokal2.id)
