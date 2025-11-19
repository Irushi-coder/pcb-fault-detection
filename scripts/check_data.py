import os
from pathlib import Path

print('PCB Dataset Check')
print('='*60)

raw_dir = Path('data/raw')
defects = ['Missing_hole', 'Spurious_copper', 'Spur', 'Short', 'Open_circuit', 'Mouse_bite']

total = 0
for defect in defects:
    path = raw_dir / defect
    if path.exists():
        count = len(list(path.glob('*.jpg'))) + len(list(path.glob('*.png'))) + len(list(path.glob('*.bmp')))
        print(f'{defect:20s}: {count:4d} images')
        total += count
    else:
        print(f'{defect:20s}: NOT FOUND')

print('='*60)
print(f'Total images: {total}')
