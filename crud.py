from dbModel import db, localDb

## CREATE

new_local = localDb(6)

db.session.add(new_local)
db.session.commit()

## READ

all_locals = localDb.query.all() # List of all locals

for i, obj in enumerate(all_locals):
    i+=1
    print(f"{i}. {obj}")

# Select a post by ID
postnr = 10
thePost = localDb.query.get(postnr)
print(f"Postnr: {postnr} = {thePost.local_id}")

# Filter
local_nr3 = localDb.query.filter_by(local_id = 6)
print(local_nr3.all())
## UPDATE
