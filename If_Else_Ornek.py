defkullanici="busenur"
defsifre="678910"

kullanici=input("kullanici adi:")
sifre=input("sifre")
if((defkullanici==kullanici) and (defsifre==sifre)):
       print("Yazilim Dunyasina Hosgeldiniz")
elif((defkullanici==kullanici) and (defsifre!=sifre)):
       print("Sifrenizi yanlıs girdiniz")
elif((defkullanici!=kullanici) and (defsifre==sifre)):
       print("Kullanici adinizi yanlis girdiniz")
else:
       print("Kullanici adi ve sifre hatalıdır")