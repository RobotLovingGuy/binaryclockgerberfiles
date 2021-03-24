import machine
import utime
from machine import Timer

aa = machine.Pin(17, machine.Pin.OUT)
ba = machine.Pin(16, machine.Pin.OUT)

ab = machine.Pin(26, machine.Pin.OUT)
bb = machine.Pin(22, machine.Pin.OUT)
cb = machine.Pin(20, machine.Pin.OUT)
db = machine.Pin(18, machine.Pin.OUT)

ac = machine.Pin(12, machine.Pin.OUT)
bc = machine.Pin(11, machine.Pin.OUT)
cc = machine.Pin(10, machine.Pin.OUT)

ad = machine.Pin(9, machine.Pin.OUT)
bd = machine.Pin(8, machine.Pin.OUT)
cd = machine.Pin(7, machine.Pin.OUT)
dd = machine.Pin(6, machine.Pin.OUT)

button1 = machine.Pin(0, machine.Pin.IN)
button2 = machine.Pin(1, machine.Pin.IN)

onboard_led = machine.Pin(25, machine.Pin.OUT)

onboard_led.value(0)

aa.value(0)
ba.value(0)

ab.value(0)
bb.value(0)
cb.value(0)
db.value(0)

ac.value(0)
bc.value(0)
cc.value(0)

ad.value(0)
bd.value(0)
cd.value(0)
dd.value(0)

utime.sleep(1)

onboard_led.value(1)

aa.value(1)
ba.value(1)

ab.value(1)
bb.value(1)
cb.value(1)
db.value(1)

ac.value(1)
bc.value(1)
cc.value(1)

ad.value(1)
bd.value(1)
cd.value(1)
dd.value(1)

utime.sleep(1)

onboard_led.value(0)

aa.value(0)
ba.value(0)

ab.value(0)
bb.value(0)
cb.value(0)
db.value(0)

ac.value(0)
bc.value(0)
cc.value(0)

ad.value(0)
bd.value(0)
cd.value(0)
dd.value(0)

utime.sleep(1)

aa.value(1)
ba.value(0)

ab.value(0)
bb.value(1)
cb.value(0)
db.value(0)

ac.value(0)
bc.value(1)
cc.value(0)

ad.value(0)
bd.value(1)
cd.value(0)
dd.value(0)

run = 1

b1 = 0
b2 = 0

 while run == 1:
    b1 = button1.value()
    b2 = button2.value()
    if b1 == 1:
        import BinaryRTCClock12hr
    if b2 == 1:
        import BinaryRTCClock24hr
    utime.sleep(.1)
    