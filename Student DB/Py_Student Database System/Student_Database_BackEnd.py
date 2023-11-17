#BackEnd
import sqlite3

def StudentData():
    Connect=sqlite3.connect("Student.db")
    cur=Connect.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS Student(
       Id INTEGER PRIMARY KEY,
       Student_ID TEXT,
       First_Name TEXT,
       Sur_Name TEXT,
       DOB TEXT,
       Age TEXT,
       Gender TEXT,
       Address TEXT,
       Phone_Number TEXT
    );
    ''')
    Connect.commit()
    Connect.close()

def AddStudentRecord(StudentID,FirstName,SurName,DOB,Age,Gender,Address,PhoneNumber):
    Connect=sqlite3.connect("Student.db")
    cur=Connect.cursor()
    cur.execute('''INSERT INTO Student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ? ) ''', ( StudentID, FirstName, SurName, DOB, Age, Gender, Address, PhoneNumber) )
    Connect.commit()
    Connect.close()

def ViewData():
    Connect=sqlite3.connect("Student.db")
    cur=Connect.cursor()
    cur.execute("SELECT * FROM Student")
    rows=cur.fetchall()
    Connect.close()
    return rows

def DeleteRecord(id):
    Connect=sqlite3.connect("Student.db")
    cur=Connect.cursor()
    cur.execute("DELETE FROM Student WHERE id = ?", ( id, ) )
    Connect.commit()
    Connect.close()

def DataUpdate(StudentID="",FirstName="",SurName="",DOB="",Age="",Gender="",Address="",PhoneNumber=""):
    Connect=sqlite3.connect("Student.db")
    cur=Connect.cursor()
    cur.execute('''UPDATE Student SET Student_ID=?, First_Name=?, Sur_Name=?, DOB=?, Age=?, Address=?, Phone_Number=?, WHERE id=?''', ( StudentID, FirstName, SurName, DOB, Age, Gender, Address, PhoneNumber, id) )
    Connect.commit()
    Connect.close()

def SearchData(StudentID="",FirstName="",SurName="",DOB="",Age="",Gender="",Address="",PhoneNumber=""):
    Connect=sqlite3.connect("Student.db")
    cur=Connect.cursor()
    cur.execute('''SELECT * FROM Student WHERE Student_ID=? OR First_Name=? OR Sur_Name=? OR DOB=? OR Age=? OR Gender=? OR Address=? OR Phone_Number=?''',( StudentID, FirstName, SurName, DOB, Age, Gender, Address, PhoneNumber) )
    rows=cur.fetchall()
    Connect.close()
    return rows

StudentData()
