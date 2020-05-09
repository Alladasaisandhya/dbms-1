Q1 = '''SELECT COUNT(id)
        FROM Movie
        WHERE year < 2000;'''
        
Q2 = '''SELECT AVG(rank)
        FROM Movie
        WHERE year = 1991;'''

Q3 = '''SELECT MIN(rank)
        FROM Movie
        WHERE year = 1991;'''
        
Q4 = '''SELECT fname, lname
        FROM Actor JOIN Cast
        ON id = pid
        WHERE mid = 27;'''
        
Q5 = '''SELECT COUNT(mid)
        FROM Actor JOIN Cast
        ON id = pid
        WHERE fname = 'Jon' AND lname = 'Dough';'''
        
Q6 = '''SELECT name
        FROM Movie
        where (name LIKE 'Young Latin Girls%') AND (year BETWEEN 2003 AND 2006);'''
        
Q7 = '''SELECT `Director`.fname, `Director`.lname
        FROM ((Director JOIN MovieDirector ON `Director`.id = `MovieDirector`.did) JOIN Movie ON `Movie`.id = `MovieDirector`.mid)
        WHERE `Movie`.name LIKE 'Star Trek%';'''
        
Q8 = '''SELECT `Movie`.name FROM ((((Movie JOIN Cast ON `Movie`.id = `Cast`.mid) JOIN MovieDirector ON `MovieDirector`.mid  = `Movie`.id) JOIN Actor ON `Actor`.id = `Cast`.pid) JOIN Director ON `Director`.id = `MovieDirector`.did)
        WHERE (`Director`.fname = 'Jackie (I)' AND `Director`.lname = 'Chan') AND (`Actor`.fname = 'Jackie (I)' AND `Actor`.lname = 'Chan');'''

Q9 = '''SELECT `Director`.fname, `Director`.lname
        FROM ((Director JOIN MovieDirector ON `Director`.id = `MovieDirector`.did) JOIN Movie ON `Movie`.id = `MovieDirector`.mid)
        WHERE year = 2001
        GROUP BY `MovieDirector`.did
        HAVING  COUNT(`MovieDirector`.mid) >= 4
        ORDER BY `Director`.fname ASC, `Director`.lname DESC;'''

Q10 = '''SELECT gender, COUNT(id)
         From Actor
         GROUP BY gender;'''
         
Q11 = '''SELECT DISTINCT `Movie1`.name, `Movie2`.name, `Movie1`.rank, `Movie1`.year
         FROM Movie AS Movie1 JOIN Movie AS Movie2
         ON `Movie2`.rank = `Movie1`.rank AND `Movie2`.name != `Movie1`.name AND `Movie2`.year = `Movie1`.year
         ORDER BY `Movie1`.name ASC
         LIMIT 100;'''
         
Q12 = '''SELECT `Actor`.fname, `Movie`.year, AVG(rank) AS rank
         FROM ((Actor JOIN Cast ON `Actor`.id = pid) JOIN Movie ON `Movie`.id = mid)
         GROUP BY `Movie`.year, `Actor`.id  
         ORDER BY `Actor`.fname ASC, `Movie`.year DESC
         LIMIT 100;'''
         
Q13 = '''SELECT `Actor`.fname, `Director`.fname, AVG(rank) AS score
         FROM ((((Movie JOIN Cast ON `Movie`.id = `Cast`.mid) JOIN MovieDirector ON `MovieDirector`.mid  = `Movie`.id) JOIN Actor ON `Actor`.id = `Cast`.pid) JOIN Director ON `Director`.id = `MovieDirector`.did)
         GROUP BY `Actor`.id, `Director`.id
         HAVING COUNT(`MovieDirector`.mid) >= 5
         ORDER BY score DESC, `Director`.fname ASC, `Actor`.fname DESC
         LIMIT 100;'''