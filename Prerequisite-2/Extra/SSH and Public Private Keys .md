### Create private/public key pair


```bash
$ mkdir .ssh
# Create directory for your ssh keys
$ cd .ssh
$ ssh-keygen
# Create public and private key pair
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mojtaba/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
....

$ cat id_rsa.pub
 # Obtain your public key
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDNZWFuQ/abHGmZwT0OciesslT6Quy2JAJeRQqfcj3cDZx587SXxGR02TglIZdRZwqduPKgrVI1493B7h6W5D/6Fj4kFPJ5PeAMm449qW91TCTr1SHh/TfOx26FAM1kzrdy/+EoV7GQqWpBWgu4/tlSBsK04HFECMHm/Dnka+24+nB+pQd+2/qn84K8hIrROjS2wBO8Vbd0T5fwjaBDSc2Jghy/y2q8Fe+eQWgGLGrTR2ZGm7n505wkRb6fOLD1vMIfQm70uddzny3bsEsXlFuTor+lUALmt+XErPGnQvr/wPnzxhIp+yse+/3URdPENHSvqW0Bjr6FpQ4s/kS8doothweaBJJgvV0B+U3+2T8usOaKWmYaxRcdR/IhI0+78cfXt/ZL7hy7Och0VFNRaxKdHwxxcgG8cw6S+e+WhotN3MCg9KlZ59XStaJ8e/c1Gx+OEMaoSlQNj0ClHgD/twfaNbX0/96YnCEdZGdBBkIgCHmD895zrKVMGGEdbTVD0Os= mojtaba@DESKTOP-NCT3S06
```


#### Working with generated keys

On Remote Host : 
```bash
$ sudo ssh-keygen -A
ssh-keygen: generating new host keys: RSA DSA ECDSA ED25519
$ sudo service ssh restart

$ cat  >> ~/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDNZWFuQ/abHGmZwT0OciesslT6Quy2JAJeRQqfcj3cDZx587SXxGR02TglIZdRZwqduPKgrVI1493B7h6W5D/6Fj4kFPJ5PeAMm449qW91TCTr1SHh/TfOx26FAM1kzrdy/+EoV7GQqWpBWgu4/tlSBsK04HFECMHm/Dnka+24+nB+pQd+2/qn84K8hIrROjS2wBO8Vbd0T5fwjaBDSc2Jghy/y2q8Fe+eQWgGLGrTR2ZGm7n505wkRb6fOLD1vMIfQm70uddzny3bsEsXlFuTor+lUALmt+XErPGnQvr/wPnzxhIp+yse+/3URdPENHSvqW0Bjr6FpQ4s/kS8doothweaBJJgvV0B+U3+2T8usOaKWmYaxRcdR/IhI0+78cfXt/ZL7hy7Och0VFNRaxKdHwxxcgG8cw6S+e+WhotN3MCg9KlZ59XStaJ8e/c1Gx+OEMaoSlQNj0ClHgD/twfaNbX0/96YnCEdZGdBBkIgCHmD895zrKVMGGEdbTVD0Os= mojtaba@DESKTOP-NCT3S06

Enter/ Ctrl+D


 # Add key to those with allowed access
$ chmod 640 authorized_keys
$ sudo service ssh restart

```



```bash
$ ssh -p 22 mojtaba@remote.host
# run any command 
```


### Synchronize files


```bash
$ rsync -av host.example.com:/usr/share/sounds/alsa/ wav-files
 # Mirror remote

 $ rsync -av host.example.com:/usr/share/sounds/alsa/ wav-files
 # Refresh
```

##### scp : copy files from/to remote servers

```bash
$ scp username@remote.host:/home/mojtaba/data/data.zip ~/data
```