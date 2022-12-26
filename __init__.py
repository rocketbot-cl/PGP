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
import sys
import os

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "PGP" + os.sep + "libs" + os.sep
cur_path_bin = base_path + "modules" + os.sep + "PGP" + os.sep + "bin" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)
if cur_path_bin not in sys.path:
    sys.path.append(cur_path_bin)

import gnupg

module = GetParams("module")

if module == "create_key":
    recipients = GetParams("recipients")
    passphrase_ = GetParams("passphrase")
    path_bin = GetParams("path_bin")
    path_folder = GetParams("path_folder")
    
    try:
        if not path_bin:
            path_bin = cur_path_bin + os.sep + "gpg.exe"
        
        if not isinstance(eval(recipients), list):
            raise Exception("Recipients must be a list...")
        
        gpg = gnupg.GPG(gpgbinary=path_bin)
        
        path_folder = path_folder.replace("/", os.sep)
        
        input_data = gpg.gen_key_input(
            name_email=recipients,
            passphrase=passphrase_)
        key = gpg.gen_key(input_data)

        ascii_armored_public_keys = gpg.export_keys(key.__str__(), passphrase=passphrase_)

        ascii_armored_private_keys = gpg.export_keys(key.__str__(), secret=True, passphrase=passphrase_)

        with open(path_folder + os.sep + 'mykeyfile-pub.asc', 'w') as f:
            f.write(ascii_armored_public_keys)
        with open(path_folder + os.sep + 'mykeyfile-sec.asc', 'w') as f:    
            f.write(ascii_armored_private_keys)
    
    except Exception as e:
        SetVar(res, False)        
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "encrypt":
    path_bin = GetParams("path_bin")
    path_file = GetParams("path_file")
    recipients = GetParams("recipients")
    path_file_public_key = GetParams("path_file_public_key")    
    path_folder_encrypt = GetParams("path_folder_encrypt")
    res = GetParams("res")    
    try:
        if not path_bin:
            path_bin = cur_path_bin + os.sep + "gpg.exe"
        
        if not recipients[0] == '[':
            raise Exception("Recipients must be a list...")
        
        gpg = gnupg.GPG(gpgbinary=path_bin)
        
        if path_file_public_key:
            key_data = open(path_file_public_key).read()
            import_result = gpg.import_keys(key_data)
        
        with open(path_file, 'rb') as f:
            path_file_encrypt = path_folder_encrypt.replace('/', os.sep) + os.sep + os.path.basename(path_file) + '.gpg'
            status = gpg.encrypt_file(f, recipients=recipients, output=path_file_encrypt, always_trust=True)
            
        SetVar(res, status.status)
    except Exception as e:
        SetVar(res, False)  
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
    
if module == "decrypt":
    path_bin = GetParams("path_bin")
    passphrase_ = GetParams("passphrase")
    path_file_encrypt = GetParams("path_file_encrypt")
    path_file_private_key = GetParams("path_file_private_key")
    path_folder = GetParams("path_folder")
    res = GetParams("res")
    try:
        if not path_bin:
            path_bin = cur_path_bin + os.sep + "gpg.exe"
        
        gpg = gnupg.GPG(gpgbinary=path_bin)
        
        if path_file_private_key:
            key_data = open(path_file_private_key).read()
            import_result = gpg.import_keys(key_data)
        
        with open(path_file_encrypt, 'rb') as f:
            path_file_encrypt = path_folder.replace('/', os.sep) + os.sep + os.path.basename(path_file_encrypt).replace('.gpg', '')
            status = gpg.decrypt_file(f, passphrase=passphrase_ , output=path_file_encrypt, always_trust=True)

        SetVar(res, status.status)
    except Exception as e:
        SetVar(res, False)        
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e