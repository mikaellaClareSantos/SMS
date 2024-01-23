from StudDb import StudDb
from StudGuiCtk import StudGuiCtk
from StudDbSqlite import StudDbSqlite

def main():
    db = StudDb(init=False, dbName='StudDb.csv')
    app = StudGuiCtk(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()