import urllib
import mysql.connector
import data_scrapes

def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="pythonuser",
        passwd="password",
        auth_plugin='mysql_native_password'
    )
    print(mydb)

    indeed_frame = data_scrapes.get_indeed()
    #glassdoor_frame = data_scrapes.get_glassdoor()
    print(indeed_frame.describe())



if __name__== "__main__":
    main()
