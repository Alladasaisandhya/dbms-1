Q1 = '''SELECT P.player_id, `MatchCaptain`.team_id, P.jersey_no, P.name, P.date_of_birth, P.age
        FROM Player AS P JOIN MatchCaptain ON captain = P.player_id
        WHERE EXISTS(SELECT player_id FROM Player JOIN MatchCaptain ON captain = `Player`.player_id AND `Player`.player_id = P.player_id)
        AND 
        NOT EXISTS(SELECT goal_id FROM GoalDetails JOIN Player ON `GoalDetails`.player_id = `Player`.player_id AND `Player`.player_id = P.player_id);'''
        
Q2 = '''SELECT team_id, COUNT(match_no) AS no_of_games
        FROM MatchTeamDetails 
        GROUP BY team_id;'''
  
Q3 = '''SELECT GD.team_id , COUNT(goal_id) * 1.0 / (SELECT COUNT(player_id) FROM Player WHERE `Player`.team_id = GD.team_id) AS avg_goal_score
        FROM GoalDetails AS GD
        GROUP BY GD.team_id;'''

Q4 = '''SELECT captain, COUNT(match_no) AS no_of_times_captain
        FROM MatchCaptain
        GROUP BY captain;'''
        
Q5 = '''SELECT COUNT(DISTINCT `Player`.player_id) AS no_players
        FROM
        Player JOIN MatchCaptain ON `MatchCaptain`.captain = `Player`.player_id
        JOIN Match ON `Match`.player_of_match = `Player`.player_id AND `MatchCaptain`.match_no = `Match`.match_no;'''
        
Q6 = '''SELECT DISTINCT P.player_id
        FROM Player AS P
        WHERE EXISTS(SELECT captain FROM MatchCaptain WHERE captain = P.player_id)
        AND NOT EXISTS(SELECT player_of_match FROM Match JOIN MatchCaptain ON `Match`.match_no = `MatchCaptain`.match_no AND P.player_id = player_of_match);'''

Q7 = '''SELECT strftime("%m", play_date) AS month, COUNT(match_no) AS no_of_matches
        FROM Match
        GROUP BY month
        ORDER BY no_of_matches DESC;'''
        
Q8 = '''SELECT jersey_no, COUNT(captain) AS no_captains
        FROM MatchCaptain JOIN Player ON captain = player_id
        GROUP BY jersey_no
        ORDER BY no_captains DESC, jersey_no DESC;'''
        
Q9 = '''SELECT `Player`.player_id, AVG(audience) AS avg_audience
        FROM Player JOIN MatchCaptain ON `MatchCaptain`.team_id  = `Player`.team_id JOIN Match ON `Match`.match_no = `MatchCaptain`.match_no
        GROUP BY `Player`.player_id
        ORDER BY avg_audience DESC, `Player`.player_id DESC;'''
        
Q10 = '''SELECT `Team`.team_id, AVG(age)
         FROM Team JOIN Player ON `Player`.team_id = `Team`.team_id
         GROUP BY `Team`.team_id;'''

Q11 = '''SELECT AVG(age) AS avg_age_of_captains
         FROM MatchCaptain JOIN Player ON captain = player_id;'''
         
Q12 = '''SELECT strftime("%m", date_of_birth) AS month, COUNT(player_id) AS no_of_players
         FROM Player
         GROUP BY month
         ORDER BY no_of_players DESC, month DESC;'''

Q13 = '''SELECT captain, COUNT(win_lose) AS no_of_wins
         FROM MatchCaptain LEFT JOIN MatchTeamDetails ON `MatchCaptain`.match_no = `MatchTeamDetails`.match_no AND `MatchCaptain`.team_id = `MatchTeamDetails`.team_id
         WHERE win_lose = 'W'
         GROUP BY captain
         ORDER BY no_of_wins DESC;'''
         
         
Q = '''SELECT P.player_id, `MatchCaptain`.team_id, P.jersey_no, P.name, P.date_of_birth, P.age
        FROM Player AS P
        INNER JOIN MatchCaptain ON `MatchCaptain`.captain = P.player_id 
        LEFT JOIN GoalDetails ON `GoalDetails`.player_id = `MatchCaptain`.captain
        WHERE goal_id IS NULL;'''
         
