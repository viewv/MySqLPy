import pymysql
from Database import Database

database = Database()

_host = database.gethost()
_port = database.getport()
_sql_user = database.getuser()
_sql_password = database.getpassword()
_database = database.getdatabase()


def comment(id, message):  # id is user's id message: string
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()