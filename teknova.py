import os
import hashlib

C = "\033[96m"
G = "\033[92m"
Y = "\033[93m"
R = "\033[0m"

def banner():
    os.system("clear")
    print(C + r"""
╔══════════════════════════════╗
║        TEKNOVA-X v1.0        ║
║      SECURITY SCANNER        ║
╚══════════════════════════════╝
""" + R)

def scan():
    folder = os.path.expanduser(
        "~/storage/shared/Download"
    )

    if not os.path.isdir(folder):
        print(Y + "Storage haijapatikana!" + R)
        print("Ruhusu storage kwa kuandika:")
        print("termux-setup-storage")
        return

    count = 0
    print(C + "\nScanning downloaded files..." + R)

    for root, dirs, files in os.walk(folder):
        for name in files:
            if name.lower().endswith(
                (".apk", ".dex", ".jar", ".sh")
            ):
                path = os.path.join(root, name)

                try:
                    h = hashlib.sha256()
                    with open(path, "rb") as f:
                        for block in iter(
                            lambda: f.read(65536), b""
                        ):
                            h.update(block)

                    print(Y + "\n[REVIEW] " + name + R)
                    print("SHA256:", h.hexdigest())
                    count += 1

                except OSError:
                    print("Imeshindwa kusoma:", name)

    print(G + f"\nFiles zilizokaguliwa: {count}" + R)
    print(Y + "Hii si antivirus kamili." + R)

def main():
    while True:
        banner()
        print("[1] Scan downloaded files")
        print("[2] Exit")

        choice = input("\nTEKNOVA-X > ")

        if choice == "1":
            scan()
            input("\nBonyeza Enter kuendelea...")
        elif choice == "2":
            break
        else:
            input("Chaguo si sahihi. Bonyeza Enter...")

if __name__ == "__main__":
    main()
0

