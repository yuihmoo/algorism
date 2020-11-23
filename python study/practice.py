print(5)
print(-10)
print(3.14)
print(1000)
print(1425*2333)
gunsan = "shit"
print(gunsan)
i=4
j=8
print(i+j)
print(i-j)
print(i*j)
print(i/9)
print(i*i)
Nael_Caewoom = "Very_Good"
print(Nael_Caewoom)
con = "error"

if con == "error":
      print("새로 사다")
else:
      print("그냥 쓴다")

season = "fall"

if season == "spring":
    print("봄이 왔네요")
elif season == "summer":
    print("여름에는 비키니")
elif season == "fall":
    print("내가 제일 좋아하는 계절")
elif season == "winter":
    print("겨울에는 눈이 와요")

i = 1
while i < 11: # 조건식
    print("파이썬"+str(i))
    i = i+1 #탈출조건

str = "파이썬 프로그래밍"

for ch in str:
    print(ch)

range(5)
range(1,33)

for col in range(2,10):
    for row in range(1,10):
        print(col,"x",row,"=", col*row)

primes = [2,3,5,7]

for p in primes:
    print(p)

print(len(primes))

def arith(a,b):
    add = a+b
    sub = a-b
    return add, sub


i,j = arith(10,1)
print(i)
print(j)

def add(a,b):
   return a+b

print(add(1,2))
print((lambda a,b: a+b)(1,2))

class Dog: #클래스 선언
    name = "삼식이" #속성 선언
    age = 3
    breed = "골든 리트리버"

    def bark(self): # 메소드 선언
        print(self.name + "가 멍멍하고 짖는다")

my_dog = Dog() #인스턴스 생성

print(my_dog.breed) # 인스턴스의 속성 접근
my_dog.bark() #인스턴스의 메소드 호출

yuihmoo = "용재는 매우 똑똑하다."
print(yuihmoo)

김도환 = "천재"
print(김도환)
