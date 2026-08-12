"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""

class solution:
    def pattern5(self,N):
                for i in range(N):
                       for j in range (N,i,-1):
                            print("*", end=" ")
                       print()

if __name__ == "__main__":
    sol = solution()
    N=5
    sol.pattern5(N)