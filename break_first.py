import webbrowser
import time
total=3
start=1
print("This program started on "+time.ctime())
while(start <= total):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=Mu74UmFBAq8&list=PLillGF-RfqbbpWowfjk9_Vv8XUuTBFPut")
    start=start+1
