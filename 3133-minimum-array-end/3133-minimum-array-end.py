class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        x0 = x
        bin_x = bin(x)[2:]
        N = len(bin_x)
        zeros = bin_x.count('0')
        pp = pow(2, zeros)
        
        cnt = 0
        while n > pp:
            pp *= 2
            cnt += 1
        
        bin_x = list(bin_x)
        bin_x = cnt*['0']+bin_x
        bin_x = ''.join(bin_x)
        
        #########
        zeros = bin_x.count('0')
        arr = list(bin_x)
        for ind, char in enumerate(arr):
            if char == '1':
                continue
            if n == 1:
                break
            
            if pow(2, zeros-1) >= n:
                zeros -= 1
                continue
            
            n -= pow(2, zeros-1)
            arr[ind] = '1'
            zeros -= 1
            
        ans = int(''.join(arr), 2)
        return(ans)