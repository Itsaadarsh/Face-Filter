#-------------Face Paradise GUI----------------------
#-------------Developer: @itsaadarsh-----------------

import dlib
import PIL
from PIL import ImageTk
import cv2
import random
from tkinter import *
from imutils import resize,face_utils

def gui():
    global imgtk
    if len(args_list) == 0 or args_list[-1] == 4 :
        frame = rawframe()
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA))
        imgtk = ImageTk.PhotoImage(image=img)
        guimain.imgtk = imgtk
        guimain.configure(image=imgtk)
        guimain.after(2, gui)
        
    else:
        frame =  button(args_list[-1])
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA))
        imgtk = ImageTk.PhotoImage(image=img)
        guimain.imgtk = imgtk
        guimain.configure(image=imgtk)
        guimain.after(2, gui)

def rawframe():
    _, frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame = cv2.flip(frame, 1)
    
    return frame

def glasses(img):
    _, frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = dect(gray)
    for face in faces:
        landmarks = pred(gray,face)
        landmarks = face_utils.shape_to_np(landmarks)
        le = landmarks[17:48]
        x,y,w,h = cv2.boundingRect(le)
        imgcpy = img.copy()
        imgcpy = resize(imgcpy,width = int(w*1.0334))
        iw,ih,ic = imgcpy.shape
        for i in range(iw):
            for j in range(ih):
                if imgcpy[i,j][2] != 0:
                    frame[int(y/1.04)+i,int(x)+j] = imgcpy[i,j]
                    
    return frame

def doliMask(img):
    _, frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = dect(gray)
    for face in faces:
        landmarks = pred(gray,face)
        landmarks = face_utils.shape_to_np(landmarks)
        le = landmarks[0:67]
        x,y,w,h = cv2.boundingRect(le)
        imgcpy = img.copy()
        imgcpy = resize(imgcpy,width = int(w))
        iw,ih,ic = imgcpy.shape
        for i in range(iw):
            for j in range(ih):
                if imgcpy[i,j][2] != 0:
                    frame[int(y/1.25)+i,int(x)+j] = imgcpy[i,j]
                    
    return frame

def nose(img):
    _, frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = dect(gray)
    for face in faces:
        landmarks = pred(gray,face)
        landmarks = face_utils.shape_to_np(landmarks)
        le = landmarks[28:35]
        x,y,w,h = cv2.boundingRect(le)
        imgcpy = img.copy()
        imgcpy = resize(imgcpy,width = int(w*2))
        iw,ih,ic = imgcpy.shape
        for i in range(iw):
            for j in range(ih):
                if imgcpy[i,j][2] != 0:
                    frame[int(y/1)+i,int(x/1.02)+j] = imgcpy[i,j]
                    
    return frame

def sketchFilter():
    _,frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame  = cv2.flip(frame,1)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (1,1),1)
    frame = cv2.Laplacian(frame, cv2.CV_8UC2, ksize = 5)
    frame = cv2.convertScaleAbs(frame)
    frame = 255 - frame
    
    return frame

def invertFilter():
    _, frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame = cv2.flip(frame, 1)
    frame = cv2.GaussianBlur(frame, (1,1),1)
    frame = 255 - frame
  
    return frame

def thermalFilter():
    _, frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame = cv2.flip(frame, 1)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL)
        
    return frame

def faceFilter():
    _, frame = cap.read()
    frame = cv2.resize(frame,(800,550))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = dect(gray)
    for face in faces:
        landmarks = pred(gray,face)
        landmarks = face_utils.shape_to_np(landmarks)
        le = landmarks[0:68]
        x,y,w,h = cv2.boundingRect(le)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(254,44,200),3)
        
    return frame

def frameCapture():
    glsFrame = glasses(gls_img)
    doliFrame = doliMask(mask_img)
    noseFrame = nose(nose_img)
    raw_frame = rawframe()
    sketchFrame = sketchFilter()
    invertFrame = invertFilter()
    thermalFrame = thermalFilter()
    faceFrame = faceFilter()
    
  
    if args_list[-1] == 1:
        for i in range(1):
            cv2.imwrite('Captures/Nose '+str(random.randint(0,10))+'.jpg', noseFrame)
            print('IMAGE SAVED')
            
            
    if args_list[-1] == 2:
        for i in range(1):
            cv2.imwrite('Captures/Doli '+str(random.randint(0,10))+'.jpg', doliFrame)
            print('IMAGE SAVED')
            
            
    if args_list[-1] == 3:
        for i in range(1):
            cv2.imwrite('Captures/Glasses '+str(random.randint(0,10))+'.jpg', glsFrame)
            print('IMAGE SAVED')
            
        
    if args_list[-1] == 4:
        for i in range(1):
            cv2.imwrite('Captures/Raw '+str(random.randint(0,10))+'.jpg', raw_frame)
            print('IMAGE SAVED')
            
    if args_list[-1] == 6:
        for i in range(1):
            cv2.imwrite('Captures/Sketch '+str(random.randint(0,10))+'.jpg', sketchFrame)
            print('IMAGE SAVED')
             
        
    if args_list[-1] == 7:
        for i in range(1):
            cv2.imwrite('Captures/Invert '+str(random.randint(0,10))+'.jpg', invertFrame)
            print('IMAGE SAVED')
            

    if args_list[-1] == 8:
        for i in range(1):
            cv2.imwrite('Captures/Thermal '+str(random.randint(0,10))+'.jpg', thermalFrame)
            print('IMAGE SAVED')           
        
    if args_list[-1] == 9:
        for i in range(1):
            cv2.imwrite('Captures/Face '+str(random.randint(0,10))+'.jpg', faceFrame)
            print('IMAGE SAVED')
            
        
