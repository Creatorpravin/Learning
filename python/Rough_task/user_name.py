import subprocess

def add_user():

    username_cmd = "whoami"
    username = "praveen"
    

    user = subprocess.Popen(username_cmd, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, universal_newlines=True)
    user_name = user.communicate()
    print(user_name)
    if user_name[0] != username:
     print(user_name[0])
     #subprocess.Popen("./adduser", shell=True, stdout=subprocess.PIPE,
      #                      stderr=subprocess.PIPE, universal_newlines=True)

add_user()