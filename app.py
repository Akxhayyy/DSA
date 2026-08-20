class solution:
    def pattern(self,N):
        for i in range(N):
            for j in range(N):
                print("* ", end="")
            print()

    def pattern2(self,N):
        for i in range(N):
            print("* " * (i+1))

    def pattern3(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()

    def pattern4(self,N):
            for i in range(1,N+1):
                for j in range(1,i+1):
                    print(i, end=" ")
                print()

    def pattern5(self,N):
                for i in range(N-1,1):
                   print("* " , end=" ")
                print()

if __name__ == "__main__":
    sol = solution()
    N=5
    sol.pattern4(N)