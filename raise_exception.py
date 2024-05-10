class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("accident occured: ", self.msg)

try :
    raise Accident("Two car crashed")
except Accident as e:
    e.handle()

def process_file():
    try:
        f = open("c:\\code\\data.txt")
        x=1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()

process_file()



