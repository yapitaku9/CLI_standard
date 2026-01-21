import os

# import sys
from dotenv import load_dotenv
from peewee import CharField, IntegerField, Model
from playhouse.db_url import connect

# .envの読み込み
load_dotenv(override=True)

# データベースへの接続
# db = SqliteDatabase("peewee_db.sqlite")
db = connect(os.environ.get("DATABASE"))
# db = connect(os.environ.get("DATABASE") or "sqlite://peewee_db.sqlite")


# メッセージのモデル
class User(Model):

    id = IntegerField(primary_key=True)
    user = CharField()
    age = IntegerField()

    class Meta:
        database = db
        table_name = "user"


db.create_tables([User])
