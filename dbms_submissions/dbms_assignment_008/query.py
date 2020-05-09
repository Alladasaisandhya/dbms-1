Q1 = '''SELECT id, fname
        FROM Director AS D
        WHERE NOT EXISTS(SELECT did FROM MovieDirector JOIN Movie ON id = mid WHERE year < 2000 and did = d.id)
        AND EXISTS(SELECT did FROM MovieDirector JOIN Movie ON id = mid WHERE year > 2000 AND did = d.id)
        ORDER BY id;'''
        
Q2 = '''SELECT fname, (SELECT name FROM Movie JOIN MovieDirector ON mid = `Movie`.id JOIN Director ON  `Director`.id = did WHERE `Director`.id = d.id  ORDER BY rank DESC, name ASC LIMIT 1)
        FROM Director AS d
        LIMIT 100;'''
        
Q3 = '''SELECT *
        FROM Actor AS a
        WHERE NOT EXISTS(SELECT pid FROM Cast JOIN Movie ON mid = `Movie`.id WHERE (year BETWEEN 1990 AND 2000) AND pid = a.id)
        ORDER BY a.id DESC
        LIMIT 100;'''