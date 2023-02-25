import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

argdict={'library':None,'data':None,'charttype':None,
         'x':None,'y':None,'hue':None,'color':None,
         'title':None,'xtick':None,'ytick':None,
         'rotate_x':None,'rotate_y':None,'xlim':None,'ylim':None,'savename':None}

def dynamic_chart(argdict):
    preinputs(argdict)
    if argdict.get('library')=="seaborn":
        charttype=input("[ 'heatmmap' , 'count' , 'bar' , 'hist' , 'scatter' ]\nPlease provide chart type : ")    
        argdict.update([('charttype',charttype)])
        inplot_feature(argdict)
        seaborn(argdict)
        
    elif argdict.get('library')=="matplotlib":
        charttype=input("[ 'pie' , 'count' , 'bar' , 'hist' , 'scatter' ]\nPlease provide chart type : ")
        argdict.update([('charttype',charttype)])
        inplot_feature(argdict)
        df=argdict.get("data")
        matplotlib(argdict,df)
    else: print("Error : Wrong Library")
    
    addfeature=input("Do you want to use additional features [y/n] : ")
    if addfeature=="y":postinputs(argdict)
    elif addfeature=='n':print("");
    else:print("Error : Wrong Input")   
    filename=input("Please provide the path where you want to save figure with figure name and (extension): ")
    if filename=="":filename="C:/Users/rugyr/OneDrive/Pictures/fig.png";
    argdict.update([('savename',filename)])
    plt.tight_layout()
    plt.savefig(argdict.get('savename'))
    plt.show()

def preinputs(argdict):
    library=input("Please provide the library you want to use ['matplotlib'/'seaborn'] : ")
    path=input("Please provide the path of dataset : ")
    data=pd.read_csv(path)
    argdict.update([('library',library),('data',data)])

def inplot_feature(argdict):
    color=sns.color_palette(palette='bright');x=None;y=None;
    askcolor=input("Do you want to use your colors [y/n] : ")
    if askcolor=="y":color=input("[ 'blue':'b' , 'red':'r' , 'black':'k' , 'green':'g', 'if other color, provide name in small letter' ]\nPlease provide color : ")
    if argdict['charttype'] in ['pie','hist','count']:
        x=input('Please provide column for plot : ')
    elif argdict['charttype'] in ['bar','scatter','line']:
        x=input("Please provide column for x-axis : ")
        y=input("Please provide column for y-axis : ")
    argdict.update([('x',x),('y',y),('color',color)])     
    
def postinputs(argdict):
    title=input("Please provide the title : ")
    rotation=input("Do you want to rotate labels [y/n] : ")
    rotate_x=None;rotate_y=None;
    if rotation=="y":
        rotate_x=int(input("Provide rotation angle of x-labels : "))
        rotate_y=int(input("Provide rotation angle of y-labels : "))
    elif rotation=='n':print("");
    else:print("Error : Wrong Input")   
    argdict.update([('title',title),('rotate_y',rotate_y),('rotate_x',rotate_x)])
    plt.title(argdict['title'])
    plt.xticks(rotation=argdict['rotate_x'])
    plt.yticks(rotation=argdict['rotate_y'])
    
def seaborn(argdict):
    if argdict.get('charttype')=="scatter":scattersns(argdict)
    elif argdict.get('charttype')=="line":linesns(argdict)
    elif argdict.get('charttype')=="count":countsns(argdict)
    elif argdict.get('charttype')=="hist":histsns(argdict)
    elif argdict.get('charttype')=="bar":barsns(argdict)
    elif argdict.get('charttype')=="heatmap":heatsns(argdict)
    else:print("Error : Wrong Charttype")
    
def matplotlib(argdict,df):
    if argdict.get('charttype')=="pie":piemat(argdict,df);
    elif argdict.get('charttype')=="scatter":scattermat(argdict,df);
    elif argdict.get('charttype')=="count":countmat(argdict,df)
    elif argdict.get('charttype')=="line":linemat(argdict,df);
    elif argdict.get('charttype')=="hist":histmat(argdict,df);
    elif argdict.get('charttype')=="bar":barmat(argdict,df);
    else:print("Error : Wrong Charttype")
    plt.xlabel(argdict['x']) 
    plt.ylabel(argdict['y'])
    
def scattersns(argdict):
    marker=input("Please provide marker you want to use : ")
    sns.scatterplot(data=argdict.get('data'),x=argdict['x'],y=argdict['y'],marker=marker,color=argdict['color']);
    
def linesns(argdict):
    marker=input("Please provide marker you want to use : ")
    sns.lineplot(data=argdict.get('data'),x=argdict['x'],y=argdict['y'],marker=marker,color=argdict['color']);
    
def heatsns(argdict):
    anot=input("Please give t(true) or f(false) if you want annotation or not : ")
    if anot=='t':anot=True;
    elif anot=='f':anot=False;
    else:print("Wrong Annotation");
    sns.heatmap(data=argdict['data'].corr(),annot=anot)
    
def countsns(argdict):
    sns.countplot(data=argdict['data'],x=argdict['x'],color=argdict['color'])
       
def histsns(argdict):
    sns.histplot(data=argdict['data'],x=argdict['x'],color=argdict['color']);argdict.update([('y','Frequency')])

def barsns(argdict):
    sns.barplot(data=argdict['data'],x=argdict['x'],y=argdict['y'],color=argdict.get('color'))

def piemat(argdict,df):
    x=input("Please provide column you want to plot : ")
    count=df[x].value_counts().reset_index()
    autopct="%1.1f%%"
    plt.pie(x=count[x],labels=count['index'],autopct=autopct)

def countmat(argdict,df):
    countdf=df[argdict['x']].value_counts().reset_index()
    argdict.update([('y','Count')])
    plt.bar(countdf["index"],countdf["Weather"],color=argdict['color'])

def linemat(argdict,df):
    marker=input("Please provide the marker you want to use : ")
    x_values=list(df[argdict['x']].unique())
    x_values.sort()
    y_values=[]
    for i in x_values:y_values.append(df.loc[df[argdict['x']]==i,argdict['y']].mean())
    plt.plot(x_values,y_values,marker=marker,color=argdict['color'])

def histmat(argdict,df):
    plt.hist(df[argdict['x']],edgecolor='k',color=argdict['color']);argdict.update([('y','Frequency')])   
    
def barmat(argdict,df):
    plt.bar(df[argdict['x']],height=df[argdict['y']],color=argdict['color'])

def scattermat(argdict,df):
    marker2=input("Please provide marker you want to use : ")
    plt.scatter(df[argdict['x']],df[argdict['y']],marker=marker2,c=argdict.get('color'))  

dynamic_chart(argdict)
