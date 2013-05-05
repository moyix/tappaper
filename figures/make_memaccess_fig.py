#!/usr/bin/env python
# vim: set fileencoding=utf8 :

from matplotlib.pyplot import *
from numpy import *

XMAX=30.0
YMAX=25.0

xlim(xmin=0,xmax=XMAX)
ylim(ymin=0,ymax=YMAX)
xticks([])
yticks([])
xlabel(u'Time →')
ylabel(u'Memory Address →')

# memcpy
text(11.3,.5,"memcpy")
memcpy_x1 = arange(5,9)
memcpy_y1 = arange(4,8)
circles = plot(memcpy_x1,memcpy_y1,'bo')
memcpy_x2 = arange(9,11)
memcpy_y2 = arange(8,10)
triangles = plot(memcpy_x2,memcpy_y2,'r^')
for x,y,c,k in zip(concatenate([memcpy_x1,memcpy_x2])-.25,
                   concatenate([memcpy_y1,memcpy_y2])+1,
                   "google", "bbbbrr"):
    text(x,y,c,color=k)

# dmesg
text(27,13,"dmesg")
dmesg_x1 = arange(17,21)
dmesg_y1 = arange(15,19)
plot(dmesg_x1,dmesg_y1,'bo')
text(22,18.5,"[...]")
dmesg_x2 = arange(25,29)
dmesg_y2 = arange(19,23)
plot(dmesg_x2,dmesg_y2,'r^')
for x,y,c,k in zip(concatenate([dmesg_x1,dmesg_x2])-.25,
                   concatenate([dmesg_y1,dmesg_y2])+1,
                   "doneInit", "bbbbrrrr"):
    text(x,y,c,color=k)

# memmove
text(10.5,13,"memmove")
memmove_x = arange(4,12)
memmove_y = concatenate([arange(19,23),arange(15,19)])
plot(memmove_x,memmove_y,'bo')
for x,y,c,k in zip(memmove_x-.25,
                   memmove_y+1,
                   "le.cgoog", "bbbbbbbb"):
    text(x,y,c,color=k)

# Serial port
text(27.5,.5,"serial")
serial_x = arange(18,28)
serial_y = repeat([6], len(serial_x))
plot(serial_x,serial_y, 'bo')
for x,y,c,k in zip(serial_x-.25, serial_y+1,
                   "Uncompress", "bbbbbbbbbb"):
    text(x,y,c,color=k)

# Dividing lines
plot([0,XMAX],[YMAX/2,YMAX/2],'k--')
plot([XMAX/2,XMAX/2],[0,YMAX],'k--')

legend([circles[0],triangles[0]],['Tap A', 'Tap B'],
    bbox_to_anchor=(.5,1.1), loc=9, ncol=2, frameon=False)

savefig('memaccess.pdf')
