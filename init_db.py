import sqlite3

conn = sqlite3.connect('math_problems.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    statement TEXT NOT NULL
)
''')

# Example data
c.execute("INSERT INTO problems (title, statement) VALUES (?, ?)",
          ("Pythagorean Theorem", "In a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides."))
c.execute("INSERT INTO problems (title, statement) VALUES (?, ?)",
          ("Quadratic Formula", "The solutions to ax^2 + bx + c = 0 are given by x = [-b ± sqrt(b^2-4ac)]/(2a)."))

conn.commit()
conn.close()
