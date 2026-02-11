#1
def findsquare(n):
  return n*n
#2  
def findcube(n):
  return n*n*n
#3
def finddouble(n):
    return n * 2
#4
def findtriple(n):
    return n * 3
#5
def findpower(n, p):
    return n ** p
#6
def iseven(n):
    return n % 2 == 0
#6
def isodd(n):
    return n % 2 != 0
 
#7
def login(username, password):
    if username == "abc" and password == "1234":
        return "Login successful"
    else:
        return "Invalid username or password"
#8
def check_username(user):
    return len(user) >= 4
#9
def check_password_length(pwd):
    return len(pwd) >= 6
