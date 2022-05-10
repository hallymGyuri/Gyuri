from bluetooth import *
import rctest
r=rctest.Rc()
r.motor_init()
def receiveMsg():
    global r
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    # RFCOMM 포트를 통해 데이터 통신을 하기 위한 준비    
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(('',PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    # 블루투스 서비스를 Advertise
    advertise_service( server_sock, "BtChat",
            service_id = uuid,
            service_classes = [ uuid, SERIAL_PORT_CLASS ],
            profiles = [ SERIAL_PORT_PROFILE ] )
    
    print("Waiting for connection : channel %d" % port)
    # 클라이언트가 연결될 때까지 대기
    while True:
        client_sock, client_info = server_sock.accept()
        print('accepted')
        while True:          
            print("Accepted connection from ", client_info)
            try:
                # 들어온 데이터를 역순으로 뒤집어 전달
                data = client_sock.recv(1024)
                if len(data) == 0: 
                    break
                print("received [%s]" % data)
                msg=data.decode('utf-8')
                print(msg)
                if msg=='f':
                    r.forward_(100)
                elif msg=='b':
                    r.backward_(100)
                elif msg=='s':
                    r.stop_()
                elif msg=='l':
                    r.left_(100)
                elif msg=='r':
                    r.right_(100)
                elif msg=='o':
                    print('turn on laser')
                    r.turn_on()
                elif msg=='x':
                    print('turn off laser')
                    r.turn_off()
                #print("send [%s]" % data[::-1])
                #client_sock.send(data[::-1])
            except Exception as e:
                print("disconnected")
                client_sock.close()
                #server_sock.close()
                print("all done")
                break


receiveMsg()

