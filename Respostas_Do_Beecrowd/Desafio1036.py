A, B, C= map(float, input().split())
delta= (B ** 2) - 4 * A * C
if A==0 or delta<0:
    print("Impossivel calcular")
else:
  import math
  delt= math.sqrt(delta)
  R1= ( -B + delt) / (2 * A)
  R2= ( -B - delt) / (2 * A)
  print("R1 = %.5f" %R1)
  print("R2 = %.5f" %R2)