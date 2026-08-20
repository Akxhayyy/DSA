"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

class solution:
    def pattern(self,N):
        for i in range(N):
            for j in range(N):
                print("* ", end="")
            print()

if __name__ == "__main__":
    sol = solution()
    N=5
    sol.pattern(N)