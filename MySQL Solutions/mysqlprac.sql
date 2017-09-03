
/* 1 */
CREATE PROCEDURE projectList()
BEGIN

SELECT project_name, team_lead, income
FROM Projects;
    
END

/* 2 */
CREATE PROCEDURE countriesSelection()
BEGIN

SELECT * FROM countries
WHERE countries.continent = 'Africa'
ORDER BY countries.name;
    
END

/* 3 */
CREATE PROCEDURE monthlyScholarships()
BEGIN

SELECT id, scholarship/12 AS scholarship
FROM scholarships;

    
END

/* 4 */
CREATE PROCEDURE projectsTeam()
BEGIN

SELECT DISTINCT projectLog.name
FROM projectLog
ORDER BY projectLog.name;
    
END

/* 5 */
CREATE PROCEDURE automaticNotifications()
    SELECT email
    FROM users
    WHERE users.role NOT IN ("admin", "premium")

    ORDER BY email;


/* 6 */
CREATE PROCEDURE volleyballResults()
BEGIN
SELECT *
FROM results
ORDER BY wins;
    
END

/* 7 */
CREATE PROCEDURE mostExpensive()
BEGIN

SELECT name
FROM Products
ORDER BY price*quantity DESC, name
LIMIT 1;

END

/* 8 */
CREATE PROCEDURE contestLeaderboard()
BEGIN

SELECT name
FROM leaderboard
ORDER BY score DESC
LIMIT 3,5;
    
END

/* 9 */
CREATE PROCEDURE gradeDistribution()
BEGIN

SELECT Name, ID
FROM Grades
WHERE Final/100 > ((Midterm1+Midterm2+Final)/400) AND Final/100 > ((Midterm1+Midterm2)/200)
ORDER BY LEFT(Name,3), ID;
/* it should actually be Final/200...wrong answer is desired... */
    
END

/* 10 */
CREATE PROCEDURE mischievousNephews()
BEGIN

/* could have just used WEEKDAY */
SELECT MOD(DAYOFWEEK(mischief_date)+5, 7) AS weekday, mischief_date, author, title
FROM mischief
ORDER BY weekday, FIELD(author,'Huey', 'Dewey', 'Louie'), mischief_date, title;
    
END

/* 11 */
CREATE PROCEDURE suspectsInvestigation()
BEGIN

SELECT id, name, surname
FROM Suspect
WHERE height < 171 AND name LIKE 'B%' AND surname LIKE 'Gre_n';
    
END

/* 12 */
CREATE PROCEDURE suspectsInvestigation2()
BEGIN

SELECT id, name, surname
FROM Suspect
WHERE NOT (height > 170 AND name LIKE 'B%' AND surname LIKE 'Gre_n');
    
END

/* 13 */
CREATE PROCEDURE securityBreach()
BEGIN

SELECT first_name, second_name, attribute
FROM users
WHERE attribute LIKE CONCAT('_%\%', BINARY(first_name), '\_', BINARY(second_name), '\%%')
ORDER BY attribute;
    
END

/* 14 */
CREATE PROCEDURE testCheck()
    SELECT id, IF ( correct_answer = given_answer, 'correct', IF(given_answer IS NULL, 'no answer', 'incorrect') ) AS checks
    FROM answers
    ORDER BY id

/* 15 */
CREATE PROCEDURE expressionsVerification()
BEGIN

SELECT *
FROM expressions
WHERE 
(operation = '+' AND a+b=c) OR 
(operation = '-' AND a-b=c) OR 
(operation = '*' AND a*b=c) OR 
(operation = '/' AND a/b=c)
ORDER BY id;
    
END

/* 16 */
CREATE PROCEDURE newsSubscribers()
BEGIN

SELECT DISTINCT subscriber
FROM ((SELECT * FROM full_year) UNION (SELECT * FROM half_year)) AS FullAndHalf
WHERE FullAndHalf.newspaper LIKE '%daily%'
ORDER BY subscriber;
    
END

/* 17 */
CREATE PROCEDURE countriesInfo()
BEGIN

SELECT COUNT(name) AS number, AVG(population) AS average, SUM(population) AS total
FROM countries;

END

/* 18 */
CREATE PROCEDURE itemCounts()
BEGIN

SELECT item_name, item_type, COUNT(*) AS item_count
FROM availableItems
GROUP BY item_name, item_type
ORDER BY item_type, item_name;
    
END

/* 19 */
CREATE PROCEDURE usersByContinent()
BEGIN

SELECT continent, SUM(users) AS users
FROM countries
GROUP BY continent
ORDER BY users DESC;
    
END

/* 20 */
CREATE PROCEDURE movieDirectors()
BEGIN

SELECT director
FROM moviesInfo
WHERE year > 2000
GROUP BY director
HAVING SUM(oscars) > 2
ORDER BY director;
  
END

