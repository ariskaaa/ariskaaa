nm=[]
n=[]
tgs=[]
uts=[]
uas=[]
stop=False
no=0
while (not stop) :
    nama      =raw_input ("\tMasukan Nama  :")
    nm.append(nama)
    nim       =input     ("\tNIM           :")
    n.append(nama)
    tugas     =input     ("\tTugas         :")
    tgs.append(tugas)
    nilai_uts =input   ("\tUTS           :")
    uts.append(uts)
    nilai_uas =input   ("\tUAS           :")
    uas.append(uas)
    data      =raw_input ("Tambah Data (Y/T) ?")
    if (data == 't') :
        stop = True

    akhir=(tugas+nilai_uts+nilai_uas)/3
    no += 1
print "#########################################################################"
print "   No   |   Nama   |   NIM   |   Tugas   |   UTS   |   UAS   |   Akhir   |"
print "    ",no," |   ",nama,"  | ",nim,"  | ",tugas,"      | ",nilai_uts,"    | ",nilai_uas,"    | ",akhir,"      |"
print "#########################################################################"
