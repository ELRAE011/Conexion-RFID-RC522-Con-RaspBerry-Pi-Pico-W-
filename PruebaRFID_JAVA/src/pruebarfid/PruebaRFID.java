package pruebarfid;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

//@author ELRAE011

public class PruebaRFID {


    public static void main(String[] args) {
         try {
             String serverIP = "IP de tu RaspBerry Pi Pico W";//<= Importante
            int serverPort = 8080;
            
            Socket socket = new Socket(serverIP,serverPort);
            
            System.out.println("Conectado al servidor en la dirección IP: " + serverIP + " en el puerto: " + serverPort);

            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            System.out.println("Esperando datos del RFID...");

            while (true) {
                String uid = reader.readLine();
                System.out.println("Tarjeta detectada! UID: " + uid);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
