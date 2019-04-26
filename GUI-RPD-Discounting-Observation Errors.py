#-*-coding:utf-8-*-
import numpy as np
import numpy.linalg as LA
import random
import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg  import FigureCanvasTkAgg
from functools import partial
from tkinter import filedialog

#determinant D(p,q,f)
def D(p,q,f,epsilon,xi,w):
    tau,mu,eta = 1-2*epsilon-xi,1-epsilon-xi,epsilon+xi
    
    Matrix= [[w*(tau*p[1]*q[1]+epsilon*p[1]*q[2]+epsilon*p[2]*q[1]+xi*p[2]*q[2])-1+(1-w)*p[0]*q[0],w*(mu*p[1]+eta*p[2])-1+(1-w)*p[0],w*(mu*q[1]+eta*q[2])-1+(1-w)*q[0],f[0]],
             [w*(epsilon*p[1]*q[3]+xi*p[1]*q[4]+tau*p[2]*q[3]+epsilon*p[2]*q[4])  +(1-w)*p[0]*q[0],w*(eta*p[1]+mu*p[2])-1+(1-w)*p[0],w*(mu*q[3]+eta*q[4])  +(1-w)*q[0],f[1]],  
             [w*(epsilon*p[3]*q[1]+tau*p[3]*q[2]+xi*p[4]*q[1]+epsilon*p[4]*q[2])  +(1-w)*p[0]*q[0],w*(mu*p[3]+eta*p[4])  +(1-w)*p[0],w*(eta*q[1]+mu*q[2])-1+(1-w)*q[0],f[2]], 
             [w*(xi*p[3]*q[3]+epsilon*p[3]*q[4]+epsilon*p[4]*q[3]+tau*p[4]*q[4])  +(1-w)*p[0]*q[0],w*(eta*p[3]+mu*p[4])  +(1-w)*p[0],w*(eta*q[3]+mu*q[4])  +(1-w)*q[0],f[3]]
            ]
    return LA.det(Matrix)

def Calculation_Determinant(p,q_list,epsilon,xi,Sx,Sy,w):
    lx,ly = [],[]
    for i in range(len(q_list)):
        q=q_list[i]
        v1=[1,1,1,1]
        vdot1=D(p,q,v1,epsilon,xi,w)
        sy = D(p,q,Sx,epsilon,xi,w)/vdot1
        sx = D(p,q,Sy,epsilon,xi,w)/vdot1
        
        lx.append(sx)
        ly.append(sy)
    return lx,ly

#Inverse Matrix, Hilbe et al.,2015,GBE
def Calculation_Inverse(p,q_list,epsilon,xi,Sx,Sy,w):
    lx,ly=[],[]
    tau= 1-2*epsilon-xi
    for i in range(len(q_list)):
        q=q_list[i]

        M = np.array([
         [tau*p[1]*q[1]        +epsilon*p[1]*q[2]        +epsilon*p[2]*q[1]        +xi*p[2]*q[2],
          tau*p[1]*(1-q[1])    +epsilon*p[1]*(1-q[2])    +epsilon*p[2]*(1-q[1])    +xi*p[2]*(1-q[2]),
          tau*(1-p[1])*q[1]    +epsilon*(1-p[1])*q[2]    +epsilon*(1-p[2])*q[1]    +xi*(1-p[2])*q[2],
          tau*(1-p[1])*(1-q[1])+epsilon*(1-p[1])*(1-q[2])+epsilon*(1-p[2])*(1-q[1])+xi*(1-p[2])*(1-q[2])],
          
         [epsilon*p[1]*q[3]        +xi*p[1]*q[4]        +tau*p[2]*q[3]        +epsilon*p[2]*q[4],
          epsilon*p[1]*(1-q[3])    +xi*p[1]*(1-q[4])    +tau*p[2]*(1-q[3])    +epsilon*p[2]*(1-q[4]),
          epsilon*(1-p[1])*q[3]    +xi*(1-p[1])*q[4]    +tau*(1-p[2])*q[3]    +epsilon*(1-p[2])*q[4],
          epsilon*(1-p[1])*(1-q[3])+xi*(1-p[1])*(1-q[4])+tau*(1-p[2])*(1-q[3])+epsilon*(1-p[2])*(1-q[4])],
          
         [epsilon*p[3]*q[1]        +tau*p[3]*q[2]        +xi*p[4]*q[1]        +epsilon*p[4]*q[2],
          epsilon*p[3]*(1-q[1])    +tau*p[3]*(1-q[2])    +xi*p[4]*(1-q[1])    +epsilon*p[4]*(1-q[2]),
          epsilon*(1-p[3])*q[1]    +tau*(1-p[3])*q[2]    +xi*(1-p[4])*q[1]    +epsilon*(1-p[4])*q[2],
          epsilon*(1-p[3])*(1-q[1])+tau*(1-p[3])*(1-q[2])+xi*(1-p[4])*(1-q[1])+epsilon*(1-p[4])*(1-q[2])],
          
         [xi*p[3]*q[3]        +epsilon*p[3]*q[4]        +epsilon*p[4]*q[3]        +tau*p[4]*q[4],
          xi*p[3]*(1-q[3])    +epsilon*p[3]*(1-q[4])    +epsilon*p[4]*(1-q[3])    +tau*p[4]*(1-q[4]),
          xi*(1-p[3])*q[3]    +epsilon*(1-p[3])*q[4]    +epsilon*(1-p[4])*q[3]    +tau*(1-p[4])*q[4],
          xi*(1-p[3])*(1-q[3])+epsilon*(1-p[3])*(1-q[4])+epsilon*(1-p[4])*(1-q[3])+tau*(1-p[4])*(1-q[4])]
         ])
        
        IwM=np.eye(4)-w*M
        try:
            inverseIwM=np.linalg.inv(IwM)
        except:
            print("It can not be executed on w=1")
        
        v0=np.array([[p[0]*q[0],p[0]*(1-q[0]),(1-p[0])*q[0],(1-p[0])*(1-q[0])]])
        u=(1-w)*np.dot(v0,inverseIwM)
        sx=np.dot(u,Sx)
        sy=np.dot(u,Sy)
        lx.append(sx)
        ly.append(sy)
    return ly,lx

