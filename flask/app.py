from flask import Flask
import pyodbc
from dotenv import dotenv_values, load_dotenv

app = Flask(__name__)

load_dotenv()
config = dotenv_values(".env")


DRIVER = '{ODBC Driver 18 for SQL Server}'
cnxn = pyodbc.connect("""
                        DRIVER={0};
                        SERVER={1};
                        DATABASE={2};
                        UID={3};
                        PWD={4};
                        ENCRYPT=yes;
                        TRUSTSERVERCERTIFICATE=yes;
                        """.format(
                          DRIVER,
                          config["SERVER"],
                          config["DATABASE"],
                          config["USERNAME"],
                          config["PASSWORD"]
                          )
                      )
cursor = cnxn.cursor()


@app.route("/")
def hello():
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    while row:
        return row[0]
