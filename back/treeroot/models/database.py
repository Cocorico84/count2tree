from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'tree',
    user='tree',
    password='tree',
    host='localhost',
    autorollback=True,
    port='5555:5432'
)
