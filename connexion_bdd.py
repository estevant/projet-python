import mysql.connector
from mysql.connector import errorcode

def get_connection():
    try:
        config = {
            'host': "127.0.0.1",
            'port':3306,
            'user': "root",
            'password': "",
            'database': "hopital"
        }
        
        connexion = mysql.connector.connect(**config)
        return connexion

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erreur: Faux nom d'utilisateur ou mot de passe.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Erreur: La base de données 'hopital' n'existe pas.")
        else:
            print(f"Erreur de connexion: {err}")
        return None
    
