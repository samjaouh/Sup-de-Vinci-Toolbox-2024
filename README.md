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

- **Systèmes d'exploitation supportés :**
  - Linux (La distribution Kali est recommandée afin de pouvoir disposer d'outils préinstallés)
  - Windows

- **Outils mentionnés dans le fichier de commandes.**
- **Python 3.7+ 🐍 : Langage de programmation dans lequel le document a été programmé.**
- **pip : Gestionnaire de paquets pour Python.**
- **Git 🐙 : Logiciel de gestion de versions.**

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votreutilisateur/votredepot.git
    cd votredepot
    ```

2. Installez les dépendances nécessaires :
    ```bash
    sudo apt-get install -y nslookup dnsutils host whois wafw00f whatweb dnsrecon fping traceroute testssl sslscan sslyze nmap spiderfoot nikto httrack curl wapiti theHarvester gobuster sublist3r dirb wpscan snmpcheck enum4linux nbtscan smbmap sqlmap hydra medusa ncrack crackmapexec
    ```

3. Pour les outils spécifiques (PwnXSS, Beroot), suivez les instructions dans leur documentation respective.

## Utilisation

### Phase de Reconnaissance

#### Passive

- **nslookup**
  ```bash
  nslookup URL
  nslookup -type=A URL
  nslookup -type=MX URL
  nslookup -type=TXT URL
