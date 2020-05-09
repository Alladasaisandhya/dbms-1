
Q1 = '''SELECT AVG(age)
        FROM Player'''
        
Q2 = '''SELECT match_no, play_date
        FROM Match
        WHERE audience > 50000
        ORDER BY match_no ASC;'''
        
Q3 = '''SELECT team_id, COUNT(1) AS no_matches_won
        FROM MatchTeamDetails
        WHERE win_lose = 'W'
        GROUP BY team_id
        ORDER BY no_matches_won DESC, team_id ASC;'''
        
Q4 = '''SELECT match_no, play_date
        FROM Match
        WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match)
        ORDER BY match_no DESC;'''
        
Q5 = '''SELECT `Match`.match_no, `Team`.name AS team_name, `Player`.name AS captain_name
        FROM MatchCaptain JOIN Match ON `MatchCaptain`.match_no = `Match`.match_no
        JOIN Team ON `MatchCaptain`.team_id = `Team`.team_id
        JOIN Player ON `MatchCaptain`.captain = `Player`.player_id
        ORDER BY `Match`.match_no ASC , `Team`.name;'''
        
Q6 = '''SELECT match_no, name, jersey_no
        FROM Match JOIN Player ON player_id = player_of_match
        ORDER BY match_no ASC;'''

Q7 = '''SELECT `Team`.name, AVG(age) AS average_age
        FROM Team JOIN Player ON `Team`.team_id = `Player`.team_id
        GROUP BY `Team`.name
        HAVING average_age > 26
        ORDER BY `Team`.name ASC;'''
        
Q8 = '''SELECT name, jersey_no, age, COUNT(goal_id) AS number_of_goals
        FROM Player JOIN GoalDetails ON Player.player_id = `GoalDetails`.player_id
        WHERE age <= 27
        GROUP BY name
        ORDER BY number_of_goals DESC, name ASC;'''
        
Q9 = '''SELECT team_id, COUNT(goal_id)*100.0/(SELECT COUNT(goal_id) FROM GoalDetails)
        FROM GoalDetails
        GROUP BY team_id
        HAVING COUNT(goal_id) != 0;'''
        
Q10 = '''SELECT AVG(avg_scores)
         FROM
         (SELECT COUNT(goal_id) AS avg_scores
         FROM Team JOIN GoalDetails ON Team.team_id = `GoalDetails`.team_id
         GROUP BY `Team`.team_id) AS scores;'''
        
Q11 = '''SELECT player_id, name, date_of_birth
         FROM Player AS P
         WHERE NOT EXISTS(SELECT goal_id FROM GoalDetails WHERE `GoalDetails`.player_id = P.player_id)
         ORDER BY player_id ASC;'''

Q12 = '''SELECT `T`.name, `M`.match_no, audience AS audience, audience - (SELECT AVG(audience) FROM Match JOIN MatchTeamDetails ON `Match`.match_no = `MatchTeamDetails`.match_no AND T.team_id = `MatchTeamDetails`.team_id)
         FROM MatchTeamDetails JOIN Match AS M ON `MatchTeamDetails`.match_no = `M`.match_no
         JOIN Team AS T ON `MatchTeamDetails`.team_id = `T`.team_id
         ORDER BY `M`.match_no ASC;'''