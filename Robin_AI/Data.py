import mysql.connector as dat
import GUI_Creator
from mysql.connector import errorcode
from Responses_Keys import *
import traceback

def main_function(save=True, user=default_settings_dict["User_Name"], voice=default_settings_dict["Voice"]):
    # UserData
    user_dat = dat.connect(
        host="localhost",
        user="root",
        password="root"
    )
    my_cursor = user_dat.cursor()

    # Database Creation Function
    def create_database(my_cursor):
        try:
            my_cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format("Robin"))
        except dat.Error as err:
            GUI_Creator.fatal(0, True, "Failed to create database: {}".format(err), "Warn")
        except:
            a = traceback.format_exc()
            GUI_Creator.fatal(0, True, a, "Warn")


    try:
        my_cursor.execute("USE {}".format("Robin"))
    except dat.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(my_cursor)
            user_dat.database = "Robin"
        else:
            GUI_Creator.fatal(0, True, err, "Warn")
    except:
        b = traceback.format_exc()
        GUI_Creator.fatal(0, True, b, "Warn")

    # Tables
    Tables = {}
    Tables['Settings'] = (
        "CREATE TABLE Settings (`S.No.` INT AUTO_INCREMENT PRIMARY KEY, `User` VARCHAR(255), `Voice` VARCHAR(255))"
    )

    for table_name in Tables:
        table_description = Tables[table_name]
        try:
            my_cursor.execute(table_description)
        except dat.Error as err:
            if err.errno != errorcode.ER_TABLE_EXISTS_ERROR:
                GUI_Creator.fatal(0, True, err, "Warn")
        except:
            c = traceback.format_exc()
            GUI_Creator.fatal(0, True, c, "Warn")

    # Fetching the first row
    def fetch_row():
        my_cursor.execute("SELECT * FROM Settings")
        rows = my_cursor.fetchone()
        return rows


    # Data saving 
    def save_data():
        rows = fetch_row()

        if rows is None:
            try:
                sql = "INSERT INTO Settings (User, Voice) VALUES (%s, %s)"
                val = (user, voice)
                my_cursor.execute(sql, val)
                user_dat.commit()
            except dat.Error as err:
                GUI_Creator.fatal(0, True, err, "Warn")
            except:
                d = traceback.format_exc()
                GUI_Creator.fatal(0, True, d, "Warn")
        else:
            try:
                sql_update = "UPDATE Settings SET `User`=%s, `Voice`=%s WHERE `S.No.`=%s"
                value_update = (user, voice, 1)
                my_cursor.execute(sql_update, value_update)
                user_dat.commit()
            except dat.Error as err:
                GUI_Creator.fatal(0, True, err, "Warn")
            except:
                e = traceback.format_exc()
                GUI_Creator.fatal(0, True, e, "Warn")


    def load_data():
        # Data Loading
        rows_again = fetch_row() #0 -> S.No., 1 -> User, 2 -> Voice
        if rows_again is None:
            save_data()
        
        rows_again = fetch_row()

        data = {
            "User" : rows_again[1],
            "Voice" : rows_again[2]
        }
        return data


    if save:
        save_data()
    else:
        data_recieved = load_data()
        return data_recieved