/* 21 */
CREATE PROCEDURE travelDiary()
BEGIN

SELECT GROUP_CONCAT(DISTINCT country ORDER BY country SEPARATOR ';') AS countries
FROM diary;
    
END

/* 22 */
CREATE PROCEDURE soccerPlayers()
BEGIN

SELECT
GROUP_CONCAT(CONCAT(first_name, ' ', surname, ' #', player_number)
ORDER BY player_number SEPARATOR '; ') AS players
FROM soccer_team;
    
END

/* 23 */
CREATE PROCEDURE marketReport()
BEGIN


(SELECT country, COUNT(competitor) AS competitors
FROM foreignCompetitors
GROUP BY country
ORDER BY country)
UNION
(SELECT 'Total:' AS country, COUNT(*) AS competitors
FROM foreignCompetitors)
;
    
END

/* 24 */
CREATE PROCEDURE websiteHacking()
    SELECT id,login,name
    FROM users
    WHERE type='user'
    OR TRUE
    ORDER BY id

/* 25 */
CREATE PROCEDURE nullIntern()
BEGIN

SELECT COUNT(*) AS number_of_nulls
FROM departments
WHERE description IS NULL
OR description REGEXP '^[[:space:]]*(-|nil|NULL)[[:space:]]*$'; 

/* OR TRIM(description) in ('null', 'nil', '-'); */
/* line 11 can also be substituted for line 9 */

END

/* 26 */
DROP PROCEDURE IF EXISTS legsCount;
CREATE PROCEDURE legsCount()
    SELECT SUM(IF(type='human',2,4)) as summary_legs
    FROM creatures
    ORDER BY id;

/* 27 */
CREATE PROCEDURE combinationLock()
BEGIN

SELECT ROUND(EXP(SUM(LOG(LENGTH(characters))))) AS combinations
FROM discs;
    
END

/* 28 */
CREATE PROCEDURE interestClub()
    SELECT name
    FROM people_interests
    WHERE interests & (1+8) = (1+8) AND interests & (2+4+16+32+64+128+256+512+1024+2048) >= 0
    ORDER BY name

/* 29 */
CREATE PROCEDURE personalHobbies()
BEGIN

SELECT name
FROM people_hobbies
WHERE hobbies LIKE '%sports%' AND hobbies LIKE '%reading%'
ORDER BY name;
    
END

/* 30 */
CREATE PROCEDURE booksCatalogs()
BEGIN

SELECT ExtractValue(xml_doc, '/descendant-or-self::author[1]') AS author
FROM catalogs
ORDER BY author;
    
END

/* 31 */
CREATE PROCEDURE habitatArea()
BEGIN


SET @g = 
(SELECT CONCAT('MULTIPOINT(', points.pts, ')') AS MP
FROM
(SELECT GROUP_CONCAT(x,' ', y SEPARATOR ', ') AS pts
FROM places) AS points);

SELECT ST_AREA(ST_ConvexHull(ST_GeomFromText(@g))) AS area;
    
END

/* 32 */
CREATE PROCEDURE orderOfSuccession()
BEGIN

SELECT CONCAT(IF(gender='M','King ', 'Queen '), name) AS name
FROM Successors
ORDER BY birthday, name;
    
END

/* 33 */
CREATE PROCEDURE orderingEmails()
BEGIN

SELECT  id, 
        email_title, 
        (CASE WHEN size < 1048576 THEN CONCAT(FLOOR(size/1024), ' Kb')
              ELSE CONCAT(FLOOR(size/1048576), ' Mb') END) AS short_size
FROM emails
ORDER BY emails.size DESC;
    
END

/* 34 */
CREATE PROCEDURE placesOfInterest()
BEGIN

SELECT  country, 
        SUM(CASE WHEN leisure_activity_type='Adventure park' THEN number_of_places ELSE 0 END) AS adventure_park,
        SUM(CASE WHEN leisure_activity_type='Golf' THEN number_of_places ELSE 0 END) AS golf,
        SUM(CASE WHEN leisure_activity_type='River cruise' THEN number_of_places ELSE 0 END) AS river_cruise,
        SUM(CASE WHEN leisure_activity_type='Kart racing' THEN number_of_places ELSE 0 END) AS kart_racing
FROM countryActivities
GROUP BY country
ORDER BY country;

END

/* 35 */
CREATE PROCEDURE soccerGameSeries()
BEGIN

SELECT
CASE 
WHEN SUM(IF(first_team_score > second_team_score,1,0)) > SUM(IF(first_team_score < second_team_score,1,0)) THEN 1
WHEN SUM(IF(first_team_score > second_team_score,1,0)) < SUM(IF(first_team_score < second_team_score,1,0)) THEN 2
WHEN SUM(first_team_score) > SUM(second_team_score) THEN 1
WHEN SUM(first_team_score) < SUM(second_team_score) THEN 2
WHEN SUM(IF(match_host=2,first_team_score,0)) > SUM(IF(match_host=1,second_team_score,0)) THEN 1
WHEN SUM(IF(match_host=2,first_team_score,0)) < SUM(IF(match_host=1,second_team_score,0)) THEN 2
ELSE 0 END AS winner
FROM scores;

    
END

