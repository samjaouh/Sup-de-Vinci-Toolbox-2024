from tkinter import *
from tkinter import filedialog, messagebox
import subprocess
import os

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

    # Boucle sur le dictionnaire des commandes
    for comment, command in commands_dict.items():
        # Remplacement des placeholders IP_ADDRESS et URL par les valeurs récupérées
        command_with_ip = command.replace("IP_ADDRESS", ip_address)
        command_with_ip_and_url = command_with_ip.replace("URL", url)

        # Nom du fichier basé sur la commande pour enregistrer la sortie
        safe_command_name = command.replace(" ", "_").replace("/", "_").replace("\\", "_")
        result_file_path = f"{safe_command_name}_results.txt"

        # Exécution des commandes en parallèle dans des processus séparés
        process = subprocess.Popen(command_with_ip_and_url, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        
        # Attente de la fin de l'exécution du processus et récupération des sorties
        output, error = process.communicate()
        output = output.decode().strip()
        error = error.decode().strip()

        # Enregistrement des résultats de la commande
        with open(result_file_path, "w") as result_file:
            result_file.write("Sortie de la commande:\n")
            result_file.write(output + "\n")
            if error:
                result_file.write("Erreurs rencontrées:\n")
                result_file.write(error + "\n")

    # Affichage de la boîte de dialogue d'information une fois toutes les commandes exécutées
    messagebox.showinfo("Exécution Terminée", "Toutes les commandes ont été exécutées avec succès.")

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
