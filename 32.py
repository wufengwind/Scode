from tkinter import *
#from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os
#from codenum import *
'''
app=Tk()
app.withdraw()
app.title('代码统计器')
Label(app,text="浏览：").pack()
file_path=filedialog.askopenfilename
app.mainloop()
'''
def file_name(user_dir):
    file_list=list()
    for root,dirs,files in os.walk(user_dir):
        for file in files:
            files=os.path.splitext(file)[1]
            if files==".py" or files==".c" or files==".cpp" or files==".html" or files==".css" or files==".js" or files==".php" or files==".java" or files==".go" or files==".pyw" or files==".sh" or files==".swift" or files==".kt" or files==".sql" or files==".rs" or files==".cs" or files==".Designer" or files==".class" or files==".h":             
                file_list.append(os.path.join(root,file))
    return file_list
def rows(filess):
#print(filess)
    sum=0
    flag=False
    flag_1=False
    flag_2=False
    flag_4=False
    for file in filess:
        with open(file,'rb') as f:
            for file_line in f:
                file_line=file_line.strip()
                if file_line==b'':
                    pass
                elif file_line.startswith(b'--'):
                    pass
                elif file_line.startswith(b'#') and os.path.splitext(file)[1]=='.py':
                    pass
                elif file_line.startswith(b'//'):
                    pass
                elif file_line.startswith(b'///'):
                    pass
                elif file_line.startswith(b"'''") and not flag:
                    flag=True
                elif flag==True:
                    if file_line.endswith(b"'''"):
                        flag=False
                elif file_line.startswith(b'"""') and not flag_1:
                    flag_1=True
                elif flag_1==True:
                    if file_line.endswith(b'"""'):
                        flag_1=False
                elif file_line.startswith(b'/*') and file_line.endswith(b'*/'):
                    pass
                elif file_line.startswith(b'/*') and not flag_2 and not file_line.endswith(b'*/'):
                    flag_2=True
                elif flag_2==True:
                    if file_line.endswith(b'*/') and not file_line.startswith(b'/*'):
                        flag_2=False  
                elif file_line.startswith(b'<!--') and file_line.endswith(b'-->'):
                    pass
                elif file_line.startswith(b"<!--") and not flag_4 and not file_line.endswith(b'-->'):
                    flag_4=True
                elif flag_4==True:
                    if file_line.endswith(b"-->") and not file_line.startswith(b'<!--'):
                        flag_4=False
                else:
                    sum+=1
            #sum+=len(f.readlines())
    return sum
def test():
    files.delete('1.0',END)
    count=2.0
    path=project.get()
    getFiles=file_name(path)
    #allFiles.set(getFiles)
    files.insert(1.0,"所包含程序文件:\n")
    for i in getFiles:
        files.insert(count,i+"\n")
        count+=1.0
    display.set(rows(getFiles))
def select():
    path_=askdirectory()
    path.set(path_)
    #print(path)
root=Tk()
root.title("Scode")
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
ww=320
wh=500
x=(sw-ww)/2
y=(sh-wh)/2
root.geometry("%dx%d+%d+%d"%(ww,wh,x,y))
path=StringVar()
Label(root,text="工程路径：").grid(row=0,column=0)
project= Entry(root,textvariable=path,width=30)
project.grid(row=0,column=1)
Button(root,text="浏览",command=select).grid(row=0,column=2)
#print(project.get())
Button(root,text="统计",command=test).grid(row=1,column=2)
Label(root,text="代码行数：").grid(row=1,column=0)
display=StringVar()
sum=Entry(root,textvariable=display,width=30)
sum.grid(row=1,column=1)
#Text(root).grid(row=3,column=0,rowspan=8,columnspan=3)
#allFiles=StringVar()
files=Text(root,width=42,height=33)
files.grid(row=3,column=0,rowspan=8,columnspan=3)
root.mainloop()
    
