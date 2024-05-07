from tkinter import *
from tkinter import filedialog, messagebox
import subprocess

# Fonction pour exécuter les commandes
def execute_commands():
    # Récupération du chemin du fichier sélectionné
    filename = entry_file.get()

    # Vérification si le champ de fichier est vide
    if not filename:
        messagebox.showerror("Erreur", "Veuillez sélectionner un fichier contenant les commandes.")
        return

    # Récupération de l'adresse IP et de l'URL depuis les champs de saisie
    ip_address = entry_ip.get()
    url = entry_url.get()

    # Déclaration du dictionnaire pour stocker les commentaires et les commandes
    commands_dict = {}

    # Lecture du fichier et constitution du dictionnaire de commandes
    with open(filename, "r") as file:
        comment = ""
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                comment = line[1:].strip()
            elif line:
                commands_dict[comment] = line
                comment = ""

    # Déclaration de la liste des processus (commandes à exécuter)
    processes = []

    # Boucle sur le dictionnaire des commandes
    for comment, command in commands_dict.items():
        # Remplacement des placeholders IP_ADDRESS et URL par les valeurs récupérées
        command_with_ip = command.replace("IP_ADDRESS", ip_address)
        command_with_ip_and_url = command_with_ip.replace("URL", url)

        # Exécution des commandes en parallèle dans des processus séparés
        process = subprocess.Popen(command_with_ip_and_url, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        # Vérification si le processus s'est bien exécuté
        if process:
            # Attente de la fin de l'exécution du processus et récupération des sorties
            output, error = process.communicate()
            output = output.decode().strip()
            error = error.decode().strip()

            # Vérification des sorties des commandes
            if not output and not error and process.poll() is not None:
                break

            # Si la sortie de la commande est présente
            if output:
                # Création d'un fichier de sortie et écriture des résultats
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
                # Affichage des résultats dans la console (peut être commenté pour la version finale)
                print(f"Résultats pour le commentaire '{comment}' enregistrés dans le fichier : {output_file}")
                print(f"Sortie de la commande : {output}")

            # Si une erreur est survenue lors de l'exécution de la commande
            if error:
                # Création d'un fichier d'erreur et écriture du message d'erreur
                error_file = f"result_{comment}.txt"
                with open(error_file, "w") as file:
                    file.write("################################################################################################\n")
                    file.write("ERREUR lors de l'exécution de la commande :\n")
                    file.write(f"{command_with_ip_and_url}\n")
                    file.write("################################################################################################\n")
                    file.write(f"Erreur : {error}\n")
                    file.write("###################### FIN EXECUTION COMMANDE ###################################################\n")

# Création de la fenêtre principale
root = Tk()
root.title("Execution de commandes")

# Fonction pour sélectionner le fichier de commandes
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file.delete(0, END)
        entry_file.insert(0, file_path)

# Création du champ de saisie pour le fichier de commandes
entry_file = Entry(root, width=50)
entry_file.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Création du bouton de parcours de fichier
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
label_url = Label(root, text="URL (sans http/https):")
label_url.grid(row=2, column=1, padx=10, pady=5)

# Création du bouton d'exécution des commandes
button_execute = Button(root, text="Exécuter", command=execute_commands)
button_execute.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Lancement de la boucle principale de l'interface graphique
root.mainloop()