def Select_Method_Calculation(p,q_list,epsilon,xi,Sx,Sy,w,option):
    if option==0:
        lx,ly=Calculation_Determinant(p,q_list,epsilon,xi,Sx,Sy,w)
    elif option==1:
        if w==1:#Cannot Calculate, return wrong value when w=1
            lx,ly=100,100   
        else:
            lx,ly=Calculation_Inverse(p,q_list,epsilon,xi,Sx,Sy,w)
    return lx,ly

def Quit():
    global root
    root.quit()
    root.destroy()

def change_q(canvas, ax):
    global q_list
    q_list=[[random.random(),random.random(),random.random(),random.random(),random.random()] for i in range(1000)]
    DrawCanvas(canvas, ax, colors = "gray")

def change_5310(canvas, ax):
    global T,R,P,S
    if T==5:
        T,R,P,S=1.5,1,0,-0.5
    else:
        T,R,P,S=5,3,1,0
    DrawCanvas(canvas, ax, colors = "gray")
    
def save_fig():
    filepath = filedialog.askdirectory(initialdir = dir)
    path=filepath+'\\fig.png'
    print('save_Image')
    print(path)
    plt.savefig(path)

def DrawCanvas(canvas, ax, colors = "gray"):
    ax.cla()
    
    w=1-scale5.get()/100
    epsilon=scale6.get()/1000
    xi=scale7.get()/1000
    option=scale8.get()
    
    i=1000#stride
    #p=(p0,p1,p2,p3,p4)
    p=[scale0.get()/i,scale1.get()/i,scale2.get()/i,scale3.get()/i,scale4.get()/i]
    

    RE = R*(1-epsilon-xi)+S*(epsilon+xi)
    SE = S*(1-epsilon-xi)+R*(epsilon+xi)
    TE = T*(1-epsilon-xi)+P*(epsilon+xi)
    PE = P*(1-epsilon-xi)+T*(epsilon+xi)
    plt.title(r"(T,R,P,S)=("+str(T)+","+str(R)+","+str(P)+","+str(S)+")\n"+r"$(w,\epsilon,\xi)=($"+str(w)+","+str(epsilon)+","+str(xi)+r"$)$",fontsize=25)
    plt.ylabel("Payoff of ("+str(p[1])+","+str(p[2])+","+str(p[3])+","+str(p[4])+"),$p_0=$"+str(p[0]),fontsize=25)
    plt.xlabel("Payoff of Opponent",fontsize=25)

    plt.rcParams["font.size"] = 15
    plt.xlim([S-0.2,T+0.2])
    plt.ylim([S-0.2,T+0.2])
    plt.text(P-0.4, P-0.2, r'$(P,P)$')
    plt.text(R+0.05, R, r'$(R,R)$')
    plt.text(T-0.1, S-0.1, r'$(T,S)$')
    plt.text(S-0.1, T+0.05, r'$(S,T)$')
    plt.plot([R,S,P,T,R],[R,T,P,S,R],'r',color="black",markersize=3,alpha=0.5)
    plt.plot([R,S,P,T,R],[R,T,P,S,R],'o',color="black",markersize=3)
    plt.plot([RE,SE,PE,TE,RE],[RE,TE,PE,SE,RE],'r',color="black",markersize=3,alpha=0.5)
    plt.plot([RE,SE,PE,TE,RE],[RE,TE,PE,SE,RE],'o',color="black",markersize=3)
    plt.plot([R,P],[R,P],'r',linestyle="dashed",color="black",markersize=3,alpha=0.5)

    Sx,Sy = [RE,SE,TE,PE],[RE,TE,SE,PE]#expected stage payoff vector
    y,x = Select_Method_Calculation(p,q_list,epsilon,xi,Sx,Sy,w,option)
    
    x0,y0=Select_Method_Calculation(p,[[0,0,0,0,0]],epsilon,xi,Sx,Sy,w,option)
    x1,y1=Select_Method_Calculation(p,[[1,1,1,1,1]],epsilon,xi,Sx,Sy,w,option)
    plt.plot(y,x,'go',markersize=4,alpha=0.8)
    plt.plot(x0,y0,'ro',markersize=6,alpha=0.8)
    plt.plot(x1,y1,'bo',markersize=6,alpha=0.8)
    
    canvas.draw()

