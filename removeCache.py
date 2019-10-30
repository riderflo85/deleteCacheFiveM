import os, getpass, sys


########## Define all functions ##########
def other_path():
    print("L'emplacement du cache n'a pas été trouver.\n\
            Merci de renseigner l'emplacement de votre installation")
    print("exemple: C:\\User\\Emplacement\\fiveM")
    path_user = input('>>>')
    return path_user

def remove_cache(directory_cache):
    listing_directory = os.listdir(os.chdir(directory_cache))
    for i in listing_directory:
        if i != 'game':
            os.remove(i)
        else:
            pass

    return True

def quit_script():
    the_end = input('Appuyer sur la touche entrée pour quitter')
    return the_end
#########################################


########## Start script ##########
print('Suppresion de cache FiveM\nBy DevOne')
try:
    default_directory = f"C:\\Users\\{ getpass.getuser }\\AppData\\Local\\FiveM\\cache"
    if remove_cache(default_directory):
        print('Suppression du cache terminé avec succès')
    else:
        print('Erreur lors de la suppression')
except:
    print("Votre dossier d'installation est différente de celle d'origine.\n")
    path = other_path()
    if remove_cache(path):
        print('Suppression terminé avec succès')
    else:
        print('Une erreur est survenue...')
finally:
    if quit_script() == "":
        sys.exit()
    else:
        sys.exit()
##################################
