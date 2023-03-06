import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

argdict={'library':None,'data':None,'charttype':None,
         'x':None,'y':None,'color':None,'marker':None,'bins':None,'title':None,
         'xticks':None,'yticks':None,'rotate_x':None,'xticklabel':None,'yticklabel':None,
         'rotate_y':None,'xlim':None,'ylim':None,'savename':None}

def dynamic_chart(argdict):
    preinputs(argdict)
    if argdict.get('library')=="seaborn":
        charttype=input("[ 'heatmmap' , 'count' , 'bar' , 'hist' , 'line' ,'scatter' ]\nPlease provide chart type : ")    
        argdict.update([('charttype',charttype)])
        inplot_feature(argdict)
        seaborn(argdict)
    elif argdict.get('library')=="matplotlib":
        charttype=input("[ 'pie' , 'count' , 'bar' , 'hist' , 'line' , 'scatter' ]\nPlease provide chart type : ")
        argdict.update([('charttype',charttype)])
        inplot_feature(argdict)
        df=argdict.get("data")
        matplotlib(argdict,df)
    else: print("Error : Wrong Library");exit()
    postinputs(argdict)   
    filename=input("Please provide the path where you want to save figure with figure name and (extension): ")
    if filename=="":filename="C:/Users/rugyr/OneDrive/Pictures/fig.png";
    argdict.update([('savename',filename)])
    plt.title(argdict['title'])
    plt.xlabel(argdict['x'])
    plt.ylabel(argdict['y'])
    plt.xticks(ticks=argdict['xticks'],labels=argdict['xticklabel'],rotation=argdict['rotate_x'])
    plt.yticks(ticks=argdict['yticks'],labels=argdict['yticklabel'],rotation=argdict['rotate_y'])
    plt.tight_layout()
    plt.savefig(argdict.get('savename'))
    plt.show()

def preinputs(argdict):
    library=input("Please provide the library you want to use ['matplotlib'/'seaborn'] : ")
    path=input("Please provide the path of dataset : ")
    data=pd.read_csv(path)
    argdict.update([('library',library),('data',data)])

def inplot_feature(argdict):
    color=sns.color_palette(palette='bright');x=None;y=None;marker=None;bins=None
    if argdict['charttype'] not in ['pie','heatmap']:
        askcolor=input("Do you want to use your colors [y/n] : ")
        if askcolor=="y":color=input("[ 'blue':'b' , 'red':'r' , 'black':'k' , 'green':'g', 'if other color, provide name in small letter' ]\nPlease provide color : ")
        elif askcolor=="n":
            if argdict['charttype'] in ["line","scatter"]:color="blue"
        else :print("Error : Wrong Input");exit()
    if argdict['charttype'] in ['pie','count']:
        x=input('Please provide column for plot : ')
    elif argdict['charttype']=='bar':
        x=input("Please provide column for x-axis : ")
        y=input("Please provide column for y-axis : ")
    elif argdict['charttype']  in ['scatter','line']:
        x=input("Please provide column for x-axis : ")
        y=input("Please provide column for y-axis : ")
        marker=input("Please provide marker you want to use : ")
    elif argdict['charttype']=='hist':
        x=input('Please provide column for plot : ')
        askbin=input("Do you want to provide no. of bins [y/n] : ")
        if askbin=='y':bins=int(input("Please provide no. of bins : "))
        elif askbin=='n':print("")
        else:print("Error : wrong input");exit()
    argdict.update([('x',x),('y',y),('color',color),('bins',bins),('marker',marker)])
    autotick(argdict)
    
def postinputs(argdict):
    title=None;rotate_x=None;rotate_y=None;xtick=None;ytick=None;ylim=None;xlim=None
    access=input('Do you want use adititonal feature [y/n] :')
    while(access=='y'):
        if argdict['charttype']=='pie':addfeature=input("['title'] \nPlease select additional feature : ")
        elif argdict['charttype']=='heatmap':addfeature=input("['title','rotate_x','rotate_y']\nPlease select additional feature : ")
        else:addfeature=input("['title','rotate_x','rotate_y','xtick','ytick','xlimit','ylimit']\nPlease select additional feature : ")
        if (addfeature=='title'):title=input("Please provide the title for plot : ")
        elif (addfeature=='rotate_x') and (argdict['charttype']!='pie'):rotate_x=int(input("Please provide the angle of rotation for xlabels : "))
        elif (addfeature=="rotate_y") and (argdict['charttype']!='pie'):rotate_y=int(input("Please provide the angle of rotation for ylabels : "))
        elif (addfeature=="xtick") and (argdict['charttype'] not in ['pie','heatmap']):xticks(argdict)
        elif (addfeature=="ytick") and (argdict['charttype'] not in ['pie','heatmap']):yticks(argdict)
        elif (addfeature=="xlimit") and (argdict['charttype'] not in ['pie','heatmap']):xlimit(argdict)
        elif (addfeature=="ylimit") and (argdict['charttype'] not in ['pie','heatmap']):ylimit(argdict)
        else:print("Error : Wrong Feature");exit()
        access=input("Do you want to use more addtional features [y/n] : ")
    argdict.update([('title',title),('rotate_x',rotate_x),('rotate_y',rotate_y),('xtick',xtick),('ytick',ytick),('ylim',ylim),('xlim',xlim)])

