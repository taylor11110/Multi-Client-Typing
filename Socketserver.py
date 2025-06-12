import socket, GenerateStringclass, random

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

userstats = []
userIDs = []
returningIDs = []
global st
st = "test"
track = 0


def generateID():
    tID = random.randrange(1,51)
    if(len(userIDs)>0):
        for e in userIDs: 
            if(tID == e):
                generateID()
    userIDs.append(tID)
    
for i in range(1,3):
    generateID()
    
def retIDmanager(ID):
    if(len(returningIDs)>0):         #limits too much repitition of user IDs
        if(returningIDs[0]!=ID):
            returningIDs.append(ID)
    else:
        returningIDs.append(ID)

        

s.bind(('', 1234))

s.listen(30)
print("IDS ACESSED(initial):", userIDs)

while True:
    cs, addr = s.accept()
    
    bckup = cs.recv(2000)
    codemssg = int.from_bytes(bckup, byteorder='big' , signed=False) 
    
 #   st = GenerateStringclass.yieldString()
    print("action_number:", codemssg)
    
    if(codemssg == 1): #sentence
        cs.send(bytes(st, 'utf-8'))
       
    else:
        if(codemssg >=2 and codemssg <= 52): #send opponent stats
            if(len(returningIDs)>2 and (returningIDs[len(returningIDs)-1])==codemssg-2):
                cs.send(bytes(str(userstats[0]), 'utf-8'))
                print("SERVER SENT STATS (loss)")
            else:
                if(len(returningIDs)>2 and (returningIDs[0])==codemssg-2):
                    cs.send(bytes(str(userstats[len(userstats)-1]), 'utf-8'))
                    print("SERVER SENT STATS (win)")
                else:
                    cs.send(bytes("N/A", 'utf-8'))    
                    retIDmanager(codemssg-2)   
                    print("SERVER STORING:", userstats)
                    print("IDS ACESSED:", userIDs)
                    print("IDS ACESSED(ret):", returningIDs)
        else:
            if(codemssg == 53): #ID
                cs.send(int.to_bytes(userIDs.pop(len(userIDs)-1), byteorder='big'))
            else:
                if(codemssg == 54):
                    cs.send(bytes("reset acknowledged", 'utf-8'))
                    if(track<1):
                        st = GenerateStringclass.yieldString()
                        track+=1
                    else:
                        track = 0
                    returningIDs = []
                else:
                    print("Here's what was recieved:", bckup)
                    userstats.append(bckup.decode('utf-8'))
                

    print(addr)

    cs.close()
s.close()