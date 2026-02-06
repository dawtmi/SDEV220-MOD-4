from sqlalchemy import create_engine

engine = create_engine('sqlite:///books.db')
conn = engine.connect()

sql = "SELECT title FROM book ORDER BY title"
result = conn.execute(sql)

for row in result:
    print(row[0])

conn.close()
