class Solution:
    def validIPAddress(self, IP: str) -> str:
        ip_arr = None
        if('.' in IP):
            ip_arr = IP.split('.')
        else:
            ip_arr = IP.split(':')
        
        if(len(ip_arr) == 4):
            for i in ip_arr:
                if(i.isnumeric()):
                    if(len(i) > 1):
                        if(int(i) >= 0 and int(i) <= 255 and i[0] != '0'):
                            pass
                        else:
                            return "Neither"
                else:
                    return "Neither"
            
            return "IPv4"
        elif(len(ip_arr) == 8):
            hexa_char = ['a', 'b', 'c', 'd', 'e', 'f']
            
            for i in ip_arr:
                if(len(i) >= 1 and len(i) <= 4):
                    i = i.lower()
                    for j in i:
                        if(not j.isnumeric()):
                            if(j not in hexa_char):
                                return "Neither"
                else:
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"
