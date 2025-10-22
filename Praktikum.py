class persegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang dengan panjang {self.panjang} cm, dan lebar {self.lebar} cm"

try:
    panjang_input = float(input("Masukkan panjang persegi panjang (cm): "))
    lebar_input = float(input("Masukkan lebar persegi panjang (cm): "))

    pp = persegiPanjang(panjang_input, lebar_input)
    print("Keliling : ", pp.keliling(), "cm")
    print("Luas     : ", pp.luas(), "cm²")

except ValueError:
    print("Input harus berupa angka.")