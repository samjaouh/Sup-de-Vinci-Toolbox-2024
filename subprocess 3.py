from tkinter import *
from tkinter import filedialog, messagebox
import subprocess


# Fonction pour exécuter les commandes
def execute_commands():

    #recupère la valeur du fichier sélectionné 
    filename = entry_file.get()

    # Vérification si le champ de fichier est vide
    if not filename:
        messagebox.showerror("Erreur", "Veuillez sélectionner un fichier contenant les commandes.")
        return

    # Récupération de l'adresse IP et de l'URL
    ip_address = entry_ip.get()
    url = entry_url.get()

    # Déclaration  du dictionnaire qui servira à stocker les commentaires et les commandes
    commands_dict = {}

    # Lecture du fichier et constitution du dictionnaire de commandes
    with open(filename, "r") as file:
        comment = ""
        for line in file:
            line = line.strip()
            # Si la ligne commence par "#" => commentaire qui va servier pour le rapport 
            if line.startswith("#"):
                # on stoque le commentaire dans la variable comment
                comment = line[1:].strip()
            # Sinon et si la ligne n'est pas vide => commande qui sera exécutée 
            elif line: 
                # on stoque la commande dans le dictionnaire avec le commentaire comme clé
                commands_dict[comment] = line  
                # on réinitialise la variable comment
                comment = ""  

    # déclaration  de la liste de process => comandes à excécutée 
    processes = []

    for comment, command in commands_dict.items():

        # Ajout de l'adresse IP et de l'URL à la commande
        command_with_ip = command.replace("IP_ADDRESS", ip_address)
        command_with_ip_and_url = command_with_ip.replace("URL", url)

        # Exécute les commandes en parallèle dans des processus séparés
        process = subprocess.Popen(command_with_ip_and_url, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        #si le process à pu s'exécuter 
        if process: 

           # Attente de la fin de l'exécution du processus et récupération des sorties
           output, error = process.communicate()

           # Conversion des sorties en chaînes de caractères
           output = output.decode().strip()
           error = error.decode().strip()

           # on lit les sorties des commandes 
           if not output and not error and process.poll() is not None:
              break
           #is execution OK 
           if output:
                output_file = f"result_{comment}.txt"
                with open(output_file, "w") as file:
                    file.write("################################################################################################\n")
                    file.write(f"Exécution de : {comment}\n")
                    file.write(f"Ligne de commande exécutée: {command_with_ip_and_url}\n")
                    file.write("################################################################################################\n")
                    file.write(f"Résultats pour la commande '{command}' enregistrés dans le fichier : {output_file}\n")
                    file.write(output)
                    file.write(f"\n")
                    file.write("###################### FIN EXECUTION COMMANDE ###################################################\n")
                #print pour tests a commenter pour la version finale 
                print(f"Résultats pour le commentaire '{comment}' enregistrés dans le fichier : {output_file}")
                print(f"Sortie de la commande : {output}")
           #si execution ko 
           if error:
                error_file = f"result_{comment}.txt"
                with open(error_file, "w") as file:
                    file.write("################################################################################################\n")


root = Tk()
root.title("Execution de commandes")

# Fonction pour sélectionner le fichier
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file.delete(0, END)
        entry_file.insert(0, file_path)

# Fonction pour exécuter les commandes
#def execute_commands():
 #   filename = entry_file.get()
 #   ip_address, url = get_ip_and_url()

    # Vérification si le champ de fichier est vide
 #   if not filename:
 #       messagebox.showerror("Erreur", "Veuillez sélectionner un fichier contenant les commandes.")
 #       return

    # Reste du code...

# Fonction pour récupérer l'adresse IP et l'URL
def get_ip_and_url():
    ip = entry_ip.get().strip()
    url = entry_url.get().strip()
    return ip, url

# Création du champ de saisie pour le fichier
entry_file = Entry(root, width=50)
entry_file.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Création du bouton de parcour
button_browse = Button(root, text="Parcourir", command=select_file)
button_browse.grid(row=0, column=3, padx=10, pady=10)

# Création du champ de saisie pour l'adresse IP
entry_ip = Entry(root, width=20)
entry_ip.grid(row=1, column=0, padx=10, pady=5)
label_ip = Label(root, text="Adresse IP:")
label_ip.grid(row=1, column=1, padx=10, pady=5)

# Création du champ de saisie pour l'URL
entry_url = Entry(root, width=50)
entry_url.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
label_url = Label(root, text="URL:")
label_url.grid(row=2, column=1, padx=10, pady=5)

# Création du bouton d'exécution
button_execute = Button(root, text="Exécuter", command=execute_commands)
button_execute.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