/* 36 */
CREATE PROCEDURE correctIPs()
BEGIN

/*make sure each number is between 0 and 255, inclusive*/
/*make sure exactly one of the final two numbers is a two-digit number*/ 

SELECT *
FROM ips
WHERE ip REGEXP '^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9][0-9])$'
OR ip REGEXP '^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9][0-9])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
ORDER BY id;
    
END

/* 37 */
CREATE PROCEDURE validPhoneNumbers()
BEGIN

SELECT *
FROM phone_numbers
WHERE phone_number REGEXP '^1-[0-9]{3}-[0-9]{3}-[0-9]{4}$'
OR phone_number REGEXP '^[(]1[)][0-9]{3}-[0-9]{3}-[0-9]{4}$'
ORDER BY surname;
    
END

/* 38 */
CREATE PROCEDURE importantEvents()
BEGIN

SELECT id, name, event_date, participants
FROM events
ORDER BY WEEKDAY(event_date), participants DESC;
    
END

/* 39 */
CREATE PROCEDURE dateFormatting()
BEGIN


SELECT STR_TO_DATE(date_str,'%Y-%m-%d') AS date_iso
FROM documents;
    
END

/* 40 */
CREATE PROCEDURE pastEvents()
BEGIN

SET @d = (SELECT MAX(event_date) FROM Events);

SELECT name, event_date
FROM Events
WHERE  TO_DAYS(@d) - TO_DAYS(event_date) > 0 AND TO_DAYS(@d) - TO_DAYS(event_date) < 8
ORDER BY event_date DESC;

END

/* 41 */
CREATE PROCEDURE netIncome()
BEGIN

SELECT YEAR(date) AS year, QUARTER(date) as quarter, (CAST(SUM(profit) AS SIGNED) - CAST(SUM(loss) AS SIGNED)) AS net_profit
FROM accounting
GROUP BY year, quarter
ORDER BY year, quarter;
    
END

/* 43 */
CREATE PROCEDURE companyEmployees()
BEGIN

SELECT *
FROM departments, employees
ORDER BY dep_name, emp_name;
    
END

/* 44 */
CREATE PROCEDURE scholarshipsDistribution()
BEGIN

SELECT candidate_id AS student_id
FROM candidates LEFT JOIN detentions
ON candidates.candidate_id = detentions.student_id
WHERE student_id IS NULL;
    
END

/* 45 */
CREATE PROCEDURE userCountries()
BEGIN

SELECT id, IF(ISNULL(country), 'unknown', country) AS country
FROM users LEFT JOIN cities
ON users.city = cities.city
ORDER BY id;
    
END

/* 46 */
CREATE PROCEDURE placesOfInterestPairs()
BEGIN

SELECT s1.name AS place1, s2.name AS place2
FROM sights AS s1, sights AS s2
WHERE s1.name < s2.name AND  SQRT( POWER(ABS(s1.x-s2.x), 2) + POWER(ABS(s1.y-s2.y), 2) ) < 5
ORDER BY place1, place2;
    
END

/* 47 */
CREATE PROCEDURE localCalendar()
BEGIN

SELECT  events.event_id,  
        (CASE
        WHEN settings.hours = 24 
                THEN DATE_FORMAT( (events.date + INTERVAL settings.timeshift MINUTE), '%Y-%m-%d %k:%i' )
        WHEN settings.hours = 12 
                THEN DATE_FORMAT( (events.date + INTERVAL settings.timeshift MINUTE), '%Y-%m-%d %h:%i %p' )
        END) AS formatted_date
FROM events, settings
WHERE events.user_id = settings.user_id
ORDER BY events.event_id;
    
END

/* 48 */
CREATE PROCEDURE routeLength()
BEGIN

SELECT ROUND( SUM( SQRT( POWER(ABS(c1.x-c2.x), 2) + POWER(ABS(c1.y-c2.y), 2) ) ), 9 ) AS total
FROM cities AS c1, cities AS c2
WHERE c2.id - c1.id = 1;
    
END

/* 49 */
CREATE PROCEDURE currencyCodes()
BEGIN
    DELETE FROM currencies
    WHERE code NOT LIKE '___';

    SELECT * FROM currencies ORDER BY code;
END

/* 50 */
CREATE PROCEDURE coursesDistribution()
BEGIN
    ALTER TABLE groupcourses ADD FOREIGN KEY (course_id)
    REFERENCES courses(id) ON DELETE CASCADE;

    ALTER TABLE groupexams ADD FOREIGN KEY (course_id)
    REFERENCES courses(id) ON DELETE CASCADE;

    DELETE FROM courses WHERE name LIKE '%-toremove';


    SELECT group_id, course_id
      FROM groupcourses
     UNION
    SELECT group_id, course_id
      FROM groupexams
     ORDER BY group_id, course_id;
