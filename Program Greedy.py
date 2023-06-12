from re import L #
# Mengimpor modul sys yang menyediakan akses ke beberapa variabel.
import sys 
from queue import Queue#Mengimpor kelas Queue dari modul queue, yang digunakan untuk mengimplementasikan antrian dalam program.

def reset():#Mendefinisikan fungsi reset() yang digunakan untuk mengatur ulang variabel-variabel yang terlibat dalam algoritma.
    global dist, previous, q, in_queue#Mendeklarasikan variabel-variabel
    for i in range(m):#Melakukan perulangan untuk menginisialisasi variabel previous, dist, dan in_queue dengan nilai awal.
        previous[i] = 0
        dist[i] = -INF
        in_queue[i] = False
    dist[source] = 0#: Mengatur jarak awal dari source ke dirinya sendiri menjadi 0.
    previous[source] = -1# Mengatur nilai awal previous dari source ke -1.
    q.put(source)# Memasukkan source ke dalam antrian q.

def pushqueue(curr, before, new_distance):# Mendefinisikan fungsi pushqueue
    global dist, previous, q, in_queue#var yang ada di dalam pushqueue
    dist[curr] = new_distance#Mengatur jarak baru untuk curr
    previous[curr] = before# Mengatur simpul pendahulu dari curr.
    if not in_queue[curr]:#Memeriksa apakah curr belum ada dalam antrian.
        q.put(curr)# Memasukkan curr ke dalam antrian q.
        in_queue[curr] = True#Menandai bahwa curr ada dalam antrian.

def popqueue():#Mendefinisikan fungsi popqueue() yang mengeluarkan elemen dari antrian dan mengembalikannya.
    value = q.get()# Mengeluarkan elemen dari antrian q dan menyimpannya dalam variabel value.
    in_queue[value] = False# Menandai bahwa value tidak lagi ada dalam antrian.
    return value#Mengembalikan nilai yang dikeluarkan dari antrian.


INF = sys.maxsize#Menginisialisasi variabel INF dengan nilai maksimum yang tersedia pada sistem.
n = 3# Mendefinisikan jumlah pekerja atau pekerjaan.
m = n * 2 + 2#Menghitung jumlah total simpul dalam aliran, termasuk simpul sumber dan sumur.

matrix =[#profit untuk setiap kombinasi pekerjaan dan pekerja.
    [2, 4, 8],
    [4, 5, 6],
    [5, 7, 10]
]

matrix = [
    [6000, 10000, 20000],
    [7000, 7500, 9000],
    [9000, 11000, 15000]
]

flow = [[0] * m for _ in range(m)]#Menginisialisasi matriks aliran dengan ukuran m x m dan semua elemen diisi dengan 0.
source = 2 * n# Menentukan simpul sumber dalam aliran.
sink = 2 * n + 1#Menentukan simpul sumur dalam aliran.
profit = 0# Menginisialisasi variabel profit dengan nilai 0.
previous = [0] * m#Menginisialisasi array previous dengan nilai 0 untuk setiap simpul.
dist = [-INF] * m#Menginisialisasi array dist dengan nilai -INF untuk setiap simpul.
in_queue = [False] * m#Menginisialisasi array in_queue dengan nilai False untuk setiap simpul.
q = Queue()# Membuat objek antrian menggunakan kelas Queue.

while True:#loop sampai tidak ada peningkatan profit
    reset()#Memanggil fungsi reset()
    while not q.empty():#Memulai loop selama antrian tidak kosong.
        vertex = popqueue()#Mengeluarkan elemen dari antrian menggunakan fungsi popqueue() dan menyimpannya dalam variabel vertex.
        if vertex == source:#: Memeriksa apakah vertex adalah simpul sumber
            for worker in range(n):#mencari pekerjaan yang belum diassign untuk pekerja dan menambahkannya ke antrian.
                if flow[source][worker] == 0:
                    pushqueue(worker, source, 0)
        elif vertex < n:#Memeriksa apakah vertex adalah simpul pekerjaan.
            for job in range(n, 2 * n):#mencari pekerja yang belum mengambil pekerjaan tersebut dengan profit tertinggi dan memperbarui jarak serta pendahulunya.
                if flow[vertex][job] < 1 and dist[job] < dist[vertex] + matrix[vertex][job - n]:
                    pushqueue(job, vertex, dist[vertex] + matrix[vertex][job - n])
        else:#Memeriksa apakah vertex adalah simpul pekerja.
            for worker in range(n):#mencari pekerjaan yang telah diassign ke pekerja tersebut tetapi masih memiliki profit lebih tinggi jika dilepas, dan memperbarui jarak serta pendahulunya.
                if flow[vertex][worker] < 0 and dist[worker] < dist[vertex] - matrix[worker][vertex - n]:
                    pushqueue(worker, vertex, dist[vertex] - matrix[worker][vertex - n])
    
    curprofit = -INF#Menginisialisasi variabel curprofit dengan nilai -INF untuk mencatat profit terbaik yang ditemukan pada iterasi saat ini.
    for job in range(n, 2 * n):#Melakukan iterasi untuk pekerjaan yang belum diassign ke pekerja.
        if flow[job][sink] == 0 and dist[job] > curprofit:
            curprofit = dist[job]
            previous[sink] = job
 #Mencari pekerjaan dengan profit tertinggi yang belum masuk ke sumur dan memperbarui variabel curprofit serta previous jika ditemukan profit yang lebih tinggi.   
    if curprofit == -INF:# Memeriksa apakah curprofit tidak berubah dari nilai awalnya. Jika ya, berarti tidak ada pekerjaan dengan profit positif yang dapat diassign lagi, dan keluar dari loop.
        break
    
    profit += curprofit# Menambahkan curprofit ke total profit.
    cur = sink#Menginisialisasi variabel cur dengan nilai simpul sumur.
    while cur != -1:# Melakukan loop untuk mengupdate aliran dengan mengikuti jejak pendahulu mulai dari sumur hingga sumber. Mengecek apakah simpul sebelumnya ada, jika ada, maka mengatur aliran ke dan dari simpul tersebut.
        prev = previous[cur]
        if prev != -1:
            flow[prev][cur] = 1
            flow[cur][prev] = -1
        cur = prev
    
    pick = [0] * n#Menginisialisasi array pick dengan nilai 0 untuk setiap pekerja.
    for i in range(n):#Melakukan iterasi untuk setiap pekerja. Mencari pekerjaan yang telah diassign untuk setiap pekerja dan menyimpannya dalam array pick.
        for j in range(2 * n):
            if flow[i][j] == 1:
                pick[i] = j - n

# output
print("Matrix job assignment:")#Mencetak judul untuk matriks penugasan pekerjaan.
for i in range(n):#Melakukan iterasi untuk setiap baris matriks.
    for j in range(n):
        print(matrix[i][j], end=" ")#Mencetak elemen matriks dengan spasi sebagai pemisah.
    print()#Mencetak baris baru setelah setiap baris matriks.

print("The maximum profit is:", profit)#Mencetak nilai maksimum dari profit.
print("The selected assignments are:")#Mencetak judul untuk penugasan pekerjaan yang dipilih.
for i in range(n):#Melakukan iterasi untuk setiap pekerja.
    print("Worker %d is assigned Job %d with profit %d" % (i + 1, pick[i], matrix[i][pick[i]]))# Mencetak penugasan pekerjaan yang dipilih untuk setiap pekerja.
