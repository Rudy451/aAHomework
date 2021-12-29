import sqlite3;

class Play:

    def __init__(self, options):
        self.options = options
        con = sqlite3.connect(self.options)
        curr = con.cursor()
        curr_list = [col_name for col_name in con.execute("pragma table_info(plays)")]
        self.id = curr_list[0][1]
        self.title = curr_list[1][1]
        self.year = curr_list[2][1]
        self.playwright_id = curr_list[3][1]
        curr.execute("SELECT * FROM plays")
        print(curr.fetchall())
        curr.close()

    def create(self, title, year, play_wright_id):
        try:
            assert self.id
            self.title = title
            self.year = year
            self.playwright_id = play_wright_id
            con = sqlite3.connect(self.options)
            curr = con.cursor()
            curr.execute("INSERT INTO plays(title, year, playwright_id) VALUES (?, ?, ?)", (self.title, self.year, self.playwright_id))
            curr.execute("SELECT * FROM plays")
            result = curr.fetchall()
            self.id = result[len(result) - 1]
            print(self.id[0])
            con.commit()
            con.close()
        except AssertionError:
            print("Already in database")

    def update(self, title, year, playwright_id, id):
        try:
            con = sqlite3.connect(self.options)
            curr = con.cursor()
            curr.execute("UPDATE plays SET title  = ?, year = ?, playwright_id = ? WHERE id = ?", (title, year, playwright_id, id))
            curr.execute("SELECT * FROM plays")
            result = curr.fetchall()
            assert len(result) > 0
            print(result)
            con.commit()
            curr.close()
        except AssertionError:
            print("Not in database")

    def find_by_title(self, title):
        con = sqlite3.connect(self.options)
        curr = con.cursor()
        curr.execute("SELECT * FROM plays WHERE title = ?", (title,))
        print(curr.fetchall())
        curr.close()

    def find_by_playwright(self, name):
        con = sqlite3.connect(self.options)
        curr = con.cursor()
        curr.execute("SELECT * FROM plays WHERE playwright_id = ?", (name,))
        print(curr.fetchall())
        curr.close()

my_test = Play("plays.db")
my_test.create("Death of a Salesman", 1949, "Arthur Miller")
my_test.create("Fences", 1984, "August Wilson")
my_test.update("Fences", 1985, "August Wilson", 4)
my_test.find_by_title("Fences")
my_test.find_by_playwright("Arthur Miller")
