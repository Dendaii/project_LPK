import streamlit as st
col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.markdown('''<div class='Anggota The7'>Dendi Gusmantara Pamungkas 2219060</div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class='Anggota The7'>Arina Nuris Sabyla 2219037</div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class='Anggota The7'>Najwa Aulia Blessinta 2219124</div>''', unsafe_allow_html=True)
with col4:
    st.markdown('''<div class='Anggota The7'>Naura Maulidya 2219129</div>''', unsafe_allow_html=True)
with col5:
    st.markdown('''<div class='Anggota The7'>Nida Nafilah 2219134</div>''', unsafe_allow_html=True)

st.title("Aplikasi Perhitungan Massa Molekul dan Stoikiometri Sederhana")

st.write("*Agar tidak bosan kami sedikit membuat permainan otak untuk teman teman dikarenakan aplikasi ini lumayan mudah digunakan jadi saya ingin sedikit mempersulit penggunaan nya, dimaksudkan agar murid murid juga senang menghitung Massa Molekul Relatif dengan manual")
st.write("He=q" ,"Li=w" ,"Be=r" ,"Fe=t" ,"Na=y" ,"Mg=u" ,"Ca=i" ,"Ne=o" ,"Al=p" ,"Si=a" ,"Cl=s" ,"Ar=d" ,"Ti=f" ,"Cr=g" ,"Mn=h" ,"Co=j" ,"Ni=k" ,"Cu=l" ,"Zn=z" ,"As=x" ,"Br=b" ,"Pd=c" ,"Ag=v" ,"Cd=n" ,"Ba=m" ,"Pt=[","Au=]","Hg=@","Pb=^ ")
st.write("Untuk atom lain yang tidak tercantum ditulis seperti biasa contoh pada NaOH Na ditulis sebagai y sedangkan OH tetap jadi untuk penulisan

rumus = st.text_input("Masukkan rumus molekul senyawa: ")



massa_atom = {"H": 1.008, "q": 4.003, "w": 6.941, "r": 9.012, "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00,"F": 19,"t":56.03,"y":23.001,"K": 39.098,"u": 24.305,"i": 40.078,"S": 32.06, "o": 20.18, "p": 26.98, "a": 28.08, "P": 30.97, "s": 35.5, "d": 40.00, "f": 48.0, "V": 50.94, "g": 52.00, "h": 54.94,"j": 58.93, "k": 58.70, "l": 63.55, "z": 65.40, "x": 74.92, "b": 79.90, "c": 106.42, "v": 107.86, "n": 112.41, "Sn": 118.71, "I": 126.90, "m": 137.33, "[": 195.08, "]": 196.97, "@": 200.59, "^": 207.2,}


 
total_massa = 0


i = 0
while i < len(rumus):
    
    simbol = rumus[i]
    
    
    
    jumlah_atom = 1
    i += 1
    while i < len(rumus) and rumus[i].isdigit():
        jumlah_atom = int(rumus[i])
        i += 1
    
    
    if simbol in massa_atom:
        massa = massa_atom[simbol] * jumlah_atom
        total_massa += massa
    else:
        st.write("Simbol unsur", simbol, "tidak dikenali")
        


st.write("Massa molar dari", rumus, "adalah", total_massa, "g/mol")

if st.button("Informasi cara menggunakan Aplikasi"):
    st.write(" 1.Masukkan rumus molekul senyawa yang akan di cari")
    st.write("2.Klik Enter")
    st.write("3.Data akan ditampilkan setelah rumus molekul") 

st.sidebar:

    
    
    
    
    
    
    
    
    
  



