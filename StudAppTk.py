from StudDb import StudDb
from StudGuiTk import StudGuiTk

def main():
    db = StudDb(init=False, dbName='StudDb.csv')
    app = StudGuiTk(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()