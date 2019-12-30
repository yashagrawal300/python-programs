'''Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".'''



class Solution:
    def defangIPaddr(self, address: str) -> str:
        d = []
        for i in range(len(address)):
            if address[i]==".":
                d.append("[.]")
            else:
                d.append(address[i])
        return "".join(d)
        
