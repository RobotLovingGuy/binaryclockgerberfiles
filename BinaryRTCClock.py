import machine
import utime
from machine import Timer

secs = 0

run = 1

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

secs = 0

a = 0
a1 = 0
a2 = 0
c = 0
c1 = c
d = 0
d1 = d

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

def tick(timer):
    global secs
    secs = secs + 1
    if secs == 60:
        secs = 0
    print("count", secs)

seconds = Timer()
seconds.init(mode=Timer.PERIODIC, period=1000, callback=tick)

while run == 1:
    a = 0
    while a < 24:
        while c < 6:
            while d < 10:
                b1 = button1.value()
                if b1 == 1:
                    a = a + 1
                if a == 24:
                    a = 0
                a1 = a
                a2 = 0
                while a1 > 9:
                    a1 = a1 - 10
                    a2 = a2 + 1
                if a2 == 2:
                    a2 = 0
                    ba.value(1)
                else:
                    ba .value(0)
                if a2 == 1:
                    aa.value(1)            
                    a2 = 0
                else:
                    aa.value(0)
                if a1 > 7:
                    a1 = a1 - 8
                    db.value(1)
                else:
                    db.value(0)
                if a1 > 3:
                    a1 = a1 - 4
                    cb.value(1)
                else:
                    cb.value(0)
                if a1 > 1:
                    a1 = a1 - 2
                    bb.value(1)
                else:
                    bb.value(0)
                if a1 == 1:
                    a1 = a1 - 1
                    ab.value(1)
                else:
                    ab.value(0)
                if a1 != 0:
                    onboard_led.value(1)
                if a2 != 0:
                    onboard_led.value(1)

                c1 = c
                if c1 > 3:
                    c1 = c1 - 4
                    ac.value(1)
                else:
                    ac.value(0)
                if c1 > 1:
                    c1 = c1 - 2
                    bc.value(1)
                else:
                    bc.value(0)
                if c1 == 1:
                    c1 = 0
                    cc.value(1)
                else:
                    cc.value(0)
                if c1 != 0:
                    onboard_led.value(1)

                d1 = d
                
                if d1 > 7:
                    d1 = d1 - 8
                    ad.value(1)
                else:
                    ad.value(0)
                if d1 > 3:
                    d1 = d1 - 4
                    bd.value(1)
                else:
                    bd.value(0)
                if d1 > 1:
                    d1 = d1 - 2
                    cd.value(1)
                else:
                    cd.value(0)
                if d1 == 1:
                    d1 = 0
                    dd.value(1)
                else:
                    dd.value(0)
                if d1 != 0:
                    onboard_led.value(1)
                
                
                
                b2 = button2.value()
                if b2 == 1:
                    d = d + 1
                print(aa.value(), ba.value(), ab.value(), bb.value(), cb.value(), db.value(), ac.value(), bc.value(), cc.value(), ad.value(), bd.value(), cd.value(), dd.value())
                print(a1, a2, c1, d1, " ", b1, b2)
                e = 0
                utime.sleep(.9)
                while e < 70:
                    e = e + 1
                    utime.sleep(.1)
                    b1 = button1.value()
                    b2 = button2.value()
                    if b1 == 1:
                        e = 70
                    if b2 == 1:
                        e = 70
                    if secs == 0:
                        d = d + 1
                        e = 70
            d = 0
            c = c + 1
        c = 0
        a = a + 1
        