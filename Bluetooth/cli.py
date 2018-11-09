import bluetooth

bd_addr = "4C:BB:58:09:BC:89"

port = 1

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
