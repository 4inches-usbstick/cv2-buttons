import cv2

elements = []

#HELPERS
def blank():
    pass

def subset(needle, haystack_start, haystack_end):
    if needle in range(haystack_start, haystack_end): return True
    else: return False

#CLASSES TO CRY OVER
class Button:
    #draw button
    def __init__(self, x0, y0, width, height):
        self.origin = (x0, y0)
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
        cv2.rectangle(img, (x0, y0), (x0+width, y0+height), (255,255,255), 2)

        self.hover = blank
        self.click = blank
        self.unhover = blank
        self.unclick = blank

    #fill in the button with colors
    def fill(self, color = (255,255,255) ):
        img[self.y0:self.y0+self.height, self.x0:self.x0+self.width] = color
        cv2.imshow('image', img)


    #take a function as an input that can be called on events
    def setonclick(self, function):
        self.click = function

    def setonhover(self, function):
        self.hover = function

    def setonhoverno(self,function):
        self.unhover = function

    def setonclickno(self,function):
        self.unclick = function
    
def eventhandler(event, x, y, flags, param): 
    if event == cv2.EVENT_MOUSEMOVE:
        for i in elements:
            if subset(x, i.x0, i.x0+i.width) and subset(y,i.y0, i.y0+i.height):
                i.hover()
            else:
                i.unhover()

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in elements:
            if subset(x, i.x0, i.x0+i.width) and subset(y,i.y0, i.y0+i.height):
                i.click()
            else:
                i.unclick()
                


#initialize the window and plot elements    
img = cv2.imread('test.png')
s = Button(10, 10, 100, 50)
elements.append(s) #register it so it gets checked in mousemove event
s.fill()
s.setonhover(lambda: s.fill( (100,100,100) ))
s.setonhoverno(lambda: s.fill( (255,255,255) ))
s.setonclick(lambda: s.fill( (50,50,50) ) or print('hi') )

s1 = Button(10, 100, 100, 50)
elements.append(s1) #register it so it gets checked in mousemove event
s1.fill( (0,0,255) )
s1.setonhover(lambda: s1.fill( (0,0,100) ))
s1.setonhoverno(lambda: s1.fill( (0,0,255) ))
s1.setonclick(lambda: s1.fill( (0,0,50) ) or print('hi01') )

#show and begin event handling
cv2.imshow('image', img)
cv2.setMouseCallback('image', eventhandler)
cv2.waitKey(0)
cv2.destroyAllWindows()
