from connexion_bdd import get_connection
import bcrypt

# fonction de connexion
def login_system():
    connexion = get_connection()
    if connexion is None:
        return None

    cursor = connexion.cursor()

    max_tentatives = 3
    tentatives = 0

    while tentatives < max_tentatives:
        print("\nAuthentification requise")
        login_saisi = input("Login : ")
        password_saisi = input("Mot de passe : ")

        sql = "SELECT nom, role, password FROM users WHERE login = %s"
        cursor.execute(sql, (login_saisi,))

        user_trouve = cursor.fetchone()

        if user_trouve:
            nom_user = user_trouve[0]
            role_user = user_trouve[1]
            password_hash_bdd = user_trouve[2]

            if bcrypt.checkpw(password_saisi.encode('utf-8'), password_hash_bdd.encode('utf-8')):  # vérifie si le mdp correspond au hash de la bdd
                print(f"Bienvenue {nom_user} (Vous êtes connecté en tant que : {role_user})")
                cursor.close()
                connexion.close()
                return role_user, login_saisi
            else:
                print("Identifiants incorrects.")
        else:
            print("Identifiants incorrects.")

        tentatives += 1 #rajoute une tentative au compteur quand il y a un echec

        if tentatives < max_tentatives:
            print(f"Tentative {tentatives}/{max_tentatives} échouée.")
        else:
            print("Nombre de tentatives dépassé. Fin du programme.")

    cursor.close()
    connexion.close()
    return None