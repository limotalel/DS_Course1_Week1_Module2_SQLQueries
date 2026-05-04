import pandas as pd
import sqlite3

# CodeGrade step0 - planets
conn1 = sqlite3.connect("planets.db")

# CodeGrade step1
df_no_moons = pd.read_sql(
    """
SELECT *
FROM planets
WHERE num_of_moons = 0
""",
    conn1,
)

# CodeGrade step2
df_name_seven = pd.read_sql(
    """
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7
""",
    conn1,
)

# CodeGrade step3
df_mass = pd.read_sql(
    """
SELECT name, mass
FROM planets
WHERE mass <= 1.00
""",
    conn1,
)

# CodeGrade step4
df_mass_moon = pd.read_sql(
    """
SELECT *
FROM planets
WHERE num_of_moons >= 1 AND mass < 1.00
""",
    conn1,
)

# CodeGrade step5
df_blue = pd.read_sql(
    """
SELECT name, color
FROM planets
WHERE color LIKE '%blue%'
""",
    conn1,
)

# CodeGrade step0 - dogs
conn2 = sqlite3.connect("dogs.db")

# CodeGrade step6
df_hungry = pd.read_sql(
    """
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC
""",
    conn2,
)

# CodeGrade step7
df_hungry_ages = pd.read_sql(
    """
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1 AND age BETWEEN 2 AND 7
ORDER BY name
""",
    conn2,
)

# CodeGrade step8
df_4_oldest = pd.read_sql(
    """
SELECT name, age, breed
FROM (SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4)
ORDER BY breed
""",
    conn2,
)

# CodeGrade step0 - babe_ruth
conn3 = sqlite3.connect("babe_ruth.db")

# CodeGrade step9
df_ruth_years = pd.read_sql(
    """
SELECT COUNT(*) AS num_years
FROM babe_ruth_stats
""",
    conn3,
)

# CodeGrade step10
df_hr_total = pd.read_sql(
    """
SELECT SUM(HR) AS total_HR
FROM babe_ruth_stats
""",
    conn3,
)

# CodeGrade step11
df_teams_years = pd.read_sql(
    """
SELECT team, COUNT(*) AS number_years
FROM babe_ruth_stats
GROUP BY team
""",
    conn3,
)

# CodeGrade step12
df_at_bats = pd.read_sql(
    """
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200
""",
    conn3,
)

conn1.close()
conn2.close()
conn3.close()
