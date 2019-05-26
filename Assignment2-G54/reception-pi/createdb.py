"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is creating the database in local.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""
#!/usr/bin/env python3
import sqlite3
# a local database is created named:profile.db
connection = sqlite3.connect("profile.db")
"""
    Check if the local database have the table "profile_data" or not
    If it is not existing,creating the table and aslo named four columns header

"""
with connection:
    connection.execute("DROP TABLE IF EXISTS profile_data")
    connection.execute(
        "CREATE TABLE profile_user(username CHAR(10), password VARCHAR(500),Full_Name VARCHAR(50),Email VARCHAR(100))")

# close the database connection once table is created
connection.close()
