nama = 'Latifah Zunairoh'
program = 'gerak lurus'

print(f' program {program} oleh {nama}')

def hitung_kecepatan (jarak, waktu) :
    kecepatan = jarak / waktu
    print (f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print (f'sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

# jarak = 1000
# waktu = 5 * 60
kecepatan = hitung_kecepatan (1000, 5 * 60)
kecepatan = hitung_kecepatan (3000, 70 * 60)

def hitung_massajenis (massa, volume) :
    massajenis = massa / volume
    print (f'massa = {massa / 3000}kg dengan volume = {volume / 1500}m ** 3')
    print (f'sehingga massajenis = {massajenis}kg/m ** 3')
    return massajenis

# massa = 3000
# volume= 1500
massajenis = hitung_massajenis (3000, 1500)
massajenis = hitung_massajenis (3000, 1500)



