from abc import ABC, abstractmethod

class KamarHotel(ABC):
    def __init__(self, nama_kamar, harga_dasar):
        self._nama_kamar = nama_kamar
        self.__harga_dasar = harga_dasar
        self.__stok = 0

    def get_nama_kamar(self):
        return self._nama_kamar

    def get_harga_dasar(self):
        return self.__harga_dasar

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self._nama_kamar}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self._nama_kamar}: {self.__stok} unit.")

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah_malam):
        pass


class KamarDeluxe(KamarHotel):
    def __init__(self, nama_kamar, harga_dasar, fasilitas):
        super().__init__(nama_kamar, harga_dasar)
        self.fasilitas = fasilitas

    def tampilkan_detail(self):
        print(f"[DELUXE] {self.get_nama_kamar()} | Fasilitas: {self.fasilitas}")

    def hitung_harga_total(self, jumlah_malam):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.10
        subtotal = (harga_dasar + pajak) * jumlah_malam
        return pajak, subtotal


class KamarStandard(KamarHotel):
    def __init__(self, nama_kamar, harga_dasar, kapasitas):
        super().__init__(nama_kamar, harga_dasar)
        self.kapasitas = kapasitas

    def tampilkan_detail(self):
        print(f"[STANDARD] {self.get_nama_kamar()} | Kapasitas: {self.kapasitas}")

    def hitung_harga_total(self, jumlah_malam):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.05
        subtotal = (harga_dasar + pajak) * jumlah_malam
        return pajak, subtotal


def proses_transaksi(daftar_pesanan):
    print("\nSTRUK PEMESANAN")
    total_tagihan = 0
    for i, (kamar, malam) in enumerate(daftar_pesanan, 1):
        print(f"{i}. ", end="")
        kamar.tampilkan_detail()
        
        pajak = kamar.get_harga_dasar() * (0.10 if isinstance(kamar, KamarDeluxe) else 0.05)
        persen_pajak = "10%" if isinstance(kamar, KamarDeluxe) else "5%"
        _, subtotal = kamar.hitung_harga_total(malam)
        total_tagihan += subtotal
        
        harga_str = f"Rp {kamar.get_harga_dasar():,}".replace(",", ".")
        pajak_str = f"Rp {int(pajak):,}".replace(",", ".")
        subtotal_str = f"Rp {int(subtotal):,}".replace(",", ".")
        
        print(f"Harga Dasar/Malam: {harga_str} | Pajak ({persen_pajak}): {pajak_str}")
        print(f"Menginap: {malam} malam | Subtotal: {subtotal_str}\n")
        
    total_str = f"Rp {int(total_tagihan):,}".replace(",", ".")
    print(f"TOTAL TAGIHAN: {total_str}")


if __name__ == "__main__":
    print("SETUP DATA KAMAR")
    deluxe = KamarDeluxe("Kamar Deluxe Sea View", 1500000, "Private Pool")
    standard = KamarStandard("Kamar Standard Superior", 500000, "2 Orang")
    
    deluxe.tambah_stok(10)
    standard.tambah_stok(-5)
    standard.tambah_stok(20)
    
    pesanan = [
        (deluxe, 2),
        (standard, 1)
    ]
    
    proses_transaksi(pesanan)