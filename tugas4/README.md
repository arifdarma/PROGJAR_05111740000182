# Tugas 4

## Dokumentasi Protokol

### Ketentuan membaca format

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

### Daftar Fitur

> cara melakukan request  
> apa respon yang didapat  

1. Upload file
    * Request:
    * Parameter: namafile.ekstensi
    * Response:
        * Berhasil -> `OK`
        * Gagal -> `ERROR`
1. Download file
    * Request:
    * Parameter: namafile.ekstensi
    * Response:
        * Berhasil -> `OK`
        * Gagal -> `ERROR`
1. List file
    * Request:
    * Parameter: namafile.ekstensi
    * Response:
        * Berhasil -> `OK`
        * Gagal -> `ERROR`
1. Jika _command_ tidak dikenali -> `ERRCMD`

<!-- - create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD -->
