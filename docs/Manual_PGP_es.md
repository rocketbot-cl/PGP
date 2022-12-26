



# PGP
  
Encriptar y desencriptar datos con PGP.  
  
![banner](imgs/Banner_PGP.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Crear Keys
  
Crear Key Publica y Privada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Destinatario||['example@dom.com', 'example@dom.com']|
|Frase secreta||12345|
|Ruta a GPG binario (OPCIONAL) ||path/to/bin/gpg.exe|
|Ruta de la carpeta de keys ||path/to/save|

### Encriptar archivo
  
Encriptar archivo usando la key publica
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta a GPG binario (OPCIONAL) ||path/to/bin/gpg.exe|
|Ruta a archivo ||archivo.*|
|Destinatario||['example@dom.com', 'example@dom.com']|
|Ruta a Key publica ||archivo.asc|
|Ruta de la carpeta de archivo encriptado ||path/to/save|
|Variable||variable|

### Desencriptar archivo
  
Desencriptar archivo usando la key privada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta a GPG binario (OPCIONAL) ||path/to/bin/gpg.exe|
|Frase secreta||12345|
|Ruta archivo encriptado ||archivo.gpg|
|Ruta a Key privada ||archivo.asc|
|Ruta de la carpeta de archivo desencriptado ||path/to/save|
|Variable||variable|