if __name__ == "__main__":
    try:
        #generate GUI
        root = tkinter.Tk()
        root.title("GUI- vs 1,000 Strategies Under Discounting and Observation Errors in RPD game")

        #generate graph
        fig,ax1 = plt.subplots(figsize=(8,8))
        fig.gca().set_aspect('equal', adjustable='box')

        #generate Canvas
        Canvas = FigureCanvasTkAgg(fig, master=root)
        Canvas.get_tk_widget().grid(row=0, column=0, rowspan=1000)
        T,R,P,S=1.5,1,0,-0.5
        q_list=[[random.random(),random.random(),random.random(),random.random(),random.random()] for i in range(1000)]
        
        ReDrawButton = tkinter.Button(text="Other Opponent", width=15, command=partial(change_q, Canvas, ax1))
        ReDrawButton.grid(row=12, column=1, columnspan=1)
        TRPSButton = tkinter.Button(text="TRPS 5310", width=15, command=partial(change_5310, Canvas, ax1))
        TRPSButton.grid(row=15, column=1, columnspan=1)
        SaveButton = tkinter.Button(text="Save Fig", width=15, command=save_fig)
        SaveButton.grid(row=21, column=1, columnspan=1)
        
        scale0 = tkinter.Scale(root, label='p0', orient='h', from_=0, to=1000, command=partial(DrawCanvas, Canvas, ax1))
        scale0.grid(row=2, column=3, columnspan=1)
        scale1 = tkinter.Scale(root, label='p1', orient='h', from_=0, to=1000, command=partial(DrawCanvas, Canvas, ax1))
        scale1.grid(row=3, column=3, columnspan=1)
        scale2 = tkinter.Scale(root, label='p2',orient='h', from_=0.0, to=1000, command=partial(DrawCanvas, Canvas, ax1))
        scale2.grid(row=4, column=3, columnspan=1)
        scale3 = tkinter.Scale(root, label='p3',orient='h', from_=0, to=1000, command=partial(DrawCanvas, Canvas, ax1))
        scale3.grid(row=5, column=3, columnspan=1)
        scale4 = tkinter.Scale(root, label='p4',orient='h', from_=0, to=1000, command=partial(DrawCanvas, Canvas, ax1))
        scale4.grid(row=6, column=3, columnspan=1)
        
        scale5 = tkinter.Scale(root, label='w',orient='h', from_=0, to=100, command=partial(DrawCanvas, Canvas, ax1))
        scale5.grid(row=3, column=1, columnspan=1)
        scale6 = tkinter.Scale(root, label='epsilon',orient='h', from_=0, to=300, command=partial(DrawCanvas, Canvas, ax1))
        scale6.grid(row=4, column=1, columnspan=1)
        scale7 = tkinter.Scale(root, label='xi', orient='h', from_=0, to=300, command=partial(DrawCanvas, Canvas, ax1))
        scale7.grid(row=5, column=1, columnspan=1)
        scale8 = tkinter.Scale(root, label='(0)Det (1)Inverse', orient='h', from_=0, to=1, command=partial(DrawCanvas, Canvas, ax1))
        scale8.grid(row=2, column=1, columnspan=1)
        QuitButton = tkinter.Button(text="Quit", width=15, command=Quit)
        QuitButton.grid(row=30, column=1, columnspan=1)
        
        DrawCanvas(Canvas,ax1)
        root.mainloop()
    except:
        import traceback
        traceback.print_exc()