def seaborn(argdict):
    if argdict.get('charttype')=="scatter":scattersns(argdict)
    elif argdict.get('charttype')=="line":linesns(argdict)
    elif argdict.get('charttype')=="count":countsns(argdict)
    elif argdict.get('charttype')=="hist":histsns(argdict)
    elif argdict.get('charttype')=="bar":barsns(argdict)
    elif argdict.get('charttype')=="heatmap":heatsns(argdict)
    else:print("Error : Wrong Charttype");exit()
    
def matplotlib(argdict,df):
    if argdict.get('charttype')=="pie":piemat(argdict,df);
    elif argdict.get('charttype')=="scatter":scattermat(argdict,df);
    elif argdict.get('charttype')=="count":countmat(argdict,df)
    elif argdict.get('charttype')=="line":linemat(argdict,df);
    elif argdict.get('charttype')=="hist":histmat(argdict,df);
    elif argdict.get('charttype')=="bar":barmat(argdict,df);
    else:print("Error : Wrong Charttype");exit()
    plt.xlabel(argdict['x']) 
    plt.ylabel(argdict['y'])
    
def scattersns(argdict):
    sns.scatterplot(data=argdict.get('data'),x=argdict['x'],y=argdict['y'],marker=argdict['marker'],color=argdict['color']);
    
def linesns(argdict):
    sns.lineplot(data=argdict.get('data'),x=argdict['x'],y=argdict['y'],marker=argdict['marker'],color=argdict['color']);
    
def heatsns(argdict):
    anot=input("Please give t(true) or f(false) if you want annotation or not : ")
    if anot=='t':anot=True;
    elif anot=='f':anot=False;
    else:print("Wrong Annotation");exit()
    sns.heatmap(data=argdict['data'].corr(),annot=anot)
    
def countsns(argdict):
    sns.countplot(data=argdict['data'],x=argdict['x'],color=argdict['color'])
       
def histsns(argdict):
    sns.histplot(data=argdict['data'],x=argdict['x'],color=argdict['color'],bins=argdict['bins']);argdict.update([('y','Frequency')])

def barsns(argdict):
    sns.barplot(data=argdict['data'],x=argdict['x'],y=argdict['y'],color=argdict.get('color'))

def piemat(argdict,df):
    count=df[argdict['x']].value_counts().reset_index()
    autopct="%1.1f%%"
    plt.pie(x=count[argdict['x']],labels=count['index'],autopct=autopct)
    argdict.update([('x',None)])

def countmat(argdict,df):
    countdf=df[argdict['x']].value_counts().reset_index()
    argdict.update([('y','Count')])
    plt.bar(countdf["index"],countdf["Weather"],color=argdict['color'])

def linemat(argdict,df):
    x_values=list(df[argdict['x']].unique())
    x_values.sort();y_values=[]
    for i in x_values:y_values.append(df.loc[df[argdict['x']]==i,argdict['y']].mean())
    plt.plot(x_values,y_values,marker=argdict['marker'],color=argdict['color'])
    
def histmat(argdict,df):
    plt.hist(df[argdict['x']],edgecolor='k',color=argdict['color'],bins=argdict['bins']);argdict.update([('y','Frequency')])   
    
def barmat(argdict,df):
    plt.bar(df[argdict['x']],height=df[argdict['y']],color=argdict['color'])

def scattermat(argdict,df):
    plt.scatter(df[argdict['x']],df[argdict['y']],marker=argdict['marker'],c=argdict.get('color'))  

def autotick(argdict):
    if argdict['charttype'] not in ['pie','heatmap']:
        if type(argdict['data'][argdict['x']][1])==str:
            total=argdict['data'][argdict['x']].unique()
            if len(total)>20:
                index = round(len(total)/4);labellist=[]
                labelindex = 0;lindex=[]
                for i in range (5): 
                    if labelindex <= len(total):
                        labellist.append(total[labelindex])
                        lindex.append(labelindex)
                        labelindex=labelindex+index
                    else:
                        labellist.append(total[len(total)-1])
                        lindex.append(len(total)-1)
                argdict.update([('xticks',lindex),('xticklabel',labellist)])

def xticks(argdict):
    xtickno=int(input("Please provide no. of xlabels you want : "))
    xtick=ticklabels(xtickno);print(xtick[1],"/n",xtick[0]);
    argdict.update([('xticklabel',xtick[0]),('xticks',xtick[1])])
    
def yticks(argdict):
    ytickno=int(input("Please provide no. of ylabels you want : "))
    ytick=ticklabels(ytickno);print(ytick[1],"/n",ytick[0]);
    argdict.update([('yticklabel',ytick[0]),('yticks',ytick[1])])

def ticklabels(tickno):
    labellist=[];labelindex=[]
    for i in range(tickno):
        tick=int(input("Please provide tick"+str(i+1)+" : "))
        labels=input("Please provide label "+str(i+1)+" : ")
        labelindex.append(tick)
        labellist.append(labels)
    return [labellist,labelindex]
        
def xlimit(argdict):
    lowlim=float(input("Please provide lower limit of x-axis : "))
    uplim=float(input("Please provide upper limit of x-axis : "))
    xlimit=(lowlim,uplim);argdict.update([('xlim',xlimit)]);plt.xlim(xlimit)

def ylimit(argdict):
    lowlim=float(input("Please provide lower limit of y-axis : "))
    uplim=float(input("Please provide upper limit of y-axis : "))
    ylimit=(lowlim,uplim);argdict.update([('ylim',ylimit)]);plt.ylim(ylimit)

dynamic_chart(argdict)
