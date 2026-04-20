import threading
import time
import random

NUM_FILOSOFOS = 5

garfos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]

garcom = threading.Semaphore(1)

def pensar(id):
    print(f"Filósofo {id} está pensando...")
    time.sleep(random.uniform(1, 3))

def comer(id):
    print(f"Filósofo {id} está COMENDO")
    time.sleep(random.uniform(1, 2))

def filosofo(id):
    pensar(id)
    
    esquerda = id
    direita = (id + 1) % NUM_FILOSOFOS
    
    with garcom:
        with garfos[esquerda]:
            with garfos[direita]:
                comer(id)
        
        print(f"Filósofo {id} devolveu os garfos e terminou sua refeição")

threads = []
for i in range(NUM_FILOSOFOS):
    t = threading.Thread(target=filosofo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Todos os filósofos comeram. Encerrando o programa.")