END

/* 51 */
CREATE PROCEDURE nicknames()
BEGIN
    UPDATE reservedNicknames
    SET id = CONCAT('rename - ', id), nickname = CONCAT('rename - ', nickname)
    WHERE LENGTH(nickname) <> 8;

    SELECT * FROM reservedNicknames ORDER BY id;
END

/* 52 */
CREATE PROCEDURE tableSecurity()
BEGIN
    CREATE OR REPLACE VIEW emp
    AS SELECT id, name, YEAR(date_joined) AS date_joined, '-' AS salary
    FROM employees;

    SELECT id, name, date_joined, salary
    FROM emp
    ORDER BY id;
END

/* 53 */
CREATE PROCEDURE officeBranches()
BEGIN
    ALTER TABLE branches ADD FOREIGN KEY (branchtype_id)
    REFERENCES branch_types(id) ON DELETE SET NULL;

    DELETE FROM branch_types WHERE name LIKE '%-outdated';

    SELECT * FROM branches
    ORDER BY branch_id;
END

/* 54 */
CREATE PROCEDURE restaurantInfo()
BEGIN
    ALTER TABLE restaurants
    ADD description VARCHAR(100);

    ALTER TABLE restaurants
    ADD active INT;
    
    UPDATE restaurants
    SET description = 'TBD', active = 1;

    SELECT * FROM restaurants ORDER BY id;
END

/* 55 */
CREATE PROCEDURE studentsInClubs()
    SELECT * FROM students
    WHERE EXISTS (
        SELECT *
        FROM clubs
        WHERE students.club_id = clubs.id
    )
    ORDER BY students.id;

/* 56 */
CREATE PROCEDURE emptyDepartments()
BEGIN

SELECT dep_name
FROM departments
WHERE NOT EXISTS (
    SELECT *
    FROM employees
    WHERE employees.department = departments.id
);
    
END

/* 57 */
CREATE PROCEDURE sunnyHolidays()
BEGIN

SELECT holidays.holiday_date AS ski_date
FROM holidays INNER JOIN weather
ON holidays.holiday_date = weather.sunny_date
ORDER BY ski_date;
    
END

/* 58 */
CREATE PROCEDURE closestCells()
BEGIN

SELECT t2.id1, t2.id2
FROM 
    (SELECT p1.id AS id1, MIN(SQRT(POWER(ABS(p1.x-p2.x),2) + POWER(ABS(p1.y-p2.y),2))) AS distance
    FROM positions AS p1, positions AS p2
    WHERE p1.id != p2.id
    GROUP BY p1.id) AS t1
    JOIN
    (SELECT p1.id AS id1, p2.id AS id2, SQRT(POWER(ABS(p1.x-p2.x),2) + POWER(ABS(p1.y-p2.y),2)) AS distance
    FROM positions AS p1, positions AS p2
    WHERE p1.id != p2.id) AS t2
    ON t1.id1 = t2.id1 AND t1.distance = t2.distance
ORDER BY t1.id1;
    
END

/* 59 */
CREATE PROCEDURE top5AverageGrade()
BEGIN

SELECT ROUND(AVG(grade),2) AS average_grade
FROM
    (SELECT *
     FROM students
     ORDER BY grade DESC
     LIMIT 5) AS FiveBest
;
    
END

/* 60 */
CREATE PROCEDURE salaryDifference()
BEGIN

SET @theMax = (SELECT MAX(salary) FROM employees);
SET @theMin = (SELECT MIN(salary) FROM employees);
SET @salDiff = 
(SELECT SUM(
    CASE WHEN salary = @theMax AND salary = @theMin THEN 0
         WHEN salary = @theMax THEN salary
         WHEN salary = @theMin THEN -salary
         ELSE 0
         END) AS difference
FROM employees);

SELECT ROUND(IF(ISNULL(@salDiff), 0, @salDiff), 0) AS difference;

END

/* 61 */
CREATE PROCEDURE recentHires()
BEGIN

SELECT name AS names
FROM
(
 SELECT *
 FROM
   (SELECT name, date_joined, 1 AS filter
    FROM pr_department
    ORDER BY date_joined DESC
    LIMIT 5) AS t1
   UNION ALL
 SELECT *
 FROM
   (SELECT name, date_joined, 2 AS filter
    FROM it_department
    ORDER BY date_joined DESC
    LIMIT 5) AS t2
   UNION ALL
 SELECT *
 FROM
   (SELECT name, date_joined, 3 AS filter
    FROM sales_department
    ORDER BY date_joined DESC
    LIMIT 5) AS t3

ORDER BY filter, name
 ) AS theNames
