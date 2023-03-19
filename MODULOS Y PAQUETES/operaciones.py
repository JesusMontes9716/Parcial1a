class calcBasica:



    def resta(*nums): 
        res = 0
        for valor in nums:
            res -= valor

        return res
    
    def suma(*nums): 
        res = 0
        for valor in nums:
            res += valor

        return res
    
    def divicion(n1 , n2): 
        res = 0
        for valor in nums:
            res = n1 / n2
            sobra = n1 % n2

        return res, sobra
    
    def multiplicacion(*nums): 
        res = 0
        for valor in nums:
            res *= valor

        return res