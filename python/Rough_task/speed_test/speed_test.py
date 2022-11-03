# Python program to test
# internet speed
  
import speedtest  


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"  # Get last two decimal pointss
        bytes /= factor
  
  
st = speedtest.Speedtest()

  
option = int(input('''What speed do you want to test:  
  
1) Download Speed  
  
2) Upload Speed  
  
3) Ping 
  
Your Choice: '''))
  
  
if option == 1:  

    a = st.download()  
    print(st.download())  
    print(get_size(a))
    
elif option == 2: 
    b = st.upload()
    print(st.upload())  
    print(get_size(b))

elif option == 3:  
  
    servernames =[]  
  
    st.get_servers(servernames)      
    
    print(st.results.ping)
    
  
else:
  
    print("Please enter the correct choice !") 
