import psycopg2

def get_args(filename):
    f = open(filename)
	
    con = psycopg2.connect(database='beacon_db', user='reggibeacon', password='temppass', host='localhost')
    cur = con.cursor()

    while True:
        courseNum = f.readline()[:-1]
        courseName = f.readline()[:-1]
        
        if not courseNum:
            break

        sqlquery = """INSERT INTO "CourseData_universitycourses" ("courseNum", "courseName") VALUES (""" + courseNum + ", '" + courseName + "');"
        cur.execute(sqlquery)

    con.commit()
    f.close()
    con.close()
def main():
    get_args('2013springnumtoname.txt')

if __name__ == '__main__':
    main()
