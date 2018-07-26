import threading
import time

def worker(message, loop):
    for _ in range(loop):
        print(message)
        print(time.ctime(time.time()))
        time.sleep(1)


t = threading.Thread(target=worker,args=("thread sendo executada", 4))
t.start()
while t.isAlive():
    print("Aguardando thread")
    time.sleep(5)

print("Thread morreu")
print("Finalizando programa")