;

END

/* 62 */
CREATE PROCEDURE checkExpenditure()
BEGIN

SELECT id, IF(SUM(expenditure_sum)-value < 0, 0, SUM(expenditure_sum)-value) AS loss 
FROM (SELECT expenditure_sum, WEEK(monday_date) AS weekNumber
      FROM expenditure_plan) AS EP 
            JOIN 
      (SELECT * FROM allowable_expenditure) AS AE
            ON EP.weekNumber BETWEEN AE.left_bound AND AE.right_bound
GROUP BY id
ORDER BY id;
END

/* 63 */
CREATE PROCEDURE dancingCompetition()
BEGIN

SET @firstMax = (SELECT MAX(first_criterion) FROM scores);
SET @secondMax = (SELECT MAX(second_criterion) FROM scores);
SET @thirdMax = (SELECT MAX(third_criterion) FROM scores);
SET @firstMin = (SELECT MIN(first_criterion) FROM scores);
SET @secondMin = (SELECT MIN(second_criterion) FROM scores);
SET @thirdMin = (SELECT MIN(third_criterion) FROM scores);

SELECT *
FROM scores
WHERE 
    (first_criterion = @firstMax OR first_criterion = @firstMin) +
    (second_criterion = @secondMax OR second_criterion = @secondMin) +
    (third_criterion = @thirdMax OR third_criterion = @thirdMin)
    < 2;
END

/* 64 */
CREATE PROCEDURE trackingSystem()
BEGIN

SELECT NIL.anonymous_id AS anonym_id, NIL.event_name AS last_null, NOTNIL.event_name AS first_notnull
FROM
    (SELECT anonymous_id, event_name
    FROM 
        (SELECT MAX(received_at) AS received_at
        FROM (SELECT * FROM tracks WHERE user_id IS NULL) AS Nulls
        GROUP BY anonymous_id) AS TheNulls
        JOIN
        tracks
        ON TheNulls.received_at = tracks.received_at) AS NIL
    LEFT JOIN
    (SELECT anonymous_id, event_name
    FROM 
        (SELECT MIN(received_at) AS received_at
        FROM (SELECT * FROM tracks WHERE user_id IS NOT NULL) AS NotNulls
        GROUP BY anonymous_id) AS TheNotNulls
        JOIN
        tracks
        ON TheNotNulls.received_at = tracks.received_at) AS NOTNIL
    ON NIL.anonymous_id = NOTNIL.anonymous_id
ORDER BY NIL.anonymous_id
;
    
END

/* 65 */
CREATE PROCEDURE storageOptimization()
BEGIN

SELECT *
FROM
(
    SELECT id, 'name' AS column_name, name AS value FROM
    (SELECT id, name
    FROM workers_info) AS names
    UNION
    SELECT id, 'date_of_birth' AS column_name, date_of_birth AS value FROM
    (SELECT id, date_of_birth
    FROM workers_info) AS dates_of_birth
    UNION
    SELECT id, 'salary' AS column_name, salary AS value FROM
    (SELECT id, salary
    FROM workers_info) AS salaries
) AS info
WHERE value IS NOT NULL
ORDER BY id, FIELD(column_name,'name', 'date_of_birth', 'salary');
    
END

/* 66 */
CREATE PROCEDURE consecutiveIds()
BEGIN

SET @row_number = 0;

SELECT id AS oldId, (@row_number:=@row_number + 1) AS newId
FROM itemIds;
    
END

/* 67 */
CREATE PROCEDURE holidayEvent()
BEGIN

SET @row_number = 0;

SELECT DISTINCT buyer_name AS winners
FROM
    (SELECT buyer_name, (@row_number:=@row_number + 1) AS buyer_id
    FROM purchases) AS buyers
WHERE MOD(buyer_id,4) = 0
ORDER BY buyer_name;
    
END

/* 68 */
CREATE PROCEDURE hostnamesOrdering()
BEGIN

/* separate the 1-domain hostnames, 2-domain hostnames and the 3-domain hostnames */

SELECT id, hostname
FROM
    (SELECT 
        id,
        hostname,
        domain3,
        CASE
            WHEN LENGTH(hostname) = LENGTH(domain3) THEN NULL
            ELSE SUBSTRING_INDEX(domain2domain3, '.', 1)
        END
            AS domain2,
        CASE
            WHEN LENGTH(hostname) = LENGTH(domain2domain3) THEN NULL
            ELSE SUBSTRING_INDEX(hostname, '.', 1)
        END
            AS domain1
    FROM
        (SELECT 
            id,
            hostname,
            SUBSTRING_INDEX(hostname, '.', -1) AS domain3,
            SUBSTRING_INDEX(hostname, '.', -2) AS domain2domain3
        FROM hostnames) AS t1) AS t2
ORDER BY domain3, domain2, domain1;
    
END

