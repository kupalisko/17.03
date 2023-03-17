#vstup = input("Zadaj adresu")
vstup = "https://login:p455w0rd@admin.server.sk/12345"
vstup = "https://www.w3schools.com/python/ref_string_split.asp"
path = []
dictt = {
    "protocol":"-",
    "server":"-",
    "login":"-",
    "password":"-",
    "path":"-",
    "query": {
    }
}


if vstup[0:4] == "http":
    dictt["protocol"]  = "http"
    cislo = 4
else: print("Chybna url")

if vstup[0:5] == "https":
    dictt["protocol"]  = "https"
    cislo = 5
else: print("Chybna url")

vstup = vstup[cislo+3:]

if vstup[:5] == "login":
    vstup = vstup[5:]
    if vstup[0] == "@":
        login = vstup.split(".",1)
        login = login[0]
    if vstup[0] == ":":
        password = vstup.split("@",1)
        password = password[0]
        password = password[1:]
        vstup = vstup[len(password)+1:]
        login = vstup.split(".",1)
        login = login[0]
        login = login[1:]
        vstup = vstup[len(login)+1:]   
        dictt["login"] = login
        dictt["password"] = password


full = vstup.split("/",1)
server = full[0]
if server[1]==".":server = server[1:]
dictt["server"] = server

dictt["path"] = full[1]

print(vstup)
print(dictt)