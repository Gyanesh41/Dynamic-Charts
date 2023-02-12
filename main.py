import matplotlib.pyplot as plt;
import pandas as pd;
import seaborn as sns;
def plot(charttype="line",library="Pyplot",
         data=None,x=None,y=None,colors=None,annot=False,bins=None,
         textprops=None,explode=None,xlabels=None,ylabels=None,vmin=-100,vmax=100,edgecolor="black",
         hue=None,title=None,xtick=None,ytick=None,rotate_x=None,rotate_y=None,xlim=None,ylim=None,
         labels=None,autopct=None,save="fig.png"):
    ctrl=0
    if library=="Pyplot" or library=="pyplot":
    
        if charttype=="pie":
            plt.pie(x=x, explode=explode,labels=labels,colors=colors,textprops=textprops,autopct=autopct)
            ctrl=ctrl+1

        elif charttype=="line":
            plt.plot(x,y,colors)

        elif charttype=="bar":
            plt.bar(data=data,x=x,height=y,color=colors)
            
        elif charttype=="hist":
            plt.hist(data=data,x=x,color=colors,edgecolor=edgecolor,width=1,bins=bins,align="left")
            
        elif charttype=="scatter":
            plt.scatter(x=x,y=y,c=colors)
            
        elif charttype=="heatmap":
            plt.imshow(X=data)
            cax = plt.axes([vmin,vmin+vmax/2,(vmin+vmax)/2,vmin/2 +vmax,vmax])
            plt.colorbar(cax=cax)
    
    elif library=="Seaborn" or library=="seaborn":
        if charttype=="line":
            sns.lineplot(data=data,x=x,y=y,c=colors,hue=hue)
            
        elif charttype=="bar":
            sns.barplot(data=data,x=x,y=y,hue=hue,color=colors)
        
        elif charttype=="hist":
            sns.histplot(data=data,x=x,y=y,hue=hue,color=colors)
        
        elif charttype=="heatmap":
            sns.heatmap(data=data,vmin=vmin,vmax=vmax,annot=annot)
            ctrl=ctrl+1
        
        elif charttype=="scatter":
            sns.scatterplot(data=data,x=x,y=y,hue=hue,color=colors)
            
        elif charttype=="countplot":
            sns.countplot(data=data,x=x,y=y,hue=hue,color=colors)
    
    plt.title(title)
    if ctrl==0:
        plt.xlabel(xlabels)
        plt.ylabel(ylabels)
        plt.xticks(xtick,rotation=rotate_x)
        plt.yticks(ytick,rotation=rotate_y)
        plt.xlim(xlim)
        plt.ylim(ylim)
    plt.savefig(save)
    plt.show()

#######################################################################################
df=pd.read_csv("E:\gyanesh\python\Dynamic Chart\Weather Data.csv")
l=["Temp_C","Dew Point Temp_C","Rel Hum_%","Wind Speed_km/h","Visibility_km","Press_kPa"]
plot(charttype="line",library="Seaborn",data=df,x="Temp_C",y="Speed_km/h",annot=True,vmin=-1,vmax=1);