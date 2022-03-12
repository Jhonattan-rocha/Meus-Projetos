import threading

# Exer1


class ExerUm(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        print(self.native_id, self.name, self.ident)


# executando
for i in range(5):
    Thread = ExerUm()
    Thread.start()