/* 69 */
DROP PROCEDURE IF EXISTS orderAnalytics;
CREATE PROCEDURE orderAnalytics()
BEGIN

    CREATE OR REPLACE VIEW order_analytics
    AS
    (SELECT 
         id, 
         YEAR(order_date) AS year, 
         QUARTER(order_date) AS quarter, 
         type, 
         quantity*price AS total_price
     FROM orders);

    SELECT *
    FROM order_analytics
    ORDER by id;
END;

/* 70 */
DROP FUNCTION IF EXISTS response;
CREATE FUNCTION response(name VARCHAR(40)) RETURNS VARCHAR(200) DETERMINISTIC
BEGIN

    SET @Firstname = LOWER(SUBSTRING_INDEX(name, ' ', 1));
    SET @Lastname = LOWER(SUBSTRING_INDEX(name, ' ', -1));

    SET @Firstname = CONCAT(UPPER(LEFT(@Firstname, 1)), SUBSTRING(@Firstname, 2));
    SET @Lastname = CONCAT(UPPER(LEFT(@Lastname, 1)), SUBSTRING(@Lastname, 2));

    RETURN CONCAT('Dear ', @Firstname, ' ', @Lastname, '! We received your message and will process it as soon as possible. Thanks for using our service. FooBar On! - FooBarIO team.');
END;

/* 71 */
CREATE PROCEDURE customerMessages()
BEGIN
    SELECT id, name, response(name) AS response
    FROM customers;
END;

