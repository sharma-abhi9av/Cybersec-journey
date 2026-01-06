https://labs.hackthebox.com/achievement/machine/2142022/656
Nocturnal is a easy-difficulty Linux machine demonstrating an IDOR vulnerability in a PHP web app, allowing access to other users uploaded files. 
Credentials (amanda) are retrieved to log in to the admin panel, where the source code of application is accessed. 
A command injection vulnerability is identified, providing a reverse shell as the www-data user. 
Hashes for passwords were obtained from a SQLite database and cracked to obtain SSH access as the tobias user. 
Exploiting CVE-2023-46818 in the ISPConfig application grants remote command execution, leading to privilege escalation to the root user.
