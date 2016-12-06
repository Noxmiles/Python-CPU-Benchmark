#!/usr/bin/python3
#Small Python CPU Benchmark for Linux CLI by Alexander Ochs - noxmiles.de

import time
import platform

print('Einfacher Benchmark zum Testen der CPU Geschwindigkeit')

if "Linux" == platform.system():
  print('Prozessor:')
  with open('/proc/cpuinfo') as f:
    for line in f:
        # Ignore the blank line separating the information between
        # details about two processing units
        if line.strip():
            if line.rstrip('\n').startswith('model name'):
                model_name = line.rstrip('\n').split(':')[1]
                print(model_name)
                break
else:
  print('Prozessor Name kann nur bei Linux automatisch angezeigt werden.')

laeufe = input( '\nWie viele Wiederholungen pro Versuch? [def=1000] ')
if laeufe == '': laeufe = 1000
laeufe = int(laeufe)
wiederholungen = input( 'Wie viele Durchlaeufe? [def=10] ')
if wiederholungen == '': wiederholungen = 10
wiederholungen = int(wiederholungen)

schnitt = 0

for a in range(0,wiederholungen):

  start = time.time()

  for i in range(0,laeufe):
    for x in range(1,1000):
      3.141592 * 2**x
    for x in range(1,10000):
      float(x) / 3.141592
    for x in range(1,10000):
      float(3.141592) / x

  ende = time.time()
  dauer = (ende - start)
  dauer = round(dauer, 3)
  schnitt += dauer
  print('Zeit: ' + str(dauer) + 's')

schnitt = round(schnitt / wiederholungen, 3)
print('Mittel: ' + str(schnitt) + 's')

