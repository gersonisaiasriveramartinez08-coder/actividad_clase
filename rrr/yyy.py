import qrcode 


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"

qr = qrcode.QRcode(
    version=1,
    box_size=25,
    border=5
)

qr.add_data(url)
qr.make(fit=True)


imagen = qr.make_image()

imagen.save("el_verdadero_qr.png")