# Mengimpor Library
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Membuat object url
url = 'https://www.worldometers.info/coronavirus/'

# Membuat object page
page = requests.get(url)
page

# Mengambil informasi website 'page'
soup = BeautifulSoup(page.text, 'lxml')
soup

# Mengambil informasi tag <table>
tabel = soup.find('table', id='main_table_countries_today')
tabel

# Mengambil semua nama kolom dengan tag <th>
headers = []
for i in tabel.find_all('th'):
    judul = i.text
    headers.append(judul)
    
headers[13] = 'Tests/1M pop'

# Membuat dataframe untuk tabel utama
dataku = pd.DataFrame(columns=headers)

# Mengisi datafram dataku
for j in tabel.find_all('tr')[1:]: # <tr> untuk per barisnya
    data_baris = j.find_all('td')  # <td> untuk per kolomnya
    baris = [tr.text for tr in data_baris]
    panjang = len(dataku)          # menghitung sampai dibaris keberapa
    dataku.loc[panjang] = baris
    
# Menghilangkan dan merapikan baris
dataku.drop(dataku.index[0:7], inplace=True)
dataku.drop(dataku.index[222:231], inplace=True)
dataku.reset_index(inplace=True, drop=True)

# Menghilangkan kolom #
dataku.drop('#', inplace=True, axis=1)

# Eksport ke CSV
dataku.to_csv('data_covid.csv', index=False)

# Mebuka file yang sudah disimpan
buka = pd.read_csv('data_covid.csv')