DROP FUNCTION IF EXISTS get_total;
CREATE FUNCTION get_total(items VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN

    SET @Sum = 0;
    SET @remainingItems = CONCAT(items, ';');

    WHILE LOCATE(';', @remainingItems) != 0 DO

        SET @CurNumber = SUBSTRING(@remainingItems FROM 1 FOR LOCATE(';', @remainingItems) - 1);
        SET @Sum = @Sum + (SELECT price FROM item_prices WHERE id = @CurNumber);

        SET @remainingItems = SUBSTRING(@remainingItems, LOCATE(';', @remainingItems) + 1);
    
    END WHILE;
    
    RETURN @Sum;


END;

CREATE PROCEDURE orderPrices()
BEGIN
    SELECT id, buyer, get_total(items) AS total_price
    FROM orders
    ORDER BY id;
END;

/* 72 */
CREATE PROCEDURE findTable()
BEGIN

SELECT TABLE_NAME AS tab_name, COLUMN_NAME AS col_name, DATA_TYPE AS data_type
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'ri_db' AND TABLE_NAME LIKE 'e%s'
ORDER BY tab_name, col_name;
    
END

/* 74 */
CREATE PROCEDURE filmLibrary()
BEGIN
    /* actors (oldest to youngest, name) who star in most common genre */

SELECT starring_actors.actor, age
FROM
    (movies 
    JOIN
    starring_actors
    ON movies.movie = starring_actors.movie_name)
    JOIN
    actor_ages
    ON starring_actors.actor = actor_ages.actor
WHERE genre = 
    (SELECT genre AS mostCommonGenre
    FROM
        (SELECT genre, COUNT(genre) AS genreCount
        FROM movies
        GROUP BY genre
        ORDER BY genreCount DESC
        LIMIT 1) AS MCG)
ORDER BY age DESC, starring_actors.actor;

END

/* 75 */
CREATE PROCEDURE bugsInComponent()
BEGIN

SELECT bug_title, component_title, bugs_in_component
FROM
    (SELECT t3.component_id, bug_num, bugs_in_component, component_title
    FROM
        (SELECT component_id, bugs_in_component, title AS component_title
        FROM
            (SELECT *
            FROM 
                (SELECT component_id, COUNT(bug_num) AS bugs_in_component
                FROM BugComponent
                GROUP BY component_id) AS t1) AS t2
            JOIN
            Component
            ON Component.id = t2.component_id) AS t3
        JOIN
        BugComponent
        ON t3.component_id = BugComponent.component_id) AS t4
        JOIN
        (SELECT bug_num, title AS bug_title
        FROM
            (SELECT bug_num, COUNT(component_id) AS compCount
            FROM BugComponent
            GROUP BY bug_num
            HAVING compCount > 1) AS t3
            JOIN
            Bug
            ON Bug.num = t3.bug_num) AS t5
        ON t5.bug_num = t4.bug_num
ORDER BY bugs_in_component DESC, component_id, t4.bug_num
;

END

/* 76 */
CREATE PROCEDURE freeSeats()
BEGIN

SELECT flight_id, (number_of_seats - taken_seats) AS free_seats
FROM
    (SELECT flight_id, plane_id AS pid, IF(taken_seats IS NULL, 0, taken_seats) AS taken_seats
    FROM
        flights
        LEFT JOIN
        (SELECT flight_id AS fid, COUNT(seat_no) AS taken_seats
        FROM purchases
        GROUP BY flight_id) AS t1
        ON flights.flight_id = t1.fid) AS t2
    JOIN planes
    ON planes.plane_id = t2.pid
ORDER BY flight_id;

END

/* 77 */
CREATE PROCEDURE giftPackaging()
BEGIN

SELECT package_type, COUNT(id) AS number
FROM
    (SELECT id, package_type
    FROM
        (SELECT id, MIN(vol) AS packageVol
        FROM
            (SELECT id, gift_name, length, width, height, length*width*height AS volume
            FROM gifts) AS gfts
            JOIN
            (SELECT package_type, length AS len, width AS wid, height AS hgt, length*width*height AS vol
            FROM packages) AS pkgs
            ON length <= len AND width <= wid AND height <= hgt AND volume <= vol
        GROUP BY id) AS t1
        JOIN
        packages
        ON
        packageVol = packages.length*packages.width*packages.height) AS t2
GROUP BY package_type
ORDER BY package_type
;
    
END

/* 78 */
CREATE FUNCTION countLetter(letter VARCHAR(1), str VARCHAR(100)) RETURNS INT DETERMINISTIC
BEGIN
    SET @letterCount = 0;
    SET @remainingString = str;

    WHILE LENGTH(@remainingString) > 0 DO
        SET @firstChar = LEFT(@remainingString, 1);
        IF @firstChar = letter THEN SET @letterCount = @letterCount + 1;
        END IF;

        SET @remainingString = RIGHT(@remainingString, LENGTH(@remainingString)-1);
    END WHILE;
    
    RETURN @letterCount;

END;

CREATE PROCEDURE stringsStatistics()
BEGIN

/* create temp table, loop through letters a-z, add rows to table */

CREATE TABLE IF NOT EXISTS letters (
    letter VARCHAR(1)
);

SET @ord = 97;
WHILE @ord < 123 DO
    INSERT INTO letters(letter)
    VALUES (CHAR(@ord));
    
    SET @ord = @ord + 1;
END WHILE;

CREATE TABLE IF NOT EXISTS letter_count (
    letter VARCHAR(1),
    str VARCHAR(100),
    letterCount INT
);

INSERT INTO letter_count
SELECT * FROM
    (SELECT letter, str, countLetter(letter, str) AS letterCount
    FROM letters, strs
    WHERE LOCATE(letters.letter, strs.str) != 0) AS t1;

CREATE TABLE IF NOT EXISTS occurrences (
    ltr VARCHAR(1),
    occurrence INT
);

INSERT INTO occurrences
SELECT * FROM
    (SELECT letter AS ltr, COUNT(letter) AS occurrence
    FROM letters, strs
    WHERE LOCATE(letters.letter, strs.str) != 0
    GROUP BY letter) AS t2;


CREATE TABLE IF NOT EXISTS ans (
    letter VARCHAR(1),
    total INT,
    occurrence INT,
    max_occurrence INT,
    max_occurrence_reached INT
);

INSERT INTO ans
SELECT letter, total, occurrence, max_occurrence, max_occurrence_reached FROM
    (SELECT letter, total, occurrence
    FROM 
        (SELECT letter, SUM(letterCount) AS total
        FROM letter_count
        GROUP BY letter) AS t2
        JOIN
        occurrences
        ON t2.letter = occurrences.ltr) AS t5
    JOIN
    (SELECT ltr, max_occurrence, COUNT(ltr) AS max_occurrence_reached
    FROM
        (SELECT letter AS ltr, MAX(letterCount) AS max_occurrence
        FROM letter_count
        GROUP BY letter) AS t4
        JOIN
        letter_count
        ON t4.ltr = letter_count.letter AND t4.max_occurrence = letter_count.letterCount
    GROUP BY ltr) AS t6
    ON t5.letter = t6.ltr
ORDER BY letter;

SELECT *
FROM ans;
    
DROP TABLE letters;
DROP TABLE letter_count;
DROP TABLE occurrences;
DROP TABLE ans;

    
END

/* 79 */
CREATE PROCEDURE unluckyEmployees()
BEGIN

SET @row_number = 0;

SELECT dep_name, emp_number, total_salary
FROM
    (SELECT dep_name, emp_number, total_salary, (@row_number:=@row_number + 1) AS row
    FROM
        (SELECT dep_name, IF(department IS NULL, 0, COUNT(department)) AS emp_number, SUM(salary) AS total_salary
        FROM
            (SELECT name AS dep_name, IF(salary IS NULL, 0, salary) AS salary, Department.id AS dep_id, department
            FROM Department LEFT JOIN Employee
            ON Department.id = Employee.department) AS t1
        GROUP BY dep_name
        HAVING emp_number < 6
        ORDER BY total_salary DESC, emp_number DESC, dep_id) AS t2) AS t3
WHERE MOD(row,2) != 0;

    
END


/* 80 */
CREATE PROCEDURE driversInfo()
BEGIN

/*order by two things: driver_name and date

create names table and dates table, join on driver_name*/

CREATE TABLE IF NOT EXISTS Names (
    min_date date,
    driver_name VARCHAR(20),
    NamesInfo VARCHAR(100)
);

INSERT INTO Names
SELECT date, driver_name, NamesInfo FROM
    (SELECT 
         (MIN(date) - INTERVAL 1 DAY) AS date,
         driver_name, 
         CONCAT(' Name: ', driver_name, '; number of inspections: ', 
                   COUNT(driver_name), '; miles driven: ', SUM(miles_logged)) AS NamesInfo
     FROM inspections
     GROUP BY driver_name) AS t1;


CREATE TABLE IF NOT EXISTS Dates (
    inspection_date date,
    driver_name VARCHAR(20),
    InspectionsInfo VARCHAR(100)
);

INSERT INTO Dates
SELECT date, driver_name, InspectionsInfo FROM
    (SELECT
        date,
        driver_name,
        CONCAT('  date: ', date, '; miles covered: ', miles_logged) AS InspectionsInfo
     FROM inspections) AS t3;


SELECT *
FROM
    (SELECT CONCAT(' Total miles driven by all drivers combined: ', SUM(miles_logged)) AS summary
    FROM inspections) AS t3
    UNION
    (SELECT info
    FROM
        (SELECT *
        FROM
            (SELECT min_date AS date, driver_name, NamesInfo AS info FROM Names) AS t1
            UNION
            (SELECT inspection_date AS date, driver_name, InspectionsInfo AS info FROM Dates)
        ORDER BY driver_name, date) AS t2);



DROP TABLE Names;
DROP TABLE Dates;
    
END

/* 81 */
CREATE FUNCTION RomanToArabic(number VARCHAR(50)) RETURNS INT DETERMINISTIC
BEGIN
    /* store a total, set it to zero (also store a LSNV (last seen numeral value), set it to zero)
       start from the rightmost roman numeral
           get its numeral value -- store it in CNV
           if CNV < LSNV:
               add its negation to the total
           else
               add it to the total
           LSNV = CNV
       return the total
    */
        
    SET @total = 0;
    SET @LSNV = 0;
    SET @remainingString = number;

    WHILE LENGTH(@remainingString) > 0 DO
        SET @CNV = (SELECT Value FROM RomanNumerals WHERE Symbol = RIGHT(@remainingString, 1));
        IF @CNV < @LSNV THEN SET @total = @total - @CNV;
        ELSE SET @total = @total + @CNV;
        END IF;
        SET @LSNV = @CNV;
        SET @remainingString = LEFT(@remainingString, LENGTH(@remainingString)-1);
    END WHILE;
    
    RETURN @total;

END;


CREATE PROCEDURE sortBookChapters()
BEGIN
    
/* write a function */
/* parse from right to left */

CREATE TABLE IF NOT EXISTS RomanNumerals (
    Symbol VARCHAR(1),
    Value INT
);

INSERT INTO RomanNumerals (Symbol, Value)
VALUES
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000);


SELECT chapter_name
FROM
    (SELECT chapter_name, 
           chapter_number AS chapter_number_roman, 
           RomanToArabic(chapter_number) AS chapter_number_arabic
    FROM book_chapters
    ORDER BY chapter_number_arabic) AS t1;



DROP TABLE RomanNumerals;

END


/* 82 */
/* THIS SOLUTION TAKES TOO LONG - TIMES OUT ON FINAL TEST */
CREATE PROCEDURE typeInheritance()
BEGIN

/* maybe use find_in_set, group_concat somehow */

CREATE TABLE IF NOT EXISTS main_set (
    type VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS inheritance2 (
    derived VARCHAR(20),
    base VARCHAR(20)
);

INSERT INTO inheritance2
SELECT * FROM inheritance;

INSERT INTO main_set
SELECT derived FROM inheritance WHERE base = 'Number';

SET @iterator = 0;
SET @rowCount = (SELECT COUNT(*) FROM inheritance2);

WHILE @iterator < @rowCount DO

INSERT INTO main_set
SELECT derived
FROM inheritance2 JOIN main_set
    ON inheritance2.base = main_set.type;

SET @a = (SELECT GROUP_CONCAT(main_set.type SEPARATOR ', ') FROM main_set);

DELETE FROM inheritance2
WHERE FIND_IN_SET(inheritance2.base, @a) != 0;

SET @iterator:= @iterator + 1;
SET @rowCount = (SELECT COUNT(*) FROM inheritance2);

END WHILE;

SELECT DISTINCT var_name, variables.type AS var_type
FROM main_set JOIN variables
ON main_set.type = variables.type
ORDER BY var_name;

DROP TABLE main_set;
DROP TABLE inheritance2;

    
END