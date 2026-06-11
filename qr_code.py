import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import tkinter.simpledialog as simpledialog

# Tkinter penceresini gizle
root = tk.Tk()
root.withdraw()

# 1️⃣ PDF linkini kullanıcıdan al
data = simpledialog.askstring("PDF Linki", "PDF dosyasının paylaşılabilir linkini girin:")
if not data:
    print("PDF linki girilmedi. Program sonlandırıldı.")
    exit()

# 2️⃣ QR kod ayarları
qr = qrcode.QRCode(
    version=4,  # QR boyutu (veri uzunluğuna göre arttır)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Logo için yüksek hata düzeltme
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# 3️⃣ Renkli QR oluştur (siyah-gri arası)
fill_color = (50, 50, 50)
back_color = "white"
img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

# 4️⃣ Logo ekleme (opsiyonel)
logo_path = filedialog.askopenfilename(title="Logo dosyasını seçin", filetypes=[("PNG Files","*.png"),("All Files","*.*")])
if logo_path:
    logo = Image.open(logo_path)

    # Logoyu QR boyutuna göre ölçeklendir
    basewidth = 180
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.LANCZOS)

    # Logoyu QR’ın ortasına yerleştir
    pos = ((img.size[0] - logo.size[0]) // 2,
           (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos, mask=logo if logo.mode=="RGBA" else None)

# 5️⃣ Kaydetme konumunu kullanıcı seçsin
save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files","*.png")], title="QR Kodunu Kaydet")
if save_path:
    img.save(save_path)
    print(f"QR kodu oluşturuldu ve kaydedildi: {save_path}")
else:
    print("QR kodu kaydedilmedi.")
