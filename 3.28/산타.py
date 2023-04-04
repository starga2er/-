class box():
    def __init__(self,id,w) :
        self.id = id
        self.w = w
        self.next =None
        self.prev = None
    
class belt():
    def __init__(self) :
        self.front = None
        self.back = None

    def append(self, n : box):
        if self.front == None:
            self.front = n
            self.back = n
        else:
            self.back.next = n
            n.prev = self.back
            self.back = n
    
    def find(self, id):
        temp = self.front
        while temp != None:
            if temp.id == id :
                return temp
            else :
                temp = temp.next
        return None
    
    def popleft(self):
        if self.front == None:
            return None
        else:
            temp = self.front
            if self.back == self.front:
                self.back = self.front = None
                return temp

            if self.front.next != None:
                self.front = self.front.next
                self.front.prev = None
                temp.next = None
            return temp
    
    def control2(self, w_max):
        if self.front == None :
            return None
        else :
            temp = self.popleft()
            if temp == None :
                return None
            if temp.w <= w_max:
                return temp
            else:
                self.append(temp)
                return None

    def control3(self, r_id):
        temp = self.find(r_id)
        if temp == self.front:

            return self.popleft().id
        elif temp == self.back:
            self.back.prev.next = None
            self.back = self.back.prev
            return temp.id
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            return temp.id
        
    def control4(self, f_id):  
        temp = self.find(f_id)
        if temp != self.front:
            self.front.prev = self.back
            self.back.next = self.front
            self.back = temp.prev
            self.back.next = None
            self.front = temp
            self.front.prev = None
        return temp.id

belts = []
belt_map = []
id_dict = dict()
q = int(input())
for i in range(q):
    cmd = list(map(int,input().split()))

    if cmd[0] == 100 :
        #공장 설립
        n = cmd[1]
        m = cmd[2]
        IDs = cmd[3:3+n]
        Ws = cmd[3+n:]
        len(IDs)
        len(Ws)
        for j in range(m):
            new_belt = belt()
            belt_map.append(j)
            for k in range(n//m):
                new_belt.append(box(IDs[j*(n//m)+k],Ws[j*(n//m)+k]))
                id_dict[IDs[j*(n//m)+k]] = j
            belts.append(new_belt)

    elif cmd[0] == 200 :
        w_max = cmd[1]
        ans = 0
        for b in belts:
            if b == None :
                continue
            temp = b.control2(w_max)
            if temp != None:
                ans += temp.w
                del id_dict[temp.id]
        print(ans)
        # 물건 하차
    elif cmd[0] == 300 :
        f_id = cmd[1]
        if f_id in id_dict:
            if f_id == belts[belt_map[id_dict[f_id]]].control3(f_id):
                del id_dict[f_id]
                print(f_id)
            else :
                print('error 3')
        else :
            print(-1)
        # 물건 제거
    elif cmd[0] == 400 :
        r_id = cmd[1]
        if r_id in id_dict:
            if r_id == belts[belt_map[id_dict[r_id]]].control4(r_id):
                print(belt_map[id_dict[r_id]]+1)
                # del id_dict[r_id]
            else :
                print('error 4')
        else :
            print(-1)
    elif cmd[0] == 500 :
        b_num = cmd[1] - 1
        if belts[b_num] != None:
            if belts[b_num].front == None:
                print(b_num+1)
                continue
            bbelt = belts[b_num]
            belts[b_num] = None
            new_num = (b_num+1)%len(belts)

            while belts[new_num] == None:
                new_num = (new_num+1)%len(belts)

            for l in range(len(belt_map)):
                if belt_map[l] == b_num:
                     belt_map[l] = new_num

            if belts[new_num].front == None :
                belts[new_num] = bbelt
            else :
                belts[new_num].back.next = bbelt.front
                bbelt.front.prev = belts[new_num].back
                belts[new_num].back = bbelt.back
            print(b_num+1)
        else :
            print(-1)

# double linked list는 맞지만, 각 요소를 바로바로 접근하기 위해서는 prev와 next을 dict에 넣어서 매칭 시킨다.
"""
t = belts[new_num].front
            print(t)
            while t != None:
                print(t.id)
                t = t.next
"""