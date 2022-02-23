import psycopg2
from psycopg2 import Error
import os

# Connect to an existing database
db_user = os.environ.get("DB_USER")
db_pw = os.environ.get("DB_PW")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
def conn():
    connection = psycopg2.connect(
                                user=db_user,
                                password=db_pw,
                                host=db_host,
                                port=db_port,
                                database=db_name
                                )
    return connection
def createT():
    con = conn()
    cur = con.cursor()
    create_table = """
                   CREATE TABLE event
                   (NAME    TEXT    PRIMARY KEY    NOT NULL,
                    WOODCUTTING    INT    NOT NULL,
                    MINING    INT NOT NULL);
                   """
    cur.execute(create_table)
    con.commit()
    cur.close()
    con.close()
    return True



def insert(m_name,m_wc,m_mining):
    cur = connection.cursor()
    insert_query = """ 
                    INSERT INTO event (NAME,WOODCUTTING,MINING) 
                    VALUES ('m_name',%s,'m_wc',%s,'m_mining',%s)
                    """
    cur.execute(insert_query,count)
    connection.commit()
    cur.close()

def update(m_name,m_wc,m_mining):
    cur = connection.cursor()
    update_wc_query = """
                    Update event
                    set woodcutting = %s
                    where name = {m_name}
                    """
    update_mining_query = """
                    Update event
                    set mining = %s
                    where name = {m_name}
                    """
    cur.execute(update_wc_query,(m_wc,),update_mining_query,(m_mining,))
    connection.commit()
    cur.close()


def retrieve(skill):
    cur = connection.cursor()
    cur.execute("SELECT {skill} FROM event ORDER BY {skill}")
    row = cur.fetchone()
    while row is not None:
        skill_data = int(row)
        row = cur.fetchone()
    connection.commit()
    cur.close()
    return count
