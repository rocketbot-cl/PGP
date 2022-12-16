



# PGP
  
Encrypt and decrypt data with PGP.  
  
![banner](imgs/Banner_PGP.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Create Keys
  
Create Public and Private Key
|Parameters|Description|example|
| --- | --- | --- |
|Recipient||[example@dom.com, example@dom.com]|
|Passphrase||12345|
|Path to GPG binary (OPTIONAL) ||path/to/bin/gpg.exe|
|Keys folder path ||path/to/save|

### Encrypy file
  
Encrypt file using public key
|Parameters|Description|example|
| --- | --- | --- |
|Path to GPG binary (OPTIONAL) ||path/to/bin/gpg.exe|
|Path to file ||file.*|
|Recipient||[example@dom.com, example@dom.com]|
|Path to public Key ||file.acs|
|Encrypted file folder path ||path/to/save|
|Variable||variable|

### Decrypy file
  
Decrypy file using private key
|Parameters|Description|example|
| --- | --- | --- |
|Path to GPG binary (OPTIONAL) ||path/to/bin/gpg.exe|
|Passphrase||12345|
|Path to encrypt file ||file.gpg|
|Path to private Key ||file.acs|
|Decrypted file folder path ||path/to/save|
|Variable||variable|
