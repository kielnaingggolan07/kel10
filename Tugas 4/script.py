log_file = open("smtplib_debug2.log", 'r')

# Mencetak pesan EHLO
for line in log_file:
    if 'send: ' in line and 'ehlo' in line:
        print(line.strip())
        break

# Mencetak pesan bahwa server mendukung TLS
log_file.seek(0)
for line in log_file:
    if 'reply: b\'250-STARTTLS' in line:
        print(line.strip())
        break

# Mencetak pesan bahwa server siap mengirim email
log_file.seek(0)
for line in log_file:
    if 'reply: retcode (220); Msg: b\'2.0.0 SMTP server ready'in line:
        print(line.strip())
        break

# Mencetak pesan yang menunjukkan username yang sudah di-hash
log_file.seek(0)
for line in log_file:
    if 'AUTH LOGIN' in line:
        print(line.strip())
        break

# Mencetak pesan balasan server dari sebuah hello message dari client
log_file.seek(0)
for line in log_file:
    if 'reply: b\'250-' in line and 'Hello' in line:
        print(line.strip())
        break

# Mencetak pesan bahwa koneksi telah ditutup
log_file.seek(0)
for line in log_file:
    if 'reply: b\'221' in line:
        print(line.strip())
        break

log_file.close()
