# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""


base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "PGP" + os.sep + "libs" + os.sep
cur_path_bin = base_path + "modules" + os.sep + "PGP" + os.sep + "bin" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)
if cur_path_bin not in sys.path:
    sys.path.append(cur_path_bin)

import gnupg

module = GetParams("module")

if module == "decrypt":
    key = GetParams("key")
    path_file_encrypt = GetParams("path_file_encrypt")
    path_file_public_key = GetParams("path_file_public_key")
    path_file_private_key = GetParams("path_file_private_key")
    path_file = GetParams("path_file")
    try:
        gpg = gnupg.GPG(gnupghome=cur_path_bin)
        if path_file_public_key:
            key_data = open(path_file_public_key).read()
            import_result = gpg.import_keys(key_data)
        if path_file_private_key:
            key_data = open(path_file_private_key).read()
            import_result = gpg.import_keys(key_data)
        with open(path_file_encrypt, 'rb') as f:
            status = gpg.decrypt_file(f, passphrase=key, output=path_file)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
