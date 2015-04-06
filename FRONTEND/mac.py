#
# macstyle.py - A minimalist implementation of the Mac Classic style for PyQt
# and Qt 2.
# Use with styletester.py
#
from PyQt4 import *
import time
FALSE=0
TRUE=1


class MacStyle(QWindowsStyle):

    def __init__(self):
        QWindowsStyle.__init__(self)
        self.setButtonDefaultIndicatorWidth(0)

    def polish(self, object):

        # Overloading doesn't work here, for Python cannot distinguish
        # between QApplication and QWidget - Python can only overload based
        # on the number of arguments.

        if isinstance(object, QApplication):
            self.polish_qapplication(object)
        elif isinstance(object, QWidget):
            self.polish_qwidget(object)
        else:
            QPlatinumStyle.polish(self, object)

    def unPolish(self, object):
        if isinstance(object, QApplication):
            self.unPolish_qapplication(object)
        elif isinstance(object, QWidget):
            self.unPolish_qwidget(object)
        else:
            QPlatinumStyle.unPolish(self, object)

    def polish_qapplication(self, app):
        # Set a font that's an approximation of Chicago: keep a ref to
        # the old font
        self.oldFont=app.font()
        app.setFont(QFont("chicago",
                            app.font().pointSize()-2, QFont.Bold),
                            TRUE)

        # keep a reference to the old color palette, otherwise
        # it cannot be restored
        self.oldPalette=app.palette()
        # create a new palette - black, white and 50% gray for text and buttons

        # color definitions
        white=QColor("white")
        lightgray=QColor(210,210,210)
        gray=QColor(190,190,190)
        darkgray=QColor(120,120,120)
        black=QColor("black")

        active=QColorGroup()
        #
        # Basic colors
        #
        active.setColor(QColorGroup.Background,
                        white) # general background color
        active.setColor(QColorGroup.Foreground,
                        black) # general foreground color
        active.setColor(QColorGroup.Base,
                        white) # lighter background for text widgets
        active.setColor(QColorGroup.Text,
                        black) # foreground to go with Base
        active.setColor(QColorGroup.Button,
                        white) # button background color
        active.setColor(QColorGroup.ButtonText,
                        black) # button text color
        #
        # Used for bevels and shadows
        #
        active.setColor(QColorGroup.Light,
                        lightgray ) # a bit lighter than Button
        active.setColor(QColorGroup.Midlight,
                        gray)
        active.setColor(QColorGroup.Dark,
                        darkgray) # depressed button state
        active.setColor(QColorGroup.Mid,
                        gray) # mid tone
        active.setColor(QColorGroup.Shadow,
                        black) # shadow tone
        #
        # Selections
        #
        active.setColor(QColorGroup.Highlight,
                        black)
        active.setColor(QColorGroup.HighlightedText,
                        white)
        #
        # Text color that shows well on Dark
        #
        active.setColor(QColorGroup.BrightText,
                        white)


        disabled=QColorGroup(active)

        disabled.setColor(QColorGroup.Base, gray)
        disabled.setColor(QColorGroup.Text, darkgray)

        inactive=QColorGroup(active)

        inactive.setColor(QColorGroup.Text, darkgray)
        self.newPalette=QPalette(active, disabled, inactive)

        app.setPalette(self.newPalette, TRUE)

    def unPolish_qapplication(self, app):
        # Restore the old palette
        app.setFont(self.oldFont,  TRUE)
        app.setPalette(self.oldPalette, TRUE)

    def polish_qwidget(self, w):
        # Hook to set attributes of certain widgets
        # the polish function will set some widgets to transparent mode, to get the
        # full benefit from the nice pixmaps in the color group.
        if w.inherits("QTipLabel"):
            return

        if w.inherits("QLCDNumber"):
            return

        if not w.isTopLevel():
            if w.inherits("QLabel") \
               or w.inherits("QButton") \
               or w.inherits("QComboBox") \
               or w.inherits("QGroupBox") \
               or w.inherits("QSlider") \
               or w.inherits("QTabWidget") \
               or w.inherits("QPanel"):
                w.setAutoMask(TRUE)


    def unPolish_qwidget(self, w):
        # Undo what we did in polish_qwidget
        if w.inherits("QTipLabel"):
            return

        if w.inherits("QLCDNumber"):
            return

        if not w.isTopLevel():
            if w.inherits("QLabel") \
               or w.inherits("QButton") \
               or w.inherits("QComboBox") \
               or w.inherits("QGroupBox") \
               or w.inherits("QSlider") \
               or w.inherits("QTabWidget") \
               or w.inherits("QPanel"):
                w.setAutoMask(FALSE)

    #
    # Panel, rectangles and lines
    #

    def drawPopupPanel(self, painter,x, y, w, h, colorGroup, lineWidth, fill):
        self.drawPanel(painter, x, y, w, h, colorGroup, FALSE, lineWidth, fill)

    def drawPanel(self, painter, x, y, w, h, colorGroup, sunken, lineWidth, fill):

        oldpen=painter.pen()
        oldbrush=painter.brush()

        if sunken:
            painter.setPen(QPen(colorGroup.foreground(), 2, QPen.DotLine))
        else:
            painter.setPen(QPen(colorGroup.foreground(), 2))
        if fill:
            oldbrush=painter.brush()
            painter.setPen(colorGroup.foreground())
            painter.setBrush(fill)

        painter.drawRect(x + 2, y + 2, w - 2, h - 2)

        painter.setPen(oldpen)
        painter.setBrush(oldbrush)

    def drawRect(self, painter, x, y, w, h, color, lineWidth, fill):
        qDrawPlainRect(painter, x, y, w, h, color, lineWidth, fill)

    def drawRectStrong(self, painter, x, y, w, h, colorGroup,
                             sunken, lineWidth, midLineWidth, fill):
        qDrawPlainRect(painter, x, y, w, h, colorGroup.foreground(),
                       sunken, lineWidth *2, fill)

    def drawSeparator(self, painter, x1, y1, x2, y2, colorGroup,
                            sunken, lineWidth, midLineWidth):
        painter.save()
        painter.setPen(colorGroup.foreground, lineWidth)
        painter.drawLine(x1, y1, x2, y2)
        painter.restore()

    def drawroundrect(self, painter, x, y, w, h):
        painter.drawRoundRect(x, y, w, h, 5, 50)

    def roundRectRegion(self, rect, r):
        x=rect.x()
        y=rect.y()
        right=x1+rect.right()
        bottom=y1+rect.bottom()
        a=QPointArray([8, x+r, y, right-r, y,
                      right, y + r, right, bottom-r,
                      right-r, bottom, x+r, bottom,
                      x, bottom-r, x, y+r])
        region=QRegion(a)

        d=r*2-1
        region.unite(QRegion(x, y, r*2, r*2, QRegion.Ellipse))
        region.unite(QRegion(right - d, y, r*2, r*2, QRegion.Ellipse))
        region.unite(QRegion(x, bottom-d, r*2, r*2, QRegion.Ellipse))
        region.unite(QRegion(right-d, bottom-d, r*2, r*2, QRegion.Ellipse))
        return region

    #
    # Tab
    #

    def drawTab(self, painter, tabBar, tab, selected):
        a=QPointArray(10)
        a.setPoint(0, 0, -1)
        a.setPoint(1, 0, 0)
        # Nasty! r is a private member of QTab. We shouldn't access it.
        y=tab.r.height()-2
        x=y/2
        x=x+1
        a.setPoint(2, x, y-1)
        x=x+1
        a.setPoint(3, x, y)
        x=x+1
        y=y+1
        a.setPoint(3, x, y)
        a.setPoint(4, x, y)

        right=tab.r.width()-1
        for i in range(5):
            a.setPoint(9-i, right - a.point(i)[0], a.point(i)[1])

        for i in range(10):
            a.setPoint(i, a.point(i)[0], tab.r.height() - 1 - a.point(i)[1])

        a.translate(tab.r.left(), tab.r.top())

        if selected:
            painter.setBrush(tabBar.colorGroup().background())
        else:
            painter.setBrush(tabBar.colorGroup().light())

        painter.setPen(tabBar.colorGroup().foreground())
        painter.drawPolygon(a)
        painter.setBrush(Qt.NoBrush)

    def drawTabMask(self, painter, tabbar, tab, selected):
        painter.drawRect(tab.r)

    #
    # Sliders
    #

    def drawSlider(self, painter, x, y, w, h, colorGroup,
                         orientation, tickAbove, tickBelow):
        pass

    def drawSliderMask(self, painter, x, y, w, h,
                             orientation, tickAbove, tickBelow):
        painter.fillRect(x, y, w, h, Qt.color1)

    def drawSliderGrooveMask(self, painter, x, y, w, h, coord, orientation):

        colorGroup=QColorGroup(Qt.color1, Qt.color1, Qt.color1, Qt.color1,
                               Qt.color1, Qt.color1, Qt.color1, Qt.color1,
                               Qt.color0)
        if orientation==Qt.Horizontal:
            painter.fillRect(x, y, w, h, Qt.color1)
        else:
            painter.fillRect(x, y, w, h, Qt.color1)

    #
    # Buttons and pushbuttons
    #

    def drawButton(self, painter, x, y, w, h, colorGroup,
                   sunken=FALSE, fill=None):
        oldBrush=painter.brush()

        if fill != None:
            painter.setBrush(fill)

        self.drawroundrect(painter, x, y, w, h)

        painter.setBrush(oldBrush)


    def drawPushButtonlabel (self, button, painter):
        QWindowsStyle.drawPushButonLabel(self, button, painter)

    def drawPushButton(self, button, painter):

        colorGroup=button.colorGroup()
        (x1, y1, x2, y2)=button.rect().coords()
        painter.setPen(colorGroup.foreground())
        painter.setBrush(QBrush(colorGroup.button(),
                                Qt.NoBrush))

        if button.isDown():
            brush=QBrush()
            brush.setColor(colorGroup.highlight())
            brush.setStyle(QBrush.SolidPattern)
            fill=brush
        elif button.isOn():
            brush=QBrush()
            brush.setColor(colorGroup.mid())
            brush.setStyle(QBrush.SolidPattern)
            fill=brush
        else:
            fill=colorGroup.brush(colorGroup.Button)

        if button.isDefault():
            painter.setPen(QPen(Qt.black, 3))
            self.drawroundrect(painter, x1, y1, x2-x1+1, y2-y1+1)
            painter.setPen(QPen(Qt.black, 1))
            x1=x1+4
            y1=y1+4
            x2=x2-4
            y2=y2-4

        if button.isOn() or button.isDown():
            sunken=TRUE
        else:
            sunken=FALSE

        self.drawButton(painter, x1, y1, x2-x1+1, y2-y1+1,
                        colorGroup, sunken, fill)

        if button.isMenuButton():
            dx=(y1-y2-4)/3
            self.drawArrow(painter, Qt.DownArrow, FALSE,
                           x2-dx, dx, y1, y2-y1,
                           colorGroup, button.isEnabled())

        if painter.brush().style != Qt.NoBrush:
            painter.setBrush(Qt.NoBrush)


    def drawPushButtonLabel(self, button, painter):
        r=button.rect()
        (x, y, w, h)=r.rect()

        (x1, y1, x2, y2)=button.rect().coords()
        dx=0
        dy=0
        if button.isMenuButton():
            dx=(y2-y1)/3
        if dx or dy:
            p.translate(dx,dy)

        x=x+2
        y=y+2
        w=w-4
        h=h-4
        g=button.colorGroup()
        if button.isDown() or button.isOn():
            pencolour=button.colorGroup().brightText()
        else:
            pencolour=button.colorGroup().buttonText()
        self.drawItem(painter, x, y, w, h,
                          Qt.AlignCenter|Qt.ShowPrefix,
                          g, button.isEnabled(),
                          button.pixmap(), button.text(), -1,
                          pencolour)

        if dx or dy:
            painter.translate(-dx,-dy)

    def drawBevelButton(self, painter, x, y, w, h, colorGroup,
                        sunken=FALSE, fill=None):
        self.drawButton(painter, x, y, w, h, colorGroup, sunken, fill)

    def buttonRect(self, x, y, w, h):
        return QRect(x+3, y+2, w-6, h-4)

    def drawButtonMask(self, p, x, y, w, h):
        self.drawroundrect(p, x, y, w, h)



    #
    # Radio Button
    #

    def drawExclusiveIndicator(self, painter, x, y, w, h, colorGroup,
                                     on, down, enabled):
        painter.eraseRect(x, y, w, h)
        painter.drawEllipse(x, y, w, h)

        if on:
            painter.setBrush(QBrush(colorGroup.foreground(), \
            QBrush.SolidPattern))
            
            painter.drawEllipse(x + 3, y + 3, w - 6, h -6)

    def drawExclusiveIndicatorMask(self, painter, x, y, w, h, on):
        painter.fillRect(x, y, w, h, QBrush(Qt.color1))

    #
    # Checkbox
    #

    def drawIndicator(self, painter, x, y, w, h, colorGroup,
                            state, down, enabled):
        painter.save()

        if enabled:
            painter.setPen(QPen(colorGroup.foreground(), 1, \
                           QPen.SolidLine))
        else:
            painter.setPen(QPen(colorGroup.mid(), 1, QPen.SolidLine))

        if state==QButton.Off:
            painter.setBrush(QBrush(colorGroup.background(), \
                                    QBrush.SolidPattern))
        elif state==QButton.NoChange:
            painter.setBrush(QBrush(colorGroup.dark(), \
                             QBrush.SolidPattern))
        else:
            painter.setBrush(QBrush(colorGroup.background(), \
                             QBrush.SolidPattern))

        painter.drawRect(x, y, w, h)

        if state==QButton.On:
            painter.drawLine(x, y, x + w, y + h)
            painter.drawLine(x, y + h - 1, x + w - 1, y)
        painter.restore()

    def drawIndicatorMask(self, painter, x, y, w, h, state):
        painter.fillRect(x, y , w + 3, h, QBrush(Qt.color1))

    #
    # Menu bar
    #

    def drawMenuBarItem(self, painter, x, y, w, h, menuItem, \
                        colorGroup, enabled, active):
        """
        Not subclassable?
        """
        self.drawItem(painter, x, y, w, h,
                      Qt.AlignCenter | Qt.ShowPrefix | Qt.DontClip | \
                      Qt.SingleLine, colorGroup, menuItem.pixmap(), \
                      menuItem.text(), -1, QColorGroup.buttonText())


    #
    # These items are not (yet) implemented in PyQt
    #

    def drawPopupMenuItem (self, painter, checkable, maxpmw, tab,
                                 menuItem, palette, act, enabled,
                                 x, y, w, h):
        """
        Not implemented in PyQt
        """
        pass

    def extraPopupMenuItemWidth (self, checkable, maxpmw,
                                       menuItem, fontMetrics):
        """
        Not implemented in PyQt
        """
        pass

    def popupMenuItemHeight (self, checkable, menuItem, fontMetrics):
        """
        Not implemented in PyQt
        """
        pass
