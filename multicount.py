# SPDX-License-Identifier: LGPL-3.0-or-later
# MultiCount by jlukanc1

import wasp
import icons
a = 0

class MultiCount():

    NAME = 'IncCount'
    ICON = icons.counter

    def __init__(self):
        pass

    def foreground(self):
        draw = wasp.watch.drawable
        wasp.system.request_event(wasp.EventMask.TOUCH)     #need to subscribe to event, look at foreground of testapp
        wasp.watch.display.fill(0x0000)
        draw.string("-1:Tap", 0, 212, width=240)
        draw.string("+1:Tap", 0, 6, width=240)
        draw.string("bin/oct/dec/hex", 0 , 170, width=240)
        self._draw()
        pass

    def touch(self, event):
        global a
        y = event[2]    #get touch y coord
        if y < 120:
            a += 1
            self._update()
        else:
           a -= 1
           self._update()
          
    def _draw(self):
        """Draw the display from scratch."""

    def _update(self):
        draw = wasp.watch.drawable
        global a
        c = bin(int(a))
        draw.string(c, 0, 50, width=240)
        draw.string(oct(a), 0, 75, width=240)
        draw.string(str(a), 0, 100, width=240)
        draw.string(hex(a), 0, 125, width=240)
        pass
