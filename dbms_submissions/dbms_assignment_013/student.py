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
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
        
    @staticmethod
    def get(**kwargs):
        for key, value in kwargs.items():
            if key not in ("student_id", "name", "age", "score"):
                raise InvalidField
        sql_query = read_data(f"SELECT * FROM Student WHERE {key} = '{value}'")
        
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
        conn = sqlite3.connect("selected_students.sqlite3")
        c = conn.cursor() 
        c.execute("PRAGMA foreign_keys=on;")
        
        if self.student_id == None:
            c.execute(f"INSERT INTO Student (name, age, score) values ('{self.name}', {self.age}, {self.score})")        
            self.student_id = c.lastrowid
        
        elif c.execute(f"SELECT {self.student_id} not in (SELECT student_id FROM Student) FROM Student"):
            c.execute(f"REPLACE INTO Student (student_id, name, age, score) values ({self.student_id}, '{self.name}', {self.age}, {self.score})")        
            
        else:
            c.execute(f"UPDATE Student SET name = '{self.name}', age = {self.age}, score = {self.score} WHERE student_id = {self.student_id}")
        
        conn.commit() 
        conn.close()
        
    def delete(self):
        write_data(f"DELETE FROM Student WHERE student_id = {self.student_id}")
        
    @staticmethod
    def filter(**kwargs):
        objects_list=[]
        operator={'lt' : '<', 'lte' : '<=', 'gt' : '>', 'gte' : '>=', 'neq' : '!=', 'in' : 'in'}
        
        if(len(kwargs)) >= 1:
            conditions = []
            for key, value in kwargs.items():
                    
                    keys = key
                    keys = keys.split('__')
                    if keys[0] not in ('name', 'age', 'score', 'student_id'):
                            raise InvalidField 
            
                    if len(keys) == 1:
                        sql_query= f" {key} = '{value}'"
                    
                    elif keys[1] == 'in':
                        if len(value) > 1:
                            sql_query = f"{keys[0]} {operator[keys[1]]} {tuple(value)}"
                        else:
                            sql_query= f"{keys[0]} = '{value}'"
                    
                    elif keys[1] == 'contains':
                        sql_query = f"{keys[0]} like '%{value}%'"
                    
                    else:    
                        sql_query = f"{keys[0]} {operator[keys[1]]} '{value}'"
                
                    conditions.append(sql_query)
                    
            mul_conditions = " and ".join(tuple(conditions))       
            sql_query = "SELECT * FROM Student WHERE " + mul_conditions
            
        sql_query = read_data(sql_query)
        
        for i in sql_query:
            ans = Student(i[1], i[2], i[3])
            ans.student_id = i[0]
            objects_list.append(ans)
        return objects_list    
            
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query)
	ans= crsr.fetchall()
	connection.close()
	return ans
	
selected_students = Student.filter(age__in = [18])
print(selected_students)