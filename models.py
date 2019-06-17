from graphene import ObjectType, String, Schema , Field

def hola(name):
    return {"first_name": name, "last_name": "D2"}
   
def listData():
    return [{"username": "n1", "id": 1} , {"username": "n1", "id": 2}]

def listpost():
    return [{"title": "n1", "content": 1} , {"title": "n1", "content": 2}]
   
def listDataid(ids):
    return {"first_name": ids, "last_name": "D2"}