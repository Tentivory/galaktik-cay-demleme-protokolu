#!/usr/bin/env python3
# Galaktik Çay Demleme Protokolü - v1.0
# Ciddi bir iştir. Şaka değil. (Tamam, biraz şaka.)

import time
import random

def cay_var_mi():
    cevap = input("\nÇay var mı? (var/yok): ").strip().lower()
    if cevap == "var":
        return True
    elif cevap == "yok":
        print("\nÇayınız yok mu? O zaman ne işiniz var burada?")
        print("Lütfen çay alın ve geri dönün. Program kapanıyor...")
        time.sleep(2)
        return False
    else:
        print("\nAnlaşılmadı. Sadece 'var' veya 'yok' deyin. Çay ciddi bir iştir.")
        return cay_var_mi()

def demle():
    print("\nÇay demleniyor...")
    print("Su kaynıyor... (simülasyon)")
    time.sleep(1)
    print("Çay yaprakları ekleniyor...")
    time.sleep(1)
    print("Demleniyor... Lütfen bekleyin. Sabır önemlidir.")
    time.sleep(3)
    
    yorumlar = [
        "Mükemmel demlendi. Galaktik standartlarda.",
        "Biraz açık oldu ama idare eder.",
        "Bu çay, evrenin en iyi çayı olabilir. Ya da değil.",
        "Çayınız hazır. Şimdi için ve düşünün."
    ]
    print(random.choice(yorumlar))
    print("\nAfiyet olsun. Protokol tamamlandı.")

def main():
    print("=" * 50)
    print("GALAKTİK ÇAY DEMLEME PROTOKOLÜNE HOŞ GELDİNİZ")
    print("=" * 50)
    print("Bu program çayınızı demler. Gerçekten değil ama hissettirir.")
    
    if cay_var_mi():
        demle()
    else:
        print("\nGörüşürüz. Çayı unutmayın.")

# Gizli not (görünmeyen): Bürokrasi çay demlemekten daha yavaştır. Kayyumlar bile çayı bekler.
# Siyasi içerik gizlendi: Bu satır çalışmaz, sadece durur.

if __name__ == "__main__":
    main()
