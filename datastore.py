import sqlite3

class Datastore:
    
    def __init__(self, db_file_name: str):
        """
        Initate datastore object
        """
        
        self.connection = sqlite3.connect(db_file_name)
        self.cursor = self.connection.cursor()
        
        # populate database
        self.build_db()
        
        
    def __del__(self):
        """
        Writes data from cache to drive and then closes connection
        """
        self.connection.close()

        
    def build_db(self):
        """
        Creates the newflix database
        """
        
        # create rating table
        self.cursor.execute(
            """
            CREATE TABLE rating_tb(
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        
        # create show table
        self.cursor.execute(
            """
            CREATE TABLE show_tb(
                show_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                type TEXT NOT NULL,
                date_added TEXT,
                release_year INTEGER NOT NULL CHECK(release_year > 1900),
                rating INTEGER,
                duration TEXT NOT NULL,
                description TEXT,
                FOREIGN KEY (rating) REFERENCES rating_tb(rating_id)
            )
            """
        )
        
        # create director table
        self.cursor.execute(
            """
            CREATE TABLE director_tb(
                dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        
        # create show director table
        self.cursor.execute(
            """
            CREATE TABLE show_director_table(
                show_id TEXT NOT NULL,
                dir_id INTEGER NOT NULL,
                PRIMARY KEY (show_id, dir_id)
                FOREIGN KEY (show_id) REFERENCES show_tb(show_id)
                FOREIGN KEY (dir_id) REFERENCES director_tb(dir_id)
            )
            """
        )
        
        # create actor table
        self.cursor.execute(
            """
            CREATE TABLE actor_tb(
                actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        
        # create cast table
        self.cursor.execute(
            """
            CREATE TABLE cast_tb(
                show_id TEXT NOT NULL,
                actor_id INTEGER NOT NULL,
                PRIMARY KEY (show_id, actor_id),
                FOREIGN KEY (show_id) REFERENCES show_tb(show_id),
                FOREIGN KEY (actor_id) REFERENCES actor_tb(actor_id)
            )
            """
        )
        
        # create country table
        self.cursor.execute(
            """
            CREATE TABLE country_tb(
                country_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        
        # create show country table
        self.cursor.execute(
            """
            CREATE TABLE show_country_tb(
                show_id TEXT NOT NULL,
                country_id INTEGER NOT NULL,
                PRIMARY KEY (show_id, country_id),
                FOREIGN KEY (show_id) REFERENCES show_tb(show_id),
                FOREIGN KEY (country_id) REFERENCES country_tb(country_id)
            )
            """
        )
        
        # create category table
        self.cursor.execute(
            """
            CREATE TABLE category_tb(
                cat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        
        # create show category table
        self.cursor.execute(
            """
            CREATE TABLE show_category_tb(
                show_id TEXT NOT NULL,
                cat_id INTEGER NOT NULL,
                PRIMARY KEY (show_id, cat_id),
                FOREIGN KEY (show_id) REFERENCES show_tb(show_id),
                FOREIGN KEY (cat_id) REFERENCES category_tb(cat_id)
            )
            """
        )
        
        self.connection.commit()