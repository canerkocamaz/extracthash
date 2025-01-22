# extracts ntlm hash file from SAM and SYSTEM file.
import sys
from impacket.examples.secretsdump import LocalOperations, SAMHashes

def extract_hashes(sam_file, system_file):
    try:
        print("[*] SYSTEM dosyasindan Boot Key cikariliyor...")
        local_ops = LocalOperations(system_file)
        boot_key = local_ops.getBootKey()

        print("[*] SAM dosyasindan kullanici bilgileri okunuyor...")
        sam_hashes = SAMHashes(sam_file, boot_key)
        sam_hashes.dump()
        sam_hashes.finish()

        print("[*] İşlem tamamlandi.")
    except Exception as e:
        print(f"[!] Hata: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanim: python extract_hashes.py <SAM dosyasi yolu> <SYSTEM dosyasi yolu>")
        sys.exit(1)

    sam_path = sys.argv[1]
    system_path = sys.argv[2]

    extract_hashes(sam_path, system_path)
