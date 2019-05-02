#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect("profile.db")

with connection:
    connection.execute("DROP TABLE IF EXISTS profile_data")
    connection.execute("CREATE TABLE profile_user(username CHAR(10), password VARCHAR(100),Full_Name VARCHAR(50),Email VARCHAR(30))")
    connection.execute("CREATE TABLE profile_user_login(username CHAR(10), password VARCHAR(15))")
connection.close()
