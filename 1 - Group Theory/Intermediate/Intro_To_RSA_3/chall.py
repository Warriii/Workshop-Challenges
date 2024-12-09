from Crypto.Util.number import isPrime, bytes_to_long
import secrets


with open("flag.txt", "r") as f:
    flag = f.read()
    
def genPrime(bits):
    while True:
        x = secrets.randbits(bits - 600)
        p = (x<<600)+1
        if isPrime(p):
            return p
        
p = genPrime(1024)
q = genPrime(1024)
N = p*q
e = 0x10001
m = bytes_to_long(flag.encode())
c = pow(m, e, N)

print(f"{N = }")
print(f"{c = }")

# N = 4425251209709031359523200849630225760169157607374213664235644753699880558114318935786999245805186334767623050620917674996437834795771435460148325603940016149303098176881592391800272450994806535968711016297529508003554814502839060614107036346788307383544498504520556013163476365728285719071588657494313215433254361244339176679711052587368657390212501574375893590612924106919921059278110602965098451029141560566812945151109640657457339915205112997178265653647607697865358620221381836523188202812572912556253653250603124765152247419648091319013485146809201331198775534091911694898728081340038103596994511309571075604481
# c = 2853099256671009276445228600866212070084314040911010134515891834577026493749890037386288984895707146786721246411401422754320257244788848724740371484205430464846539057823475003225520671101721269552623519470311554126554145150507792383009504925314323315742972488001774512998311007015042051148408269203262684187177563624237476725165855237033460703896056779093790419605233928866615548800213130518340764278222511690618087556009019805195045720563038189195129617422885995447892522032172192876386708850300224648629471068186500147093521183921935514937990221818215793847194734106767391320630862232306317506849170872389985314521