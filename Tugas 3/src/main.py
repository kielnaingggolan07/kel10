from ftplib import FTP
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class FtpClient:
    # TODO: Initialize FTP client object
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.ftp = FTP()

    # TODO: Connect to FTP server & login
    def connect(self):
        self.ftp.connect(host=self.host, port=self.port)
        self.ftp.login(user=self.user, passwd=self.password)


    # TODO: Disconnect from FTP server
    def disconnect(self):
        self.ftp.close()

    # Soal no 1
    # Nama dan versi FTP server
    def getNameAndVersion(self):
        # CONTOH OUTPUT getwelcome()
        # 220-FileZilla Server 1.7.0
        # 220 Please visit https://filezilla-project.org/
        welcome_msg = self.ftp.getwelcome()
        welcome_msg = welcome_msg.split('\n')[0].split('-')[1].split()
        server_name = ' '.join(welcome_msg[0:2])
        server_version = welcome_msg[-1]
        
        return ' '.join(welcome_msg)

    # Soal no 2
    # Sistem yang diemulasikan FTP server
    def getWelcomeMessage(self):
        welcome_msg = self.ftp.getwelcome()
        return welcome_msg
    
    # Soal no 3
    # Daftar file di FTP server
    def getListOfFiles(self):
        return self.ftp.nlst()
    
    # Soal no 4
    # Mengunggah file ke FTP server
    def uploadFile(self, filename):
        with open(filename, 'rb') as file:
            status = self.ftp.storbinary(f"STOR {filename}", file)
        return status

    # Soal no 5
    # Membuat direktori
    def createDirectory(self, dirname):
        status = self.ftp.mkd(dirname=dirname)
        return status

    # Soal no 6
    # Direktori saat ini di FTP server
    def getCurrentDirectory(self):
        working_directory = self.ftp.pwd()
        return working_directory
    
    # Soal no 7
    # Mengganti nama direktori
    def renameDirectory(self, oldname, newname):
        status = self.ftp.rename(fromname=oldname, toname=newname)
        return status

    # Soal no 8
    # Menghapus direktori
    def removeDirectory(self, dirname):
        status = self.ftp.rmd(dirname=dirname)
        return status
        

if __name__ == '__main__':
    # TODO: Read FTP server configuration from ftp.conf
    # with open(os.path.join(BASE_DIR, 'ftp.conf.example')) as config_file:
    with open(os.path.join(BASE_DIR, 'ftp.conf')) as config_file:
        config = dict(line.strip().split('=') for line in config_file)

    HOST = config.get("host")
    USER = config.get("user")
    PASS = config.get("pass")
    PORT = int(config.get("port", 8080))

    ftp = FtpClient(HOST, USER, PASS, PORT)
    ftp.connect()

    print(ftp.getNameAndVersion())
    print(ftp.getWelcomeMessage())
    print(ftp.getListOfFiles())
    print(ftp.uploadFile('samplefile.txt'))
    print(ftp.createDirectory('test'))
    print(ftp.getCurrentDirectory())
    print(ftp.renameDirectory('test', 'test2'))
    print(ftp.removeDirectory('test2'))
