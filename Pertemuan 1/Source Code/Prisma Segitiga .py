print ("Aplikasi menghitung luas sisi, luas permukaan dan volume Prisma Segitiga")

# Atur nilai variabel
Sisi = 14
Tinggi = 8
TinggiPrisma = 3
Alas = 6

# Rumus
LuasSisi = (Sisi + Sisi + Sisi) * Tinggi
LuasPermukaan = (Sisi + Sisi + Sisi) * Tinggi * TinggiPrisma
volume = 0.5 * Alas * TinggiPrisma * Tinggi

# Output
print("Sisi= ",Sisi )
print("Tinggi= ",Tinggi)
print("Tinggi Prisma= ",TinggiPrisma)
print("Alas = ",Alas)
print("Hasilnya Adalah")
print("Luas Sisi =",LuasSisi)
print("Luas Permukaan =",LuasPermukaan)
print("Volume =",volume)
