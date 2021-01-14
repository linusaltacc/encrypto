crypt = input("Enter something to encrypt :")

cipher = {"A":"X","a":"x","B":"Y","b":"y","C":"Z","c":"z","D":"A","d":"a","E":"B","e":"b","F":"C","f":"c","G":"D","g":"d","H":"E","h":"e","I":"F","i":"f","J":"G","j":"g","K":"H","k":"h","L":"I","l":"i","M":"J","m":"j","N":"K","n":"k","O":"L","o":"l","P":"M","p":"m","Q":"N","q":"n","R":"O","r":"o","S":"P","s":"p","T":"Q","t":"q","U":"R","u":"r","V":"S","v":"s","W":"T","w":"t","X":"U","x":"u","Y":"V","y":"v","Z":"W","z":"w", " " : " ", "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "0": "0", "@" : "%", "#": "&", "%" : "@"}

def encrypt():
    result = ''
    for x in crypt:
        result = result + cipher[x]
    print(result)

encrypt()
