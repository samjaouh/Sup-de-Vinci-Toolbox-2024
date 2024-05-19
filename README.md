# Toolbox de Commandes de Sécurité

## À propos

Cette toolbox regroupe une série de commandes utiles pour la reconnaissance, les tests de sécurité, et l'exploitation des vulnérabilités. Elle est conçue pour aider les professionnels de la sécurité informatique dans leurs évaluations de la sécurité des systèmes et des réseaux.

## Table des matières

- 🔍 [À propos](#à-propos)
- 📦 [Prérequis](#prérequis)
- 🚀 [Installation](#installation)
- 🛠️ [Utilisation](#utilisation)
- 🏗️ [Construit avec](#construit-avec)
- 📚 [Documentation](#documentation)
- 🏷️ [Gestion des versions](#gestion-des-versions)
- 📝 [Licence](#licence)

## Prérequis

- **Linux 🐧 (La distribution Kali est recommandée afin de pouvoir disposer d'outils préinstallés)**
- **Outils mentionnés dans le fichier de commandes.**
- **Python 3.7+ 🐍 : Langage de programmation dans lequel le document a été programmé.**
- **pip : Gestionnaire de paquets pour Python.**
- **Git 🐙 : Logiciel de gestion de versions.**

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/samjaouh/Sup-de-Vinci-Toolbox-2024
    cd Sup-de-Vinci-Toolbox-2024
    ```

2. Installez les dépendances nécessaires :
    ```bash
    sudo apt-get install -y nslookup dnsutils host whois wafw00f whatweb dnsrecon fping traceroute testssl sslscan sslyze nmap spiderfoot nikto httrack curl wapiti theHarvester gobuster sublist3r dirb wpscan snmpcheck enum4linux nbtscan smbmap sqlmap hydra medusa ncrack crackmapexec
    ```

3. Pour les outils spécifiques (PwnXSS, Beroot), suivez les instructions dans leur documentation respective.

## Utilisation

Pour utiliser la toolbox, suivez ces étapes :

## Lancer l'outil

```bash
python3 process.py
```
Une boite de dialogue apparaitra une fois la commande envoyée. Cette boite de dialogue contient :

- Un champ permettant de mettre un document contenant des lignes de commandes (il est possible d'utiliser le fichier lignes de commande.txt disponible sur ce repo.)
- l'adresse IP a entrer
- L'URL a entrer

Il est possible d'entrer soit une adresse IP, soit une URL, soit les deux.
Les rapports générés seront stockés dans des dossiers crées à la racine d'ou le document process.py sera situé.
Un dossier pour les rapports des adresse IP et un autre dossier avec les rapports de l'URL seront crées.
