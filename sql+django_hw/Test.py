import sqlite3

conn = sqlite3.connect("C:/Users/Rudy451/app_academy/aA-homeworks/sql_hw/plays.db")
curr = conn.cursor()

curr.execute("SELECT * FROM plays")
print(curr.fetchall())

curr_list = [name for name in conn.execute("pragma table_info(plays)")]
print([curr_list[spot][1] for spot in range(0, len(curr_list))])
curr.close()
