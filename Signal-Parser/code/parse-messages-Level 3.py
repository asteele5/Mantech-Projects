#Connect to database
from sqlcipher3 import dbapi2 as sqlcipher
from tabulate import tabulate

db = sqlcipher.connect('/home/ubuntu/Downloads/Signal/sql/db.sqlite')

db.execute('PRAGMA key = "x\'f0fdad64e7e0a677dc69e24874762cea6a742a74761e359ea01a6cd1f40f0bff\'"')

db.execute('pragma cipher_compatibility = 3')

#Prints a list of tables in the database
print('List of tables in database: \n')
for table in db.execute('SELECT name FROM sqlite_master WHERE type="table" ORDER BY name ASC;').fetchall():
	print(table[0])

print('\n')

#Prints content of each message along with the phone number and whether each message was incoming or outgoing in a table format
print('List of messages in database: \n')
print(tabulate(db.execute('SELECT body, type, conversationID FROM messages ORDER BY sent_at ASC;').fetchall()))
