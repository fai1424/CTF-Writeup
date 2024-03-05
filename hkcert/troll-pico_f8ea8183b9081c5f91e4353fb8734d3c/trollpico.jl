using TropicalNumbers

function TropicalAM(X, Y)
  return X + Y + X * Y
end 

function TropicalSDP(X1, Y1, X2, Y2)
  return TropicalAM(X1, Y2) + X2, TropicalAM(Y1, Y2) 
end  

function TropicalBinomial(X, Y, n)
  s = 0
  oX, oY = dX, dY = X, Y
  while n > 0
    if n % 2 == 1
      if s == 0
        oX, oY = dX, dY
        s = 1
      else
        oX, oY = TropicalSDP(oX, oY, dX, dY)
      end
    end
    dX, dY = TropicalSDP(dX, dY, dX, dY)
    n = n >> 1
  end
  return oX, oY
end

function Encrypt(T, K)
  K = map((x)->parse(Int32, chop(string(x))) % 256, K)
  T = map(xor, T, K)
  return T
end

# Public Matrices
M = TropicalMinPlus{Int32}.(rand(UInt16, (32, 32)))
H = TropicalMinPlus{Int32}.(rand(UInt16, (32, 32)))

# Private Exponents
a = rand(UInt64)
b = rand(UInt64)
println(a)
println(b)

# Compute Shared Key
Ma, Ha = TropicalBinomial(M, H, a)
Mb, Hb = TropicalBinomial(M, H, b)

Ka = TropicalAM(Mb, Ha) + Ma
Kb = TropicalAM(Ma, Hb) + Mb

if Ka != Kb
  print("Something wrong")
else
  Plain = Vector{UInt8}(read("flag.txt", String))
  Cipher = Encrypt(Plain, Ka)

  open("output.txt","w") do io
    println(io,"M=",M)
    println(io,"H=",H)
    println(io,"Ma=",Ma)
    println(io,"Mb=",Mb)
    println(io,"Cipher=",Cipher)
  end
  print("Done")
end