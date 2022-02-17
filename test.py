import socket
import sys
import re
import time
import os
from listaDiretorio import *


class listas(ListasDirecty, ):
    def ListaPortas(self):
        self.portas = [21, 80, 79, 8080, 443, 23]

        for porta in self.portas: 
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.1)
            codigo = cliente.connect_ex(('www.bancocn.com', porta))
            if codigo == 0:
                print(porta, "OPEN")
            else:
                print(porta, "CLOSE")
