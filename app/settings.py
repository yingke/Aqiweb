class Config:
    DEBUG = True
def get_db_uri(dbinfo):
    ENGINE = dbinfo.get("ENGINE")or 'mysql'
    DRIVER = dbinfo.get("DRIVER")or 'pymysql'
    USER = dbinfo.get("USER") or 'root'
    PASSWORLD = dbinfo.get("PASSWORLD") or '900911'
    HOST = dbinfo.get("HOST") or 'localhost'
    PORT = dbinfo.get("PORT") or '3306'
    NAME = dbinfo.get("NAME")or 'hebeiaqi'
    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE,DRIVER,USER,PASSWORLD,HOST,PORT,NAME)


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        "ENGINE" :"mysql",
        "DRIVER" :"pymysql",
        "USER" :"root",
        "PASSWORLD" :"900911",
        "HOST" :"127.0.0.1",
        "PORT" :"3306",
        "NAME" :"hebeiaqi"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
    pass


envs = {
    "develop":DevelopConfig
}
