import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds035683.mlab.com:35683/tmh-database

host = "ds035683.mlab.com"
port = 35683
db_name = "tmh-database"
username = "minhhieu"
password = "minhhieu"
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)
def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]
def item2json(item):
    import json
    return json.loads(item.to_json())