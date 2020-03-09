import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'
    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

threads = []
for i in range(5):
    if i==1:
        link = 'https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg'
    elif i==2:
        link = 'https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg'
    elif i==3:
        link = 'https://cdn0-production-images-kly.akamaized.net/LEdkRVu4J7oa3FYtJzZ-qrgL7kI=/0x0:5720x3224/640x360/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/3037464/original/014685600_1580446457-ani-kolleshi-7jjnJ-QA9fY-unsplash.jpg'
    elif i==4:
        link = 'https://cdn1-production-images-kly.akamaized.net/3diH6s0Y_1ndQYsEBSz2e_eZpP0=/0x0:0x0/640x360/filters:quality(75):strip_icc():format(jpeg):watermark(kly-media-production/assets/images/watermarks/liputan6/watermark-gray-landscape-new.png,540,20,0)/kly-media-production/medias/2365173/original/012451900_1537673586-POT__1_.jpeg'
    else:
        link = 'https://cdn0-production-images-kly.akamaized.net/t3mAbxOqLMmRyA4SCeMfTjceLzc=/640x360/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/875279/original/059030700_1431447949-Instalasi-Pengolahan-Air-6.jpg'
    t = threading.Thread(target=download_gambar, args=(link,))
    threads.append(t)

for thr in threads:
    thr.start()


# if __name__=='__main__':
#    download_gambar('https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg')
