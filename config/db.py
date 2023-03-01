
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,DateTime

engine = create_engine("mariadb+pymysql://root:MasterHunter@10.72.0.2:3306/demos?charset=utf8mb4")

meta = MetaData()

conn = engine.connect()