def button(args):
    
    if args == 1:
        args_list.append(1)
        return nose(nose_img)
    
    if args == 2:
        args_list.append(2)
        return doliMask(mask_img)
    
    if args == 3:
        args_list.append(3)
        return glasses(gls_img)
    
    if args == 4:
        args_list.append(4)
        return rawframe()
    
    if args == 5:
        frameCapture()
        
    if args == 6:
        args_list.append(6)
        return sketchFilter()
    
    if args == 7:
        args_list.append(7)
        return invertFilter()
    
    if args == 8:
        args_list.append(8)
        return thermalFilter()
    
    if args == 9:
        args_list.append(9)
        return faceFilter()

cap = cv2.VideoCapture(0)
dect = dlib.get_frontal_face_detector()
pred = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')
args_list = [4]    
 
   
win = Tk()
win.title('Filter Paradise GUI')
win.geometry('1300x720')
win.iconbitmap(r'Filters/favicon.ico')
win.configure(background='turquoise1')
guimain = Label(win)    
guimain.pack()

nose_img = cv2.imread('Filters/1.png')
mask_img = cv2.imread('Filters/mask.png')
gls_img = cv2.imread('Filters/glasses.png')
nose_pic = PhotoImage(file = "Filters/nose.png")


b1 = Button(win,width=130,bg = 'black',image = nose_pic,height=130, 
            command = lambda:button(1),activebackground = 'yellow')
b1.place(x = 350,y = 570)

mask_pic = PhotoImage(file = "Filters/maskcpy.png")
b2 = Button(win,width=130,bg = 'black',image = mask_pic,height=130,
            command = lambda:button(2),activebackground = 'yellow')
b2.place(x = 600,y = 570)

gls_pic = PhotoImage(file = "Filters/gls.png")
b3 = Button(win, width=130,bg = 'black',image = gls_pic,height=130,
            command = lambda:button(3),activebackground = 'yellow')
b3.place(x = 850,y = 570)

raw_pic = PhotoImage(file = 'Filters/face.png')
b4 = Button(win, width=130,bg = 'black',image = raw_pic,height=130,
            command = lambda:button(4),activebackground = 'yellow')
b4.place(x = 80,y = 470)

save_pic = PhotoImage(file = 'Filters/save.png')
b5 = Button(win, width=130,bg = 'black',image = save_pic,height=130,
            command = lambda:button(5),activebackground = 'yellow')
b5.place(x = 1100,y = 470)

face_pic = PhotoImage(file = 'Filters/sk.png')
b6 = Button(win, width=130,bg = 'black',image = face_pic,height=130,
            command = lambda:button(6),activebackground = 'yellow')
b6.place(x = 1100,y = 250)

eyes_pic = PhotoImage(file = 'Filters/invert.png')
b7 = Button(win, width=130,bg = 'black',image = eyes_pic,height=130,
            command = lambda:button(7),activebackground = 'yellow')
b7.place(x = 1100,y = 50)

nf_pic = PhotoImage(file = 'Filters/thermal.png')
b8 = Button(win, width=130,bg = 'black',image = nf_pic,height=130,
            command = lambda:button(8),activebackground = 'yellow')
b8.place(x = 80,y = 250)

mouth_pic = PhotoImage(file = 'Filters/fc.png')
b9 = Button(win, width=130,bg = 'black',image = mouth_pic,height=130,
            command = lambda:button(9),activebackground = 'yellow')
b9.place(x = 80,y = 50)


pb1 = Label(win,text = 'Developed by @ITSAADARSH', bg="LightCyan4", fg="gold2", width=50,
                   height=2, font=('times', 20, 'bold '))
pb1.place(x=248, y=485)

pb2 = Label(win,text = 'Welcome to Filter Paradise', bg="LightCyan4", fg="gold2", width=50,
                   height=2, font=('times', 20, 'bold '))
pb2.place(x=248, y=0)


gui()
win.mainloop()
cap.release()