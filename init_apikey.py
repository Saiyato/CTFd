import os
import sqlalchemy
import time
DATABASE_URL = f"sqlite:///{os.path.dirname(os.path.abspath(__file__))}/CTFd/ctfd.db"
connection = sqlalchemy.create_engine(DATABASE_URL)

print("Trying to initialise a token for setup...\n")
q="SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tokens'"
try:
  match=connection.execute(q).fetchone()
  while match is not None and match[0]!=1:
    match=connection.execute(q).fetchone()
    time.sleep(0.5)
    print(".", end="")

  if match[0]==1:
    q="INSERT INTO tokens VALUES(1, 'user', 1, '2001-01-01 00:00:00.000000', '2099-01-01 00:00:00.000000', '{INSERT_TOKEN}')"
    try:
      insert=connection.execute(q)
    except Exception as err:
      print(f"Could not insert init-token with error: {err}") 
  else:
    print("Could not insert init-token, because the table 'tokens' does not exist.")
except Exception as ex:
  print(f"Statement failed with error: {ex}")

print("Done! Token ready to use.")