Q1 = "SELECT COUNT(id) FROM Movie WHERE (year = 2002) AND (name LIKE 'Ha%') AND (rank > 2);"

Q2 = "SELECT MAX(rank) FROM Movie WHERE (year = 1983 OR year = 1994) AND (name LIKE 'Autom%');"

Q3 = "SELECT COUNT(id) FROM Actor WHERE (gender = 'M') AND (fname LIKE '%ei' OR lname LIKE 'ei%');"

Q4 = "SELECT AVG(rank) AS average_rank_of_movies FROM Movie WHERE (year in (1993, 1995, 2000)) AND (rank >= 4.2);"

Q5 = "SELECT SUM(rank) FROM Movie WHERE (year BETWEEN 1981 and 1984) AND (name LIKE '%Hary%') AND (rank < 9);"

Q6 = "SELECT year FROM Movie WHERE rank = 5 ORDER BY year ASC LIMIT 1;"

Q7 = "SELECT COUNT(id) FROM Actor WHERE (gender = 'F') OR (Actor.fname = Actor.lname);"

Q8 = "SELECT DISTINCT(fname) FROM Actor WHERE lname LIKE '%ei' ORDER BY fname ASC LIMIT 100;"

Q9 = "SELECT id, name AS movie_title, year FROM Movie WHERE year IN (2001, 2002, 2005, 2006) LIMIT 25 OFFSET 10;"

Q10 = "SELECT DISTINCT lname FROM Director WHERE fname IN ('Yeud', 'Wolf', 'Vicky') ORDER BY lname ASC LIMIT 5;"