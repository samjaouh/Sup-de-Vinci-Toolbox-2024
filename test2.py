from tkinter import *
from tkinter import filedialog, messagebox
import subprocess
import os
import threading
import datetime

# Liste pour stocker les processus en cours d'exécution
processes = []
current_process = None
current_command_index = 0
commands_dict = {}
is_cancelled = False

# Fonction pour exécuter les commandes dans un thread séparé
def execute_commands_thread():
    thread = threading.Thread(target=execute_commands)
    thread.start()

# Fonction pour exécuter les commandes
def execute_commands():
    global current_process, current_command_index, commands_dict, is_cancelled
    is_cancelled = False
    # Récupération du chemin du fichier sélectionné
    filename = entry_file.get()

    # Vérification si le champ de fichier est vide
    if not filename:
        messagebox.showerror("Erreur", "Veuillez sélectionner un fichier contenant les commandes.")
        return

    # Récupération de l'adresse IP et de l'URL depuis les champs de saisie
    ip_address = entry_ip.get()
    url = entry_url.get()

    # Vérification si au moins une adresse IP ou une URL est fournie
    if not ip_address and not url:
        messagebox.showerror("Erreur", "Veuillez fournir au moins une adresse IP ou une URL.")
        return

    # Déclaration du dossier de logs à la racine du script
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Déclaration des sous-dossiers pour les résultats de l'adresse IP et de l'URL
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ip_log_dir = os.path.join(log_dir, 'ip_results', timestamp)
    url_log_dir = os.path.join(log_dir, 'url_results', timestamp)

    if not os.path.exists(ip_log_dir):
        os.makedirs(ip_log_dir)
    if not os.path.exists(url_log_dir):
        os.makedirs(url_log_dir)

    # Lecture du fichier et constitution du dictionnaire de commandes
    commands_dict = {}
    with open(filename, "r") as file:
        comment = ""
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                comment = line[1:].strip()
            elif line:
                commands_dict[comment] = line
                comment = ""

    current_command_index = 0
    total_commands = len(commands_dict)
    update_progress(0, total_commands)
    run_next_command(ip_address, url, ip_log_dir, url_log_dir)

# Fonction pour exécuter la prochaine commande
def run_next_command(ip_address, url, ip_log_dir, url_log_dir):
    global current_process, current_command_index, is_cancelled
    if is_cancelled or current_command_index >= len(commands_dict):
        if is_cancelled:
            messagebox.showinfo("Annulation", "L'exécution des commandes a été annulée.")
        else:
            messagebox.showinfo("Exécution Terminée", "Toutes les commandes ont été exécutées avec succès.")
        processes.clear()
        update_progress(len(commands_dict), len(commands_dict))
        update_current_command("")
        return

    comment, command = list(commands_dict.items())[current_command_index]
    update_current_command(command)

    def run_command(command):
        global current_process
        current_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        processes.append(current_process)
        output, error = current_process.communicate()
        return output.decode().strip(), error.decode().strip()

    if ip_address:
        command_ip = command.replace("IP_ADDRESS", ip_address)
        safe_command_name_ip = command_ip.replace(" ", "_").replace("/", "_").replace("\\", "_")
        result_file_path_ip = os.path.join(ip_log_dir, f"{safe_command_name_ip}_results.txt")
        output_ip, error_ip = run_command(command_ip)
        with open(result_file_path_ip, "w") as result_file:
            result_file.write("Sortie de la commande:\n")
            result_file.write(output_ip + "\n")
            if error_ip:
                result_file.write("Erreurs rencontrées:\n")
                result_file.write(error_ip + "\n")

    if url:
        command_url = command.replace("URL", url)
        safe_command_name_url = command_url.replace(" ", "_").replace("/", "_").replace("\\", "_")
        result_file_path_url = os.path.join(url_log_dir, f"{safe_command_name_url}_results.txt")
        output_url, error_url = run_command(command_url)
        with open(result_file_path_url, "w") as result_file:
            result_file.write("Sortie de la commande:\n")
            result_file.write(output_url + "\n")
            if error_url:
                result_file.write("Erreurs rencontrées:\n")
                result_file.write(error_url + "\n")

    current_command_index += 1
    update_progress(current_command_index, len(commands_dict))

    # Call next command if not cancelled
    if not is_cancelled:
        root.after(100, run_next_command, ip_address, url, ip_log_dir, url_log_dir)

# Fonction pour mettre à jour l'état d'avancement
def update_progress(executed_commands, total_commands):
    progress_label.config(text=f"Exécution des commandes : {executed_commands}/{total_commands} terminées")
    root.update_idletasks()

# Fonction pour mettre à jour la commande en cours
def update_current_command(command):
    current_command_label.config(text=f"Commande en cours : {command}")
    root.update_idletasks()

# Fonction pour annuler l'exécution des commandes
def cancel_execution():
    global is_cancelled, current_process
    is_cancelled = True
    if current_process:
        current_process.terminate()
        processes.remove(current_process)
        current_process = None
        progress_label.config(text="Exécution annulée par l'utilisateur.")

# Fonction pour passer à la commande suivante
def skip_command():
    global current_process
    if current_process:
        current_process.terminate()
        processes.remove(current_process)
        current_process = None
        progress_label.config(text="Passage à la commande suivante.")
        run_next_command(entry_ip.get(), entry_url.get(), 
                         os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/ip_results', datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")), 
                         os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/url_results', datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

# Création de la fenêtre principale
root = Tk()
root.title("Exécution de commandes")

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
button_browse = Button(root, text="Choose files", command=select_file)
button_browse.grid(row=0, column=3, padx=10, pady=10)

# Création du champ de saisie pour l'adresse IP
entry_ip = Entry(root, width=20)
entry_ip.grid(row=1, column=1, padx=10, pady=5)
label_ip = Label(root, text="IP Address :")
label_ip.grid(row=1, column=0, padx=10, pady=5)

# Création du champ de saisie pour l'URL
entry_url = Entry(root, width=50)
entry_url.grid(row=2, column=1, columnspan=3, padx=10, pady=5)
label_url = Label(root, text="URL :")
label_url.grid(row=2, column=0, padx=10, pady=5)

# Création du bouton d'exécution des commandes
button_execute = Button(root, text="Execute", command=execute_commands_thread)
button_execute.grid(row=3, column=0, columnspan=1, padx=10, pady=10)

# Création du bouton d'annulation des commandes
button_cancel = Button(root, text="Cancel", command=cancel_execution)
button_cancel.grid(row=3, column=1, padx=10, pady=10)

# Création du bouton pour passer à la commande suivante
button_skip = Button(root, text="Pass", command=skip_command)
button_skip.grid(row=3, column=2, padx=10, pady=10)

# Création du label pour afficher l'état d'avancement
progress_label = Label(root, text="")
progress_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Création du label pour afficher la commande en cours
current_command_label = Label(root, text="")
current_command_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Animation visuelle pour les boutons
def on_button_click(event):
    event.widget.config(relief=SUNKEN)
    root.after(100, lambda: event.widget.config(relief=RAISED))

# Attachement de l'animation aux boutons
button_execute.bind("<Button-1>", on_button_click)
button_cancel.bind("<Button-1>", on_button_click)
button_skip.bind("<Button-1>", on_button_click)

# Lancement de la boucle principale de l'interface graphique
root.mainloop()
