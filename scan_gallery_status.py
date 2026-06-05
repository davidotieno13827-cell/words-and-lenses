from pathlib import Path

root = Path(r'C:\Users\Administrator\OneDrive\Desktop\my-portfolio')

# Identify valid JPEG vs HEIC-mislabeled files
valid_jpgs = []
heic_mislabeled = []

for p in sorted(root.glob('*.jpg')) + sorted(root.glob('*.jpeg')):
    data = p.read_bytes()[:12]
    if data.startswith(b'\xff\xd8\xff'):  # Real JPEG
        valid_jpgs.append(p.name)
    elif data.startswith(b'\x00\x00\x00') and b'ftyp' in data:  # HEIC
        heic_mislabeled.append(p.name)

print("=== VALID JPEG FILES (Ready to use) ===")
for f in valid_jpgs:
    print(f"  {f}")

print(f"\n=== CURRENTLY IN pictorials.html ===")
in_html = ['c1.jpeg', 'c2.jpeg', 'c3.jpeg', 'c4.jpeg', 'c5.jpeg', 'c6.jpeg', 'c8.jpeg', 'c9.jpeg',
           'clubbing1.jpeg', 'clubbing2.jpeg', 'clubbing3.jpeg', 'clubbing4.jpeg', 'clubbing5.jpeg',
           'clubbing6.jpeg', 'clubbing7.jpeg', 'travel1.jpeg', 'travel2.jpeg', 'travel3.jpeg',
           'p1.jpg', 'p2.jpg', 'p4.jpg', 'p5.jpg']
for f in in_html:
    print(f"  {f}")

print(f"\n=== AVAILABLE BUT NOT YET IN GALLERY ===")
available_not_used = [f for f in valid_jpgs if f not in in_html]
for f in available_not_used:
    print(f"  {f}")

print(f"\n=== HEIC-MISLABELED FILES (Cannot use until converted) ===")
for f in heic_mislabeled:
    print(f"  {f}")
