import smtplib
import logging
import sys

# Konfigurasi log untuk menyimpan hasil debug smtplib ke file
logging.basicConfig(filename='smtplib_debug2.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Menyimpan referensi stderr asli
original_stderr = sys.stderr

# Membuka file log untuk menulis debug output
log_file = open("smtplib_debug2.log", 'w')
# Mengarahkan stderr ke file log
sys.stderr = log_file

# Konfigurasi SMTP server Office 365
smtp_server = 'smtp.office365.com'
smtp_port = 587

# Konfigurasi email pengirim
sender_email = 'hesekiel07@outlook.com'
sender_password = 'kielmaster07'

# Konfigurasi email penerima
receiver_email = 'golanhesekiel02@gmail.com'

try:
    # Buat koneksi ke SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Aktifkan debug mode
        server.set_debuglevel(1)

        # Mulai koneksi ke SMTP server
        server.starttls()

        # Login ke akun email
        server.login(sender_email, sender_password)

        # Kirim email
        message = 'Subject: Demo Progjar Tugas 4.'
        server.sendmail(sender_email, receiver_email, message)

except smtplib.SMTPException as e:
    logging.error(f'Error: {e}')

finally:
    # Menutup file log
    log_file.close()

    # Mengembalikan stderr ke keadaan semula
    sys.stderr = original_stderr

# Menutup logging dan memastikan log ditulis ke file
logging.shutdown()
