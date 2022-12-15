



# PGP
  
Criptografar e descriptografar dados com PGP.  
  
![banner](imgs/Banner_PGP.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Criar Keys
  
Criar Key Pública e Privada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Destinatário||[example@dom.com, example@dom.com]|
|Frase secreta||12345|
|Caminho para o binário GPG (OPCIONAL) ||path/to/bin/gpg.exe|
|Caminho da pasta do keys ||path/to/save|

### Criptografar arquivo
  
Criptografar arquivo usando key pública
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o binário GPG (OPCIONAL) ||path/to/bin/gpg.exe|
|Caminho para o arquivo ||arquivo.*|
|Destinatário||[example@dom.com, example@dom.com]|
|Caminho para a Key pública ||arquivo.asc|
|Caminho da pasta do arquivo criptografado ||path/to/save|
|Variável||variável|

### Descriptografar arquivo
  
Descriptografar arquivo usando key privada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o binário GPG (OPCIONAL) ||path/to/bin/gpg.exe|
|Frase secreta||12345|
|Caminho do arquivo criptografado ||arquivo.gpg|
|Caminho para a Key privada ||arquivo.asc|
|Caminho da pasta de arquivo descriptografado ||path/to/save|
|Variável||variável|
