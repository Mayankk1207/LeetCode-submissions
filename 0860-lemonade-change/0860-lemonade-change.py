class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        f = 0 
        t = 0
        
        for x in bills:
            if x == 5:
                f+=1
            elif x == 10:
                if f > 0:
                    f-=1
                    t+=1
                else:
                    return False
            else:
                if t >0 and f>0:
                    t-=1
                    f-=1

                elif f>=3:
                    f-=3
                else:
                    return False
        return True
        
