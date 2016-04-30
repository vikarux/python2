#!/usr/bin/env python
import sys, MySQLdb

def PrintFields(database, table):
    """ Connects to the table specified by the user and prints out its fields in HTML format used by Ben's wiki. """
    host = raw_input('localhost')
    user = raw_input('user name')
    db = raw_input('Server')
    password = raw_input('password')
    conn = MySQLdb.Connection(db=database, host=host, user=user, passwd=password)
    mysql = conn.cursor()
    sql = "update tbl_UserActivity"
            "set UserBlock = '0'"
            "UserLastActivityDate = GETDATE ()"
            "where UserName in ('ka4750' ) "
    mysql.execute(sql)
    fields=mysql.fetchall()
    print '<table border="0"><tr><th>order</th><th>name</th><th>type</th><th>description</th></tr>'
    print '<tbody>'
    counter = 0
    for field in fields:
        counter = counter + 1
        name = field[0]
        type = field[1]
        print '<tr><td>' + str(counter) + '</td><td>' + name + '</td><td>' + type + '</td><td></td></tr>'
    print '</tbody>'
    print '</table>'
    mysql.close()
    conn.close()

users_database = sys.argv[1]
users_table = sys.argv[2]
print "Wikified HTML for " + users_database + "." + users_table
print "========================"
PrintFields(users_database, users_table)