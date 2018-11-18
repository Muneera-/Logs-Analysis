#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Muneera AlRashidi
# FSND logs analysis project
import psycopg2

DBNAME = "news"

Question_1 = "1. What are the most popular three articles of all time?"

Question_2 = "2. Who are the most popular article authors of all time? "

Question_3 = "3. On which days did more than 1% of requests lead to errors?"
file = open('output.txt', 'w')


def question_1_answer():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute('''select articles.title, count (articles.title)
    AS numberOfViews FROM articles , log
    WHERE log.status= '200 OK'
        AND log.path like '/article/%'||articles.slug||'%'
        GROUP BY articles.title ORDER BY numberOfViews DESC limit 3;''')
    result = cursor.fetchall()
    print Question_1, ": \n"
    file.write(Question_1+": \n")
    for x in result:
        print "\t", '"' + x[0] + '"', " - ", x[1], "views"
        file.write("\t" + '"' + str(x[0]) + '"' +
                   " — " + str(x[1]) + " views" + "\n")
    db.close()
    return " "


def question_2_answer():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute('''select authors.name, COUNT(articles.title)
    AS numberOfViews FROM articles , log, authors
    WHERE articles.author = authors.id
    GROUP BY authors.name ORDER BY numberOfViews DESC;''')
    result = cursor.fetchall()
    print Question_2, ": \n"
    file.write(Question_2+": \n")
    for x in result:
        print "\t", x[0], " - ", x[1], "views"
        file.write("\t" + '"' + str(x[0]) +
                   " — " + str(x[1]) + " views" + "\n")
    db.close()
    return " "


def question_3_answer():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute('''select to_char(date,'FMMONTH FMDD, YYYY'),
    round(percentage,2)
    FROM failedRequestsRate WHERE percentage > 1
    ORDER BY percentage DESC;''')
    result = cursor.fetchall()
    print Question_3, ": \n"
    file.write(Question_3+": \n")
    for x in result:
        print "\t", x[0], " - ", x[1], "% errors"
        file.write("\t" + str(x[0]) +
                   " — " + str(x[1]) + "% errors" + "\n")
    db.close()
    return " "


if __name__ == '__main__':
    print question_1_answer()
    print question_2_answer()
    print question_3_answer()
    file.close()
