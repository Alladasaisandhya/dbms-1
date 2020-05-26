class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    @classmethod
    def avg(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select avg({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select avg({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
    
    @classmethod
    def min(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select min({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select min({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
    
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select max({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select max({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
        
    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select sum({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select sum({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
        
    @classmethod
    def count(cls, field = None, **kwargs):
        if field == None:
            sql_query = "select count(*) from student"    
        
        elif field not in ('name','age','score','student_id'):
                raise InvalidField
                
        elif len(kwargs)>=1:
            sql_query = f"select count({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select count({field}) from student"        
    
        ans=read_data(sql_query)
        return ans[0][0]
    
    @staticmethod
    def filter(**kwargs):
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
                        sql_query = f"{keys[0]} {operator[keys[1]]} {tuple(value)}"
                    
                    elif keys[1] == 'contains':
                        sql_query = f"{keys[0]} like '%{value}%'"
                    
                    else:    
                        sql_query = f"{keys[0]} {operator[keys[1]]} '{value}'"
                
                    conditions.append(sql_query)
                    
            mul_conditions = " and ".join(tuple(conditions))       
            sql_query = " " + mul_conditions
        return sql_query

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans