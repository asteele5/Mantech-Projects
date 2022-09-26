#Connect to database
from sqlcipher3 import dbapi2 as sqlcipher

db = sqlcipher.connect('/home/ubuntu/Downloads/Signal/sql/db.sqlite')

db.execute('PRAGMA key = "x\'f0fdad64e7e0a677dc69e24874762cea6a742a74761e359ea01a6cd1f40f0bff\'"')

db.execute('pragma cipher_compatibility = 3')

#Header of text file
with open('messages.txt', 'w') as f:
	f.write('o = outgoing message')
	f.write('\n')
	f.write('i = incoming message')
	f.write('\n\n')

#Writes messages from database into text file organized by the number receiving the messages in order of when they were sent and labeled as outgoing or incoming
def print_conversation(num):

	#Pulls messages from database
	convo = db.execute(f'SELECT body, type FROM messages WHERE conversationID={num} ORDER BY sent_at ASC;').fetchall()
	
	#Writes messages to text file and labels them as (o) or (i)
	with open('messages.txt', 'a') as f:
		f.write('To '+num)
		f.write('\n\n')
		temp = convo[0][1]
		for msg in convo:
			if(temp == msg[1]):
				f.write(msg[0])
					
			else:
				temp = msg[1]
				f.write('\n')
				f.write(msg[0])
				
			if(msg[1] == 'outgoing'):
				f.write(' (o)')
			else:
				f.write(' (i)')
					
			f.write('\n')
			
		f.write('\n\n')

print_conversation('17036512962')
print_conversation('17036516754')
print_conversation('17039198567')

#Pulls messages from group chat from database
convo = db.execute('SELECT body, type FROM messages WHERE conversationID!=17036512962 AND conversationID!=17036516754 AND conversationID!=17039198567 ORDER BY sent_at ASC;').fetchall()

#Writes messages from group chat to text file in same manner as above, including the phone number of incoming messages
with open('messages.txt', 'a') as f:
		f.write('To 17036512962, 17036516754, 17039198567')
		f.write('\n\n')
		temp = convo[0][1]
		for msg in convo:
			if(temp == msg[1] and msg[0] is not None):
				f.write(msg[0])
					
			else:
				temp = msg[1]
				if(msg[0] is not None):
					f.write('\n')
					f.write(msg[0])
			
			if(msg[1] == 'outgoing'):
				f.write(' (o)')
			else:
				f.write(' (i, from: '+str(db.execute('SELECT source FROM messages WHERE conversationID!=17036512962 AND conversationID!=17036516754 AND conversationID!=17039198567 AND type LIKE \'%incoming%\';').fetchall()[0][0])+')')		
					
			f.write('\n')
			
		f.write('\n\n')


