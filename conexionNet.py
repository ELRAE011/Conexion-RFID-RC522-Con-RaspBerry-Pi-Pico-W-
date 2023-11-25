from mfrc522 import MFRC522
import machine
import usocket as socket
import network
import time

# Configuración del lector RFID
lector = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

try:
    lector.init()
    print("Lector RFID inicializado correctamente.")
except Exception as e:
    print("Error al inicializar el lector RFID:", e)
    machine.reset()

ssid = "EL NOMBRE DE TU ROUTER"#CONEXION SSID
password = "CONTRASEÑA DE TU ROUTER"#CONTRASEÑA

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

print("Conexión WiFi establecida.")

# Configuración del servidor de socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(1)

print("Esperando conexión desde Java...")

# Función para leer la tarjeta RFID
def read_rfid():
    lector.init()
    (stat, tag_type) = lector.request(lector.REQIDL)
    if stat == lector.OK:
        (stat, uid) = lector.SelectTagSN()
        if stat == lector.OK:
            identificador = int.from_bytes(bytes(uid), "little", False)
            print("Tarjeta detectada! UID: {}".format(identificador))
            return str(identificador)
    return None

while True:
    conn, addr = server.accept()
    print("Conexión establecida desde:", addr)

    try:
        while True:
            uid = read_rfid()
            if uid:
                conn.sendall(uid.encode()+ b'\n')
                time.sleep(1)
    except OSError:
        conn.close()
        print("Conexión cerrada.")
        
