import csv
import os
import pyqrcode

# Membuka File CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    
    # Lewati baris tajuk
    headers = next(reader)
    
    # Ulangi setiap baris dalam file CSV
    for row in reader:
        name = row[0]
        url = row[1]
        # Dapatkan nama file CSV
        csv_filename = row[2]
        folder = csv_filename.split(".")[0]

        # Buat folder untuk menyimpan gambar kode QR
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Hasilkan data kode QR
        qr = pyqrcode.create(url)
        
        # Simpan kode QR sebagai gambar PNG
        filename = f"{folder}/{name}.png"
        qr.png(filename, scale=8)
