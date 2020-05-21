Q1 = '''SELECT `Actor`.id, fname, lname, gender
        FROM Actor
        JOIN Cast ON `Actor`.id = pid
        JOIN Movie ON `Movie`.id = mid
        WHERE name LIKE 'Annie%';'''

Q2 = '''SELECT `Movie`.id, name, rank, year
        FROM Movie JOIN MovieDirector ON `Movie`.id = mid
        JOIN Director ON `Director`.id = did
        WHERE `Director`.fname = "Biff" AND `Director`.lname = "Malibu" AND year in (1999, 1994, 2003)
        ORDER BY rank DESC, year ASC;'''

Q3 = '''SELECT M.year, COUNT(name) AS no_of_movies
        FROM Movie AS M
        GROUP BY year
        HAVING AVG(rank) > (SELECT AVG(rank) FROM Movie)
        ORDER BY year ASC;'''

Q4 = '''SELECT * FROM Movie AS M
        WHERE year = 2001 AND (rank < (SELECT AVG(rank) FROM Movie WHERE year = 2001))
        ORDER BY rank DESC
        LIMIT 10;'''

Q6 = '''SELECT DISTINCT `Cast`.pid FROM Cast
        JOIN Movie ON `Cast`.mid = `Movie`.id
        GROUP BY `Cast`.mid, `Cast`.pid
        HAVING COUNT(DISTINCT role) > 1
        ORDER BY `Cast`.pid ASC
        LIMIT 100;'''

Q7 = '''SELECT fname, COUNT(1) AS count
        FROM Director
        GROUP BY fname
        HAVING COUNT > 1;'''

Q8 = '''SELECT DISTINCT D.id, D.fname, D.lname
        FROM Director AS D
        WHERE EXISTS(SELECT `Director`.id FROM Director JOIN MovieDirector ON `Director`.id = `MovieDirector`.did AND D.id = `MovieDirector`.did
                     JOIN Cast ON `Cast`.mid = `MovieDirector`.mid
                     GROUP BY `Director`.id, `MovieDirector`.mid
                     HAVING COUNT(`Cast`.role) >= 100)
        AND
        NOT EXISTS(SELECT `Director`.id FROM Director JOIN MovieDirector ON `Director`.id = `MovieDirector`.did AND D.id = `MovieDirector`.did
                   JOIN Cast ON `Cast`.mid = `MovieDirector`.mid
                   GROUP BY `Director`.id, `MovieDirector`.mid
                   HAVING COUNT(`Cast`.role) < 100)
        GROUP BY D.id;'''

Q5 = '''SELECT C.mid, (case when gender == "F" then count("F") end) AS no_of_female_actors, count(case when gender == "M" then 1 end) AS no_of_male_actors   
        FROM Cast AS C
        JOIN Actor ON `Actor`.id = C.pid
        GROUP BY C.mid5
        ORDER BY C.mid ASC
        LIMIT 100;'''