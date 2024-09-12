import os
import dotenv
import pymysql
import pymysql.cursors

def conn():

    dotenv.load_dotenv()
    CURRENT_CURSOR = pymysql.cursors.DictCursor

    connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            # port=int(os.getenv('PORT')),
            charset='utf8mb4',
            cursorclass=CURRENT_CURSOR,
        )
    return connection