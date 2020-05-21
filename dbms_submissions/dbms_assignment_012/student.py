class DoesNotExist(Exception):
	pass

class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

class Student:
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score

	@staticmethod
	def get(**kwargs):
		for key, value in kwargs.items():
			key_attribute = key
			value = value

		if key_attribute not in ("student_id", "name", "age", "score"):
			raise InvalidField
		
		sql_query = read_data(f"SELECT * FROM Student WHERE {key_attribute} = {value}")
	
		if len(sql_query) == 0:
			raise DoesNotExist
			
		elif len(sql_query) > 1:
			raise MultipleObjectsReturned
		else:
			ans = Student(sql_query[0][1], sql_query[0][2], sql_query[0][3])
			ans.student_id = sql_query[0][0]
			return ans
		
	def save(self):
		import sqlite3
		conn = sqlite3.connect("students.sqlite3")
		c = conn.cursor() 
		c.execute("PRAGMA foreign_keys=on;")
		
		if self.student_id == None:
			c.execute(f"INSERT INTO Student (name, age, score) values (\'{self.name}\', {self.age}, {self.score})")        
			self.student_id = c.lastrowid
		else:
			c.execute(f"UPDATE Student SET name = \'{self.name}\', age = {self.age}, score = {self.score} WHERE student_id = {self.student_id}")
		conn.commit() 
		conn.close()

	def delete(self):
	    write_data(f"DELETE FROM Student WHERE student_id = {self.student_id}")
	
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query)
	ans= crsr.fetchall()
	connection.close()
	return ans