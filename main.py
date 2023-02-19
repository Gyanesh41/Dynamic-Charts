import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

argdict={'charttype':"line",'library':"Matplotlib",        
         'data':None,'x':None,'y':None,'hue':None,'color':None,
         'title':None,'xtick':None,'ytick':None,
         'rotate_x':None,'rotate_y':None,'xlim':None,
         'ylim':None,'savename':"C:/Users/rugyr/OneDrive/Pictures/fig.png"}

def dynamic_chart(argdict):
    preinputs(argdict);
    if argdict.get('library')=="seaborn":
        charttype=input("[ 'heatmmap' , 'count' , 'bar' , 'hist' , 'scatter' ]\nPlease provide chart type : ")
        argdict.update([('charttype',charttype)])
        seaborn(argdict);
        
    elif argdict.get('library')=="matplotlib":
        charttype=input("[ 'pie' , 'count' , 'bar' , 'hist' , 'scatter' ]\nPlease provide chart type : ")
        argdict.update([('charttype',charttype)])
        df=argdict.get("data")
        matplotlib(argdict,df);
    else: print("Error : Wrong Library");
    addfeature=input("Do you want to use additional features [y/n] : ")
    if addfeature=="y":
        postinputs(argdict)
    elif  addfeature=="n":print("")
    else:
        print("Error: Add. feature : Wrong input")
        exit()
    plt.title(argdict.get('title'))
    plt.xticks(rotation=argdict.get('rotate_x'));
    plt.yticks(rotation=argdict.get('rotate_y'));
    plt.savefig(argdict.get("savename"));
    plt.show();
    
def seaborn(argdict):
    if argdict.get('charttype')=="scatter":
        scattersns(argdict);
    elif argdict.get('charttype')=="line":
        linesns(argdict);
    elif argdict.get('charttype')=="count":
        countsns(argdict)
    elif argdict.get('charttype')=="hist":
        histsns(argdict)
    elif argdict.get('charttype')=="bar":
        barsns(argdict)
    elif argdict.get('charttype')=="heatmap":
        heatsns(argdict)
    else:
        print("Error : Wrong Charttype")
    
def matplotlib(argdict,df):
    if argdict.get('charttype')=="pie":
        piemat(argdict,df);
    elif argdict.get('charttype')=="scatter":
        scattermat(argdict,df);
    elif argdict.get('charttype')=="count":
        countmat(argdict,df)
    elif argdict.get('charttype')=="line":
        linemat(argdict,df);
    elif argdict.get('charttype')=="hist":
        histmat(argdict,df);
    elif argdict.get('charttype')=="bar":
        barmat(argdict,df);
    else:
        print("Error : Wrong Charttype")
    plt.xlabel(argdict.get('x')) 
    plt.ylabel(argdict.get('y'))
    
def scattersns(argdict):
    x=input("Please provide x-axis column : ")
    y=input("Please provide y-axis column : ")
    marker=input("Please provide marker you want to use : ")
    sns.scatterplot(data=argdict.get('data'),x=x,y=y,marker=marker);
    
def linesns(argdict):
    x=input("Please provide the column on x-axis column : ")
    y=input("Please provide the column on y-axis column : ")
    marker=input("Please provide marker you want to use : ")
    sns.lineplot(data=argdict.get('data'),x=x,y=y,marker=marker);
    
def heatsns(argdict):
    anot=input("Please give t(true) or f(false) if you want annotation or not : ")
    if anot=='t':anot=True;
    elif anot=='f':anot=False;
    else:print("Wrong Annotation");
    sns.heatmap(data=argdict.get('data').corr(),annot=anot)
    
def countsns(argdict):
    x=input("Please provide the column to be counted : ")
    sns.countplot(data=argdict.get('data'),x=x)
       
def histsns(argdict):
    x=input("Please provide the column on x-axis : ")
    y=input("Please provide the column on y-axis : ")
    argdict.update([('x',x),('y',y)])
    if y=="":y=None
    sns.histplot(data=argdict.get('data'),x=x,y=y)

def barsns(argdict):
    x=input("Please provide the column on x-axis : ")
    y=input("Please provide the column on y-axis : ")
    argdict.update([('x',x),('y',y)])
    sns.barplot(data=argdict.get('data'),x=x,y=y)

def piemat(argdict,df):
    x=input("Please provide column you want to plot : ")
    count=df[x].value_counts().reset_index()
    autopct="%1.1f%%"
    plt.pie(x=count[x],labels=count['index'],autopct=autopct)

def countmat(argdict,df):
    x=input("Please provide the column on x-axis : ")
    countdf=df[x].value_counts().reset_index()
    argdict.update([('x',x),('y','Count')])
    plt.bar(countdf["index"],countdf["Weather"])

def linemat(argdict,df):
    x=input("Please provide the column on x-axis : ")
    y=input("Please provide the column on y-axis : ")
    marker=input("Please provide the marker you want to use : ")
    x_values=list(df[x].unique())
    x_values.sort()
    y_values=[]
    for i in x_values:
        y_values.append(df.loc[df[x]==i,y].mean())
    plt.plot(x_values,y_values,marker=marker)
    argdict.update([('x',x),('y',y)])

def histmat(argdict,df):
    x=input("Please provide the column on x-axis : ")
    plt.hist(df[x],edgecolor='k')
    argdict.update([('x',x)])
    
def barmat(argdict,df):
    x=input("Please provide the column on x-axis : ")
    y=input("Please provide the column on y-axis : ")
    plt.bar(df[x],height=df[y])
    argdict.update([('x',x),('y',y)])

def scattermat(argdict,df):
    x=input("Please provide the column on x-axis : ")
    y=input("Please provide the column on y-axis : ")
    marker=input("Please provide marker you want to use : ")
    plt.scatter(df[x],df[y],marker=marker)  
    argdict.update([('x',x),('y',y)])

def preinputs(argdict):
    library=input("Please provide the library you want to use ['matplotlib'/'seaborn'] : ")
    path=input("Please provide the path of dataset : ")
    data=pd.read_csv(path)
    argdict.update([('library',library),('data',data)])
    
    
def postinputs(argdict):
    title=input("Please provide the title : ")
    rotation=input("Do you want to rotate labels [y/n] : ")
    rotate_x=None;rotate_y=None;
    if rotation=="y":
        rotate_x=int(input("Provide rotation angle of x-labels : "))
        rotate_y=int(input("Provide rotation angle of y-labels : "))
    filename=input("Please provide the path where you want to save figure : ")
    if filename=="":filename="C:/Users/rugyr/OneDrive/Pictures/fig.png";
    argdict.update([('title',title),('rotate_y',rotate_y),('rotate_x',rotate_x),('savename',filename)])
    
dynamic_chart(argdict)
