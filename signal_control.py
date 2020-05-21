import wx

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
class CrossingSignalCalculater(wx.Frame): 
    
    
    def __init__(self):
        

        ##定义名称
        wx.Frame.__init__(self, None, -1, '信号交叉口配时参数计算',size=(1190, 800))  
        
 
 


       
        ##静态文本显示
        self.panel = wx.Panel(self, -1) 
        
        self.rev = wx.StaticText(self.panel, -1, "信号交叉口配时参数计算", (460,10))  
        self.rev.SetForegroundColour('black')  
        self.rev.SetBackgroundColour('white')
        ###定义静态文本字体
        font = wx.Font(18, wx.DECORATIVE,wx.ITALIC, wx.NORMAL)  
        self.rev.SetFont(font)  
        ##绘制前后损失、黄灯、全红时间对话框
        loss1 = wx.StaticText(self.panel,-1,"前损失(s):",(20,100))
        self.loss1 = wx.TextCtrl(self.panel, -1, "1",(80,100), size=(50, 20))
        loss2 = wx.StaticText(self.panel,-1,"后损失(s):",(140,100))
        self.loss2 = wx.TextCtrl(self.panel, -1, "1",(200,100), size=(50, 20))
        yellow = wx.StaticText(self.panel,-1,"黄灯时间(s):",(260,100))
        self.yellow = wx.TextCtrl(self.panel, -1, "3",(330,100), size=(50, 20))
        allred = wx.StaticText(self.panel,-1,"全红时间(s):",(390,100))
        self.allred = wx.TextCtrl(self.panel, -1, "1",(460,100), size=(50, 20))
         ##建立相位个数选项框
        #self.dict = {'1':2,'2':3,'3':4,'4':4,'5':4}
        authors = ['2','3','4']
        text1 = wx.StaticText(self.panel,-1,"请输入相位数:",(20,60))
        self.choose = wx.ComboBox(self.panel,-1,'', pos=(100, 60), size=(130, -1), choices=authors , style=wx.CB_SORT)
        self.button=wx.Button(parent=self.panel,id=-1,label=u'确定',pos=(280,60))
      
        ##插入相位图
        img3=wx.Image('相位方案图.jpg',wx.BITMAP_TYPE_ANY)
        show3=wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img3),pos=(20,130))
      
     
    
        self.Bind(wx.EVT_BUTTON,self.Settings,self.button)
        
      
        sb=wx.StaticBox(self.panel, label='预定义参数',pos = (10,38),size = (520,180))
       
      
 
     
 

        
  
    def Recalculate(self,event):
        self.Destroy() 
        app = wx.PySimpleApp()  
        frame = CrossingSignalCalculater()  
        frame.Show()  
        app.MainLoop() 
    def Exit(self,event):
        self.Destroy()
    
    def isisnumber(self,a):
        try:
            int(a)
            return int(a) #能成功转换为浮点型，则是数字
        except:
            return 0 
 
 
        
        
        
        
    def Settings(self,event):

        self.phase= self.isisnumber(self.choose.GetValue())

        basiclabel = [0,0,0,0,0] ##每方向流量
        self.lanes = [0,0,0,0,0]
        for i in range(self.phase):
            basiclabel[i] = wx.StaticText(self.panel,-1,"相位"+str(i+1)+"包含车道数(请输入1-4之间的数字):",(20,245+20*i))
            self.lanes[i] = wx.TextCtrl(self.panel, -1, "",(240,245+20*i), size=(70, 20))
        self.button4=wx.Button(parent=self.panel,id=-1,label=u'确定',pos=(320,245))
        
        sb=wx.StaticBox(self.panel, label='车道数输入',pos = (10,220),size = (520,115))
        
    
        self.Bind(wx.EVT_BUTTON,self.Settings2,self.button4)
        
    def Settings2(self,event):
        self.lanes_1= [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.lanes_2= [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for i in range(self.phase):
            a = self.isisnumber(self.lanes[i].GetValue())
            wx.StaticText(self.panel,-1,"相位"+str(i+1)+"各车道流量(pcu/h):",(20,365+50*i))
            wx.StaticText(self.panel,-1,"各车道饱和流率(pcu/h):",(20,385+50*i))
            for j in range(a):
                self.lanes_1[i][j] = wx.TextCtrl(self.panel, -1, "",(160+90*j,365+50*i), size=(70, 20))
                self.lanes_2[i][j] = wx.TextCtrl(self.panel, -1, "",(160+90*j,385+50*i), size=(70, 20))
       
        ##输入行人流量
        wx.StaticText(self.panel, -1, "行人流量 南北方向(人/小时):",(20,565))
        self.non_auto1 = wx.TextCtrl(self.panel, -1, "",(190,565), size=(70, 20))
        wx.StaticText(self.panel, -1, "行人流量 东西方向(人/小时):",(20,585))
        self.non_auto2 = wx.TextCtrl(self.panel, -1, "",(190,585), size=(70, 20))
        wx.StaticText(self.panel, -1, "非机动车 南北方向(车/小时):",(20,605))
        self.non_auto3 = wx.TextCtrl(self.panel, -1, "",(190,605), size=(70, 20))
        wx.StaticText(self.panel, -1, "非机动车 东西方向(车/小时):",(20,625))
        self.non_auto4 = wx.TextCtrl(self.panel, -1, "",(190,625), size=(70, 20))
        wx.StaticText(self.panel, -1, "人行横道长度 南北方向(米):",(270,565))
        self.length1 = wx.TextCtrl(self.panel, -1, "",(440,565), size=(70, 20))
        wx.StaticText(self.panel, -1, "人行横道长度 东西方向(米):",(270,585))
        self.length2 = wx.TextCtrl(self.panel, -1, "",(440,585), size=(70, 20))
        wx.StaticText(self.panel, -1, "人行横道宽度 南北方向(米):",(270,605))
        self.length3 = wx.TextCtrl(self.panel, -1, "3",(440,605), size=(70, 20))
        wx.StaticText(self.panel, -1, "人行横道宽度 东西方向(米):",(270,625))
        self.length4 = wx.TextCtrl(self.panel, -1, "3",(440,625), size=(70, 20))
        wx.StaticText(self.panel, -1, "非机动车相位提前截止时间 南北方向(s):",(20,645))
        self.non1 = wx.TextCtrl(self.panel, -1, "",(240,645), size=(70, 20))
        wx.StaticText(self.panel, -1, "东西方向(s):",(350,645))
        self.non2 = wx.TextCtrl(self.panel, -1, "",(440,645), size=(70, 20))
        
        sb=wx.StaticBox(self.panel, label='流量输入',pos = (10,340),size = (520,365))
        
        ##绘制第二部分的确定按钮
        self.button5=wx.Button(parent=self.panel,id=-1,label=u'确定',pos=(210,665))
        self.Bind(wx.EVT_BUTTON,self.Settings3,self.button5)
        
    def Settings3(self,event):
        dui = wx.StaticText(self.panel,-1,"√已识别关键车道:",(320,665)) 
        dui.SetForegroundColour('green')
        self.jisuan = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for i in range(self.phase):
            a = self.isisnumber(self.lanes[i].GetValue())
            for j in range(a):
                self.lanes_1[i][j] = self.isisnumber(self.lanes_1[i][j].GetValue())
                self.lanes_2[i][j] = self.isisnumber(self.lanes_2[i][j].GetValue())
                if self.lanes_2[i][j] != 0:
                    self.jisuan[i][j] = self.lanes_1[i][j]/self.lanes_2[i][j]
                else:
                    self.lanes_2[i][j] = 0

        self.b = []
        self.c = []
        self.jisuan2 = []
        for i in range(self.phase):
            self.jisuan2.append(max(self.jisuan[i]))
        
        for i in range(self.phase):
            a = self.isisnumber(self.lanes[i].GetValue())
            for j in range(a):
                if self.jisuan[i][j] == self.jisuan2[i]:
                    self.b.append(self.lanes_1[i][j])
                    self.c.append(self.lanes_2[i][j])
        
            
         ##绘制“计算”button
        self.button1=wx.Button(parent=self.panel,id=-1,label=u'计算',pos=(670,600))         
        self.Bind(wx.EVT_BUTTON,self.CloseMe,self.button1)
        
        ##建立输出框_有效绿灯时间
        self.Ge = [0,0,0,0,0]
        self.output = [0,0,0,0,0]
        for i in range(self.phase):
            self.Ge[i] = wx.StaticText(self.panel, -1, "相位"+str(i+1)+"有效绿灯时间:",(600,60+20*i))  
            self.output[i] = wx.TextCtrl(self.panel, -1, "",(710,60+20*i), size=(60, 20))     
  
        self.green = [0,0,0,0,0]
        self.phase_lamda = [0,0,0,0,0]
        self.flow_rate = [0,0,0,0,0]
        self.saturation_degree = [0,0,0,0,0]
        ##建立输出框_显示绿灯时间
        for i in range(self.phase):
            wx.StaticText(self.panel,-1,"显示绿灯时间:",(780,60+20*i))        
            self.green[i]= wx.TextCtrl(self.panel, -1, "",(860,60+20*i), size=(60, 20))     
        ##建立输出框_各相位绿信比和流量比
        for i in range(self.phase):
            wx.StaticText(self.panel,-1,"绿信比:",(930,60+20*i))         
            self.phase_lamda[i]= wx.TextCtrl(self.panel, -1, "",(970,60+20*i), size=(60, 20))   
            wx.StaticText(self.panel,-1,"流量比:",(1050,60+20*i))       
            self.flow_rate[i]= wx.TextCtrl(self.panel, -1, "",(1090,60+20*i), size=(60, 20))     
            #wx.StaticText(self.panel,-1,"饱和度:",(610,260+20*i))
            #self.saturation_degree[i]= wx.TextCtrl(self.panel, -1, "",(650,260+20*i), size=(70, 20))
            
        ##建立输出框_周期参数、总损失、周期时长
        cycle = wx.StaticText(self.panel, -1, "周期参数", (600,145))     
        wx.StaticText(self.panel, -1, "总流量比:",(660,145))        
        self.total_rate = wx.TextCtrl(self.panel, -1, "",(720,145), size=(70, 20))   
        wx.StaticText(self.panel, -1, "总损失:",(800,145))
        self.total_loss= wx.TextCtrl(self.panel, -1, "",(840,145), size=(70, 20))
        wx.StaticText(self.panel, -1, "周期时长:",(940,145))
        self.cycle_length= wx.TextCtrl(self.panel, -1, "",(1000,145), size=(70, 20))
        
        
        self.multiText=wx.TextCtrl(self.panel,-1,"",(600,240), size=(550, 160),style=wx.TE_MULTILINE)
        wx.StaticText(self.panel, -1, "配时图:",(600,420))                 
        
        sb=wx.StaticBox(self.panel, label='参数输出',pos = (580,38),size = (580,180))
        sb=wx.StaticBox(self.panel, label='配时方案',pos = (580,220),size = (580,485))
        
        ##绘制“重新运行”和“退出程序”button
        self.button2=wx.Button(parent=self.panel,id=-1,label=u'重新运行',pos=(790,600))  
        self.Bind(wx.EVT_BUTTON,self.Recalculate,self.button2)
        self.button3=wx.Button(parent=self.panel,id=-1,label=u'退出程序',pos=(910,600))    
        self.Bind(wx.EVT_BUTTON,self.Exit,self.button3)
        
        
    
  
    
    def OverFlow(self):  ##当饱和度>1时，要用基于最大排队长度的最大周期时长优化方法，减小周期长
        self.add = wx.StaticText(self.panel,-1,"❌注意：交叉口处于过饱和状态，请输入饱和状态持续时长(s):",(600,180))     
        self.T = wx.TextCtrl(self.panel, -1, "",(1000,180), size=(70, 20))   
        self.add.SetForegroundColour('red')
        self.Bind(wx.EVT_BUTTON,self.OverFlow2,self.button1)
    def OverFlow2(self,event):
        flow = self.b
        s2 = self.c
        
        non_auto1 = self.isisnumber(self.non_auto1.GetValue()) 
        non_auto2 = self.isisnumber(self.non_auto2.GetValue()) 
        non_auto3 = self.isisnumber(self.non_auto3.GetValue()) 
        non_auto4 = self.isisnumber(self.non_auto4.GetValue()) 
        length1 = self.isisnumber(self.length1.GetValue()) 
        length2 = self.isisnumber(self.length2.GetValue()) 
        length3 = self.isisnumber(self.length3.GetValue()) 
        length4 = self.isisnumber(self.length4.GetValue()) 
        non1 = self.isisnumber(self.non1.GetValue()) 
        non2 = self.isisnumber(self.non2.GetValue()) 
      

        #GetValue得到的是字符串形式。
  
        yellow = self.isisnumber(self.yellow.GetValue())  #黄灯时间
        allred = self.isisnumber(self.allred.GetValue())  #全红时间
        loss1 = self.isisnumber(self.loss1.GetValue())  #前损失
        loss2 = self.isisnumber(self.loss2.GetValue())  #后损失
        L = self.phase*(loss1+yellow+allred-yellow+loss2) #周期总损失
        Y = 0
        for i in range(self.phase):
            Y += int(flow[i])/int(s2[i])
 
        T = self.isisnumber(self.T.GetValue())
        list1 = [0,0,0,0,0]
        for i in range(self.phase):
            if s2[i]!= 0:
                list1.append(int(flow[i])/int(s2[i]))
            else:
                list1.append(0)
        Co = (L*1800/(Y*(1-max(list1))))**0.5#定义更小的周期长
        Ge = Co-L  #有效绿灯时间
        total_lamda = Ge/Co #总绿信比

        ##计算各相位流量比、绿信比和有效绿灯时间、显示绿灯时间
        y = []
        split = []
        rate = []
        saturation = []
        green = []
        for i in range(self.phase):
            y.append(Ge*int(flow[i])/(int(s2[i])*Y))

        ##考虑行人流量
        if length3<=3:
            y_min1 = 3.2+2.7*non_auto1*Co/3600+length1/1.2
        else:
            y_min1 = 3.2+(2.7/length3)*non_auto1*Co/3600+length1/1.2
        if length4<=3:
            y_min2 = 3.2+2.7*non_auto2*Co/3600+length2/1.2
        else:
            y_min2 = 3.2+(2.7/length4)*non_auto2*Co/3600+length2/1.2

        if self.phase == 2:  ##HCM2010行人最小绿灯时间需求
            y2 = [max(y[0],y_min1),max(y[1],y_min2)]
            
        if self.phase == 3:
            y2 = [max(y[0],y_min1),max(y[1],y_min2),y[2]]    ##先直行相位后左转相位
            
        if self.phase == 4:
            y2 = [max(y[0],y_min1),y[1],max(y[2],y_min2),y[3]]    ##先直行相位后左转相位
            
        for i in range(self.phase):
            split.append(total_lamda*int(flow[i])/(int(s2[i])*Y))
            rate.append(int(flow[i])/(int(s2[i])))
            saturation.append(rate[i]/split[i])
            green.append(y2[i]-yellow+loss1+loss2)   
        for i in range(self.phase):
            if green[i]<=5:
                self.d = wx.StaticText(self.panel,-1,"❌注意：相位流量比过小，请调整相位数",(600,200))  
                self.d.SetForegroundColour('red')
        
        
        for i in range(self.phase):
            self.output[i].SetValue(str(y2[i]))
            self.green[i].SetValue(str(green[i]))
            self.phase_lamda[i].SetValue(str(split[i]))  
            self.flow_rate[i].SetValue(str(rate[i]))

        ##显示周期参数——总流量比、总损失、周期时长
        Co = self.phase*(yellow+allred)
        for i in range(self.phase):
            Co += round(green[i])
        self.total_rate.SetValue(str(Y))
        self.total_loss.SetValue(str(L))
        self.cycle_length.SetValue(str(Co))
        
        if non1 <= yellow+allred:
            non1 = 0
        else:
            non1 = non1-yellow-allred
        if non2 <= yellow+allred:
            non2 = 0
        else:
            non2 = non2-yellow-allred

        
        if self.phase == 2:
            a = [0,0]
            p_green = [0,0]
            p_green[0] = "相位1"+"行人绿灯时间:" +str(round(green[0])-round(length1/1.2))+'(s)'+"行人绿闪时间:"+str(round(length1/1.2)-non1)+'(s)'+"非机动车绿灯时间:"+str(round(green[0])-non1)+'(s)'
            p_green[1] = "相位2"+"行人绿灯时间:" +str(round(green[1])-round(length2/1.2))+'(s)'+"行人绿闪时间:"+str(round(length2/1.2)-non2)+'(s)'+"非机动车绿灯时间:"+str(round(green[1])-non2)+'(s)'
            a[0] = "相位1 "+"全红:"+str(allred)+'(s)'+"绿灯:"+str(round(green[0]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[0])-yellow-allred)+'(s)'
            a[1] = "相位2 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(Co)-round(green[1])-yellow-allred)+'(s)'+"绿灯:"+str(round(green[1]))+'(s),'+"黄灯:"+str(yellow)+'(s)'
            self.multiText.SetValue("信号配时结果"+'\n'+a[0]+'\n'+p_green[0]+'\n'+p_green[1]+'\n'+a[1])
            
            plt.figure(figsize = (60,5))
            x=["phase2","phase1"]
            y = [allred,allred]
            y2 = [round(Co)-round(green[1])-yellow-allred,0]
            y3 = [round(green[1]),round(green[0])]
            y4 = [yellow,yellow]
            y5 = [0,round(Co)-round(green[0])-yellow-allred]
            t1 = np.array(y)
            t2 = np.array(y2)
            t3 = np.array(y3)
            t4 = np.array(y4)
            t5 = np.array(y5)
 
            t21= list(np.sum([t1,t2],axis=0))
            t31 = list(np.sum([t21,t3],axis = 0))
            t41 = list(np.sum([t31,t4],axis = 0))

            plt.xlim(0,100)
            plt.barh(x,y,align="center",color="r",label="y")
            plt.barh(x,y2,left=y,color="r",label="y2")
            plt.barh(x,y3,left=t21,color="green",label="y3")
            plt.barh(x,y4,left=t31,color="yellow",label="y4")
            plt.barh(x,y5,left=t41,color="red",label="y5")
            plt.legend()
            plt.tick_params(labelsize=60)

            plt.savefig('1.jpg')
            img2=wx.Image('1.jpg',wx.BITMAP_TYPE_ANY).Scale(550,60)
            show2=wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img2),pos=(600,440))
            
        if self.phase == 3:
            a = [0,0,0]
            p_green = [0,0]
            p_green[0] = "相位1"+"行人绿灯时间:" +str(round(green[0])-round(length1/1.2))+'(s)'+"行人绿闪时间:"+str(round(length1/1.2)-non1)+'(s)'+"非机动车绿灯时间:"+str(round(green[0]-non1))+'(s)'
            p_green[1] = "相位2"+"行人绿灯时间:" +str(round(green[1])-round(length2/1.2))+'(s)'+"行人绿闪时间:"+str(round(length2/1.2)-non2)+'(s)'+"非机动车绿灯时间:"+str(round(green[1]-non2))+'(s)'
            a[0] = "相位1 "+"全红:"+str(allred)+'(s)'+"绿灯:"+str(round(green[0]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[0])-yellow-allred)+'(s)'
            a[1] = "相位2 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(green[0])+yellow+allred)+'(s)'+"绿灯:"+str(round(green[1]))+'(s),'+"黄灯:"+str(yellow)+'红灯'+str(round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]))+'(s)'
            a[2] = "相位3 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(Co)-round(green[2])-yellow-allred)+'(s)'+"绿灯:"+str(round(green[2]))+'(s),'+"黄灯:"+str(yellow)+'(s)'
            self.multiText.SetValue("信号配时结果"+'\n'+a[0]+'\n'+p_green[0]+'\n'+a[1]+'\n'+p_green[1]+'\n'+a[2])
            
            plt.figure(figsize = (60,5))
            x=["phase3","phase2","phase1"]
            y = [allred,allred,allred]
            y2 = [round(Co)-round(green[2])-yellow-allred,round(green[0])+yellow+allred,0]
            y3 = [green[2],green[1],green[0]]
            y4 = [yellow,yellow,yellow]
            y5 = [0,round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]),round(Co)-round(green[0])-yellow-allred]
            t1 = np.array(y)
            t2 = np.array(y2)
            t3 = np.array(y3)
            t4 = np.array(y4)
            t5 = np.array(y5)
 
            t21= list(np.sum([t1,t2],axis=0))
            t31 = list(np.sum([t21,t3],axis = 0))
            t41 = list(np.sum([t31,t4],axis = 0))

            plt.xlim(0,200)
            plt.barh(x,y,align="center",color="r",label="y")
            plt.barh(x,y2,left=y,color="r",label="y2")
            plt.barh(x,y3,left=t21,color="green",label="y3")
            plt.barh(x,y4,left=t31,color="yellow",label="y4")
            plt.barh(x,y5,left=t41,color="red",label="y5")
            plt.legend()
            plt.tick_params(labelsize=60)

            plt.savefig('1.jpg')
            img2=wx.Image('1.jpg',wx.BITMAP_TYPE_ANY).Scale(550,60)
            show2=wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img2),pos=(600,440))
        
        
        if self.phase == 4:
            a = [0,0,0,0]
            p_green = [0,0]
            p_green[0] = "相位1"+"行人绿灯时间:" +str(round(green[0])-round(length1/1.2))+'(s)'+"行人绿闪时间:"+str(round(length1/1.2)-non1)+'(s)'+"非机动车绿灯时间:"+str(round(green[0]-non1))+'(s)'
            p_green[1] = "相位3"+"行人绿灯时间:" +str(round(green[2])-round(length2/1.2))+'(s)'+"行人绿闪时间:"+str(round(length2/1.2)-non2)+'(s)'+"非机动车绿灯时间:"+str(round(green[2]-non2))+'(s)'
            a[0] = "相位1 "+"全红:"+str(allred)+'(s)'+"绿灯:"+str(round(green[0]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[0])-yellow-allred)+'(s)'
            a[1] = "相位2 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(green[0])+yellow+allred)+'(s)'+"绿灯:"+str(round(green[1]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]))+'(s)'
            a[2] = "相位3 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(green[0])+yellow+round(green[1])+yellow+2*allred)+'(s)'+"绿灯:"+str(round(green[2]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[2])-3*yellow-3*allred-round(green[0])-round(green[1]))+'(s)'
            a[3] = "相位4 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(Co)-round(green[3])-yellow-allred)+'(s)'+"绿灯:"+str(round(green[3]))+'(s),'+"黄灯:"+str(yellow)+'(s)'
            self.multiText.SetValue("信号配时结果"+'\n'+a[0]+'\n'+p_green[0]+'\n'+a[1]+'\n'+a[2]+'\n'+p_green[1]+'\n'+a[3])
        
            plt.figure(figsize = (60,5))
            x=["phase4","phase3","phase2","phase1"]
            y = [allred,allred,allred,allred]
            y2 = [round(Co)-round(green[3])-yellow-allred,round(green[0])+yellow+round(green[1])+yellow+2*allred,round(green[0])+yellow+allred,0]
            y3 = [round(green[3]),round(green[2]),round(green[1]),round(green[0])]
            y4 = [yellow,yellow,yellow,yellow]
            y5 = [0,round(Co)-round(green[2])-3*yellow-3*allred-round(green[0])-round(green[1]),round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]),round(Co)-round(green[0])-yellow-allred]
            t1 = np.array(y)
            t2 = np.array(y2)
            t3 = np.array(y3)
            t4 = np.array(y4)
            t5 = np.array(y5)
   
            t21 = list(np.sum([t1,t2],axis=0))
            t31 = list(np.sum([t21,t3],axis = 0))
            t41 = list(np.sum([t31,t4],axis = 0))

            plt.xlim(0,300)
            plt.barh(x,y,align="center",color="r",label="y")
            plt.barh(x,y2,left=y,color="r",label="y2")
            plt.barh(x,y3,left=t21,color="green",label="y3")
            plt.barh(x,y4,left=t31,color="yellow",label="y4")
            plt.barh(x,y5,left=t41,color="red",label="y5")
            plt.legend()
            plt.tick_params(labelsize=60)

            plt.savefig('1.jpg')
            img2=wx.Image('1.jpg',wx.BITMAP_TYPE_ANY).Scale(550,60)
            show2=wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img2),pos=(600,440))
                    
    
              
        
                

  
        
        
    def CloseMe(self,event):
      
        flow = self.b
        s2 = self.c
        non_auto1 = self.isisnumber(self.non_auto1.GetValue()) 
        non_auto2 = self.isisnumber(self.non_auto2.GetValue()) 
        non_auto3 = self.isisnumber(self.non_auto3.GetValue()) 
        non_auto4 = self.isisnumber(self.non_auto4.GetValue()) 
        length1 = self.isisnumber(self.length1.GetValue()) 
        length2 = self.isisnumber(self.length2.GetValue()) 
        length3 = self.isisnumber(self.length3.GetValue()) 
        length4 = self.isisnumber(self.length4.GetValue())
        non1 = self.isisnumber(self.non1.GetValue()) 
        non2 = self.isisnumber(self.non2.GetValue()) 
        
  
      
        #GetValue得到的是字符串形式。
   
        yellow = self.isisnumber(self.yellow.GetValue())#黄灯时间
        allred = self.isisnumber(self.allred.GetValue())  #全红时间
        loss1 = self.isisnumber(self.loss1.GetValue())  #前损失
        loss2 = self.isisnumber(self.loss2.GetValue())  #后损失

        L = self.phase*(loss1+yellow+allred-yellow+loss2)  #周期总损失
        
        Y = 0
        Co = 0.1
       
        for i in range(self.phase):
            if int(s2[i]) != 0:
                Y += int(flow[i])/int(s2[i])
            else:
                Y += 0
        if Y >=0.99:
            self.OverFlow()
        else:    
            Co = min(180,(1.5*L+5)/(1-Y))  #按照韦伯斯特延误最小优化模型计算出的周期长,最大周期时长设定了阈值180
            Ge = Co-L  #有效绿灯时间
            total_lamda = Ge/Co #总绿信比


            ##计算各相位流量比、绿信比和有效绿灯时间、显示绿灯时间
            y = []
            split = []
            rate = []
            saturation = []
            green = []
            for i in range(self.phase):
                y.append(Ge*int(flow[i])/(int(s2[i])*Y))
                
            ##考虑行人流量
        
            
            if length3<=3:
                y_min1 = 3.2+0.27*non_auto1*Co/3600+length1/1.2
            else:
                y_min1 = 3.2+(2.7/length3)*non_auto1*Co/3600+length1/1.2
                
            if length4<=3:
                y_min2 = 3.2+0.27*non_auto2*Co/3600+length2/1.2
            else:
                y_min2 = 3.2+(2.7/length4)*non_auto2*Co/3600+length2/1.2
            
            
            if self.phase == 2:  ##HCM2010行人最小绿灯时间需求
                y2 = [max(y[0],y_min1),max(y[1],y_min2)]
                
            if self.phase == 3:
                y2 = [max(y[0],y_min1),max(y[1],y_min2),y[2]]    ##先左转相位后直行相位
               
            if self.phase == 4:
                y2 = [max(y[0],y_min1),y[1],max(y[2],y_min2),y[3]]    ##先左转相位后直行相位
            
            
            for i in range(self.phase):
                split.append(total_lamda*int(flow[i])/(int(s2[i])*Y))
                rate.append(int(flow[i])/(int(s2[i])))
                saturation.append(rate[i]/split[i])
                green.append(y2[i]-yellow+loss1+loss2)
            for i in range(self.phase):
                if green[i]<=5:
                    self.d = wx.StaticText(self.panel,-1,"❌注意：相位流量比过小，请调整相位数",(600,180))  
                    self.d.SetForegroundColour('red')
        
                 
                    
                
         
            
            if max(saturation) >= 0.95:
                self.OverFlow()
            else:
                Co = self.phase*(yellow+allred)
             ##显示各相位有效绿灯时间、显示绿灯时间和绿信比、流量比
                for i in range(self.phase):
                    self.output[i].SetValue(str(y2[i]))
                    self.green[i].SetValue(str(green[i]))
                    self.phase_lamda[i].SetValue(str(split[i]))  
                    self.flow_rate[i].SetValue(str(rate[i]))
                    #self.saturation_degree[i].SetValue(str(saturation[i]))
                
                    Co += round(green[i])
                ##显示周期参数——总流量比、总损失、周期时长
                self.total_rate.SetValue(str(Y))
                self.total_loss.SetValue(str(L))
                self.cycle_length.SetValue(str(Co))
                
                if non1 <= yellow+allred:
                    non1 = 0
                else:
                    non1 = non1-yellow-allred
                if non2 <= yellow+allred:
                    non2 = 0
                else:
                    non2 = non2-yellow-allred
                
                
                
           
                if self.phase == 2:
                    a = [0,0]
                    p_green = [0,0]
                   
                    p_green[0] = "相位1"+"行人绿灯时间:" +str(round(green[0])-round(length1/1.2))+'(s)'+"行人绿闪时间:"+str(round(length1/1.2)-non1)+'(s)'+"非机动车绿灯时间:"+str(round(green[0]-non1))+'(s)'
                    p_green[1] = "相位2"+"行人绿灯时间:" +str(round(green[1])-round(length2/1.2))+'(s)'+"行人绿闪时间:"+str(round(length2/1.2)-non2)+'(s)'+"非机动车绿灯时间:"+str(round(green[1]-non2))+'(s)'
                    a[0] = "相位1 "+"全红:"+str(allred)+'(s)'+"绿灯:"+str(round(green[0]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[0])-yellow-allred)+'(s)'
                    a[1] = "相位2 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(Co)-round(green[1])-yellow-allred)+'(s)'+"绿灯:"+str(round(green[1]))+'(s),'+"黄灯:"+str(yellow)+'(s)'
                    self.multiText.SetValue("信号配时结果"+'\n'+a[0]+'\n'+p_green[0]+'\n'+p_green[1]+'\n'+a[1])
                    
                    plt.figure(figsize = (60,5))
                    x=["phase2","phase1"]
                    y = [allred,allred]
                    y2 = [round(Co)-round(green[1])-yellow-allred,0]
                    y3 = [green[1],green[0]]
                    y4 = [yellow,yellow]
                    y5 = [0,round(Co)-round(green[0])-yellow-allred]
                    t1 = np.array(y)
                    t2 = np.array(y2)
                    t3 = np.array(y3)
                    t4 = np.array(y4)
                    t5 = np.array(y5)
             
                    t21= list(np.sum([t1,t2],axis=0))
                    t31 = list(np.sum([t21,t3],axis = 0))
                    t41 = list(np.sum([t31,t4],axis = 0))

                    plt.xlim(0,100)
                    plt.barh(x,y,align="center",color="r",label="y")
                    plt.barh(x,y2,left=y,color="r",label="y2")
                    plt.barh(x,y3,left=t21,color="green",label="y3")
                    plt.barh(x,y4,left=t31,color="yellow",label="y4")
                    plt.barh(x,y5,left=t41,color="red",label="y5")
                    plt.tick_params(labelsize=60)
                    plt.legend()

                    plt.savefig('1.jpg')
                    img2=wx.Image('1.jpg',wx.BITMAP_TYPE_ANY).Scale(550,60)
                    show2=wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img2),pos=(600,440))
                    
                if self.phase == 3:
                    a = [0,0,0]
                    p_green = [0,0]
                    p_green[0] = "相位1"+"行人绿灯时间:" +str(round(green[0])-round(length1/1.2))+'(s)'+"行人绿闪时间:"+str(round(length1/1.2)-non1)+'(s)'+"非机动车绿灯时间:"+str(round(green[0]-non1))+'(s)'
                    p_green[1] = "相位2"+"行人绿灯时间:" +str(round(green[1])-round(length2/1.2))+'(s)'+"行人绿闪时间:"+str(round(length2/1.2)-non2)+'(s)'+"非机动车绿灯时间:"+str(round(green[1]-non2))+'(s)'
                    a[0] = "相位1 "+"全红:"+str(allred)+'(s)'+"绿灯:"+str(round(green[0]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[0])-yellow-allred)+'(s)'
                    a[1] = "相位2 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(green[0])+yellow+allred)+'(s)'+"绿灯:"+str(round(green[1]))+'(s),'+"黄灯:"+str(yellow)+'红灯'+str(round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]))+'(s)'
                    a[2] = "相位3 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(Co)-round(green[2])-yellow-allred)+'(s)'+"绿灯:"+str(round(green[2]))+'(s),'+"黄灯:"+str(yellow)+'(s)'
                    self.multiText.SetValue("信号配时结果"+'\n'+a[0]+'\n'+p_green[0]+'\n'+a[1]+'\n'+p_green[1]+'\n'+a[2])
                    
                    plt.figure(figsize = (60,5))
                    x=["phase3","phase2","phase1"]
                    y = [allred,allred,allred]
                    y2 = [round(Co)-round(green[2])-yellow-allred,round(green[0])+yellow+allred,0]
                    y3 = [green[2],green[1],green[0]]
                    y4 = [yellow,yellow,yellow]
                    y5 = [0,round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]),round(Co)-round(green[0])-yellow-allred]
                    t1 = np.array(y)
                    t2 = np.array(y2)
                    t3 = np.array(y3)
                    t4 = np.array(y4)
                    t5 = np.array(y5)
                 
                    t21= list(np.sum([t1,t2],axis=0))
                    t31 = list(np.sum([t21,t3],axis = 0))
                    t41 = list(np.sum([t31,t4],axis = 0))

                    plt.xlim(0,200)
                    plt.barh(x,y,align="center",color="r",label="y")
                    plt.barh(x,y2,left=y,color="r",label="y2")
                    plt.barh(x,y3,left=t21,color="green",label="y3")
                    plt.barh(x,y4,left=t31,color="yellow",label="y4")
                    plt.barh(x,y5,left=t41,color="red",label="y5")
                    plt.legend()
                    plt.tick_params(labelsize=60)
                    plt.savefig('1.jpg')
                    img2=wx.Image('1.jpg',wx.BITMAP_TYPE_ANY).Scale(550,60)
                    show2=wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img2),pos=(600,440))
                    
                if self.phase == 4:
                    a = [0,0,0,0]
                    p_green = [0,0]
                    p_green[0] = "相位1"+"行人绿灯时间:" +str(round(green[0])-round(length1/1.2))+'(s)'+"行人绿闪时间:"+str(round(length1/1.2)-non1)+'(s)'+"非机动车绿灯时间:"+str(round(green[0]-non1))+'(s)'
                    p_green[1] = "相位3"+"行人绿灯时间:" +str(round(green[2])-round(length2/1.2))+'(s)'+"行人绿闪时间:"+str(round(length2/1.2)-non2)+'(s)'+"非机动车绿灯时间:"+str(round(green[2]-non2))+'(s)'
                    a[0] = "相位1 "+"全红:"+str(allred)+'(s)'+"绿灯:"+str(round(green[0]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[0])-yellow-allred)+'(s)'
                    a[1] = "相位2 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(green[0])+yellow+allred)+'(s)'+"绿灯:"+str(round(green[1]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]))+'(s)'
                    a[2] = "相位3 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(green[0])+yellow+round(green[1])+yellow+2*allred)+'(s)'+"绿灯:"+str(round(green[2]))+'(s),'+"黄灯:"+str(yellow)+'(s)'+"红灯:"+str(round(Co)-round(green[2])-3*yellow-3*allred-round(green[0])-round(green[1]))+'(s)'
                    a[3] = "相位4 "+"全红:"+str(allred)+'(s)'+"红灯:"+str(round(Co)-round(green[3])-yellow-allred)+'(s)'+"绿灯:"+str(round(green[3]))+'(s),'+"黄灯:"+str(yellow)+'(s)'
                    self.multiText.SetValue("信号配时结果"+'\n'+a[0]+'\n'+p_green[0]+'\n'+a[1]+'\n'+a[2]+'\n'+p_green[1]+'\n'+a[3])
                    
                    
                    plt.figure(figsize = (60,5))
                    x=["phase4","phase3","phase2","phase1"]
                    y = [allred,allred,allred,allred]
                    y2 = [round(Co)-round(green[3])-yellow-allred,round(green[0])+yellow+round(green[1])+yellow+2*allred,round(green[0])+yellow+allred,0]
                    y3 = [green[3],green[2],green[1],green[0]]
                    y4 = [yellow,yellow,yellow,yellow]
                    y5 = [0,round(Co)-round(green[2])-3*yellow-3*allred-round(green[0])-round(green[1]),round(Co)-round(green[1])-2*yellow-2*allred-round(green[0]),round(Co)-round(green[0])-yellow-allred]
                    t1 = np.array(y)
                    t2 = np.array(y2)
                    t3 = np.array(y3)
                    t4 = np.array(y4)
                    t5 = np.array(y5)
                  
                    t21= list(np.sum([t1,t2],axis=0))
                    t31 = list(np.sum([t21,t3],axis = 0))
                    t41 = list(np.sum([t31,t4],axis = 0))

                    plt.xlim(0,200)
                    plt.barh(x,y,align="center",color="r",label="y")
                    plt.barh(x,y2,left=y,color="r",label="y2")
                    plt.barh(x,y3,left=t21,color="green",label="y3")
                    plt.barh(x,y4,left=t31,color="yellow",label="y4")
                    plt.barh(x,y5,left=t41,color="red",label="y5")
                    plt.legend()
                    plt.tick_params(labelsize=70)
                    plt.savefig('1.jpg')
                    img2=wx.Image('1.jpg',wx.BITMAP_TYPE_ANY).Scale(550,60)
                    show2=wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img2),pos=(600,440))


if __name__ == '__main__':  
    app = wx.PySimpleApp()  
    frame = CrossingSignalCalculater()  
    frame.Show()  
    app.MainLoop() 
