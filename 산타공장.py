q = int(input())

class Node():
    def __init__(self, id, weight):
        self.id = id
        self.w = weight
        self.front = None
        self.back = None
    
class Conveyor():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def input_item(self, n : Node):
        if self.head == None:
            self.head = n
            self.tail = n
        else :
            self.tail.back = n
            n.front = self.tail
            self.tail = n
        
    def w_max(self, m_weight):

        if self.head == None:
            return -1, 0
        elif self.head.w > m_weight and self.head != self.tail:
            self.tail.back = self.head
            self.head.front = self.tail
            self.tail = self.head
            self.head = self.head.back
            self.head.front = None
            self.tail.back = None

            #temp = self.head
            #while temp != None:
            #   print(temp.id)
            #   temp = temp.back

            return -1, 0
        else :
            id =self.head.id
            w = self.head.w

            self.head = self.head.back
            if self.head != None:
                self.head.front = None
            return id,w
    
    def r_id(self, remove_id):
        temp = self.head

        while temp != None:
            if temp.id == remove_id:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return remove_id

                if temp.front != None:
                    temp.front.back = temp.back
                if temp.back != None:
                    temp.back.front = temp.front
                
                return remove_id
            else :
                temp = temp.back
        
        return -1
    
    def f_id(self, find_id):
        temp = self.head

        while temp != None:
            if temp.id == find_id:
                self.tail.back = self.head
                self.head.front = self.tail
                self.head = temp
                self.tail = temp.front
                self.tail.back = None
                self.head.front = None
                return find_id
            else :
                temp = temp.back
        return -1
    
    def b_num(self, con):
        if con.head == None:
            return 

        if self.tail == None:
            self.head = con.head
            self.tail = con.tail
        else :
            self.tail.back = con.head
            con.head.front = self.tail
            self.tail = con.tail

velts =[]
Ids = dict()
liveCon = []

for i in range(q):
    cmd = input().split()
    
    if cmd[0] == '100':
        n = int(cmd[1])
        m = int(cmd[2])
        cmd = cmd[3:]
        IDs = cmd[:len(cmd)//2]
        Ws = cmd[len(cmd)//2:]
        lens = n//m
        for j in range(m):
            con = Conveyor()
            for k in range(lens):
                con.input_item(Node(int(IDs[j*lens + k]), int(Ws[j*lens + k])))
                Ids[int(IDs[j*lens + k])] = j
            velts.append(con)
            liveCon.append(j)
    elif cmd[0] == '200':
        w_max = int(cmd[1])
        ans = 0
        for k in velts:
            if k != None:
                id, w = k.w_max(w_max)
                if id != -1:
                    ans += w
                    del Ids[id]
        print(ans)
    elif cmd[0] == '300':
        r_id = int(cmd[1])
       
        if r_id in Ids:
            print(velts[liveCon[Ids[r_id]]].r_id(r_id))
            del Ids[r_id]
        else :
            print(-1)
    elif cmd[0] == '400':
        f_id = int(cmd[1])
       
        if f_id in Ids:
            velts[liveCon[Ids[f_id]]].f_id(f_id)
            print(liveCon[Ids[f_id]]+1)
        else :
            print(-1)
    elif cmd[0] == '500':
        b_num = int(cmd[1]) - 1
        if velts[b_num] == None:
            print(-1)
            continue
        n = len(velts)
        ans = (b_num +1)%n
        while velts[ans] == None:
            ans = (b_num +1)%n
        velts[ans].b_num(velts[b_num])
        velts[b_num] = None
        liveCon[b_num] = ans
        print(b_num+1)
    """
    for j in range(len(velts)):
        print(j)
        if velts[j] == None :
            print("None")
        else:
            temp = velts[j].head
            while temp != None:
                print(temp.id)
                temp = temp.back
    
    """