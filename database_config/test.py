import sqlalchemy as db 
from sqlalchemy import MetaData
from sqlalchemy import Table 
from sqlalchemy import Column

engine = db.create_engine('postgresql://sahilc:pgxtpp5k@database-1.cptcfbaucaoy.us-east-1.rds.amazonaws.com/postgres')

driver = engine.connect()

metadata_obj = MetaData()

table = Table('gumball-logging', metadata_obj,
    Column('user_id', db.Integer, primary_key=True),
    Column('name', db.String(16), nullable=False),
    Column('last_gumball_time', db.DateTime, nullable = True)
)

table.create(driver)

print(len(metadata_obj.tables))