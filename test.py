
from main import EasyDB

dbms = EasyDB()


humansDB = dbms.use("humans").collection("relatives")
print(humansDB.get())

# humansDB.insert({
#     "name": "Radhika Nalegave",
#     "age": 10
# })
# print(humansDB.get())


programmingLanguages = dbms.use(
    "programming-languages").collection("languages")

print(programmingLanguages.get())
print(programmingLanguages.doc({
    "type": "General Purpose"
}))

programmingLanguages.delete_many({
    "full_form": "Hyper Text Markup Language"
})

print(programmingLanguages.get())

programmingLanguages.update_many({"type": "General Purpose"}, {
                                 "remark": "My Favorite"})

print(programmingLanguages.get())
