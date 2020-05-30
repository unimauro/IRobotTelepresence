######
#
# Carlos Cardenas cardenas@cardenas.pe
# 2008
# little lines in GPL 3.0
#
#######
import os
import create
import time
import sys
import subprocess

def synth(txt):
    subprocess.call(["espeak","-w","test.wav","-p","60","-s","140","-v","es",txt],stdout=subprocess.PIPE)
    subprocess.call(["aplay","test.wav"],stdout=subprocess.PIPE)

if __name__=="__main__":
#    r=create.Create('/dev/rfcomm1')
    synth('Robot Activo')
#    r.demo(4)
    synth('Demo de Sonido')
    time.sleep(10)
#    r.demo()
    synth('Cerrando Demo de Sonido')
#    r.close()
    synth('Cerrando Conexion al Robot')
	
