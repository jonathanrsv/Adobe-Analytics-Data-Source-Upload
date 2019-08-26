import ftplib
import os
import io

accounts = {
    "account_name": {
        "server" : 'ftp.omniture.com',
        "username" : '',
        "password" : ''
    }
}

r_upload = input("----> Deseja Realmente realizar o upload? (s/n) :")

if(r_upload == "s"):

    r_upload_account = input("----> Para qual conta? :")
    account = accounts[r_upload_account]
    print("A conta selecionada foi:", account["username"])
    r_upload_continuar = input("----> Deseja continuar? (s/n) :")

    if(r_upload_continuar == "s"): 
        ftp_connection = ftplib.FTP(account['server'], account['username'], account['password'])
        ftp_connection.cwd("/")

        for root, dirs, files in os.walk('files_to_upload'):

            for fname in files:
                full_fname = os.path.join(root, fname)

                if(".txt" in full_fname):
                    print("Enviando o arquivo: ", fname)
                    ftp_connection.storbinary('STOR ' + fname, open(full_fname, 'rb'))
                    bio = io.BytesIO(b'')
                    ftp_connection.storbinary('STOR ' + fname.split(".")[0] + '.fin', bio)

    
        print("Done") 