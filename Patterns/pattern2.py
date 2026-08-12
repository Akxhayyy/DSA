class solution:
    def pattern(self,N):
        for i in range(N):
                print("* " * (i+1))
            

if __name__ == "__main__":
    sol = solution()
    N=5
    sol.pattern(N)