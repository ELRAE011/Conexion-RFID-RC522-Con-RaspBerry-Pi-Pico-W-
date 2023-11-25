from mfrc522 import MFRC522
import time

# Configuración del lector RFID
lector = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
#Conexion con el Lector
try:
    lector.init()
    print("Lector RFID inicializado correctamente.")
except Exception as e:
    print("Error al inicializar el lector RFID:", e)
    machine.reset()


while True:
    lector.init()
    (stat, tag_type) = lector.request(lector.REQIDL)
    if stat == lector.OK:
        (stat, uid) = lector.SelectTagSN()
        if stat == lector.OK:
            identificador = int.from_bytes(bytes(uid),"little",False)
            print("UID: "+str(identificador))
time.sleep(1)  
