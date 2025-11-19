import os
import shutil
from pathlib import Path
import random

def prepare_pcb_dataset():
    print('PCB Dataset Preparation')
    print('='*60)
    
    raw_dir = Path('data/raw')
    processed_dir = Path('data/processed')
    
    defect_types = {
        'Missing_hole': 0,
        'Spurious_copper': 1,
        'Spur': 2,
        'Short': 3,
        'Open_circuit': 4,
        'Mouse_bite': 5
    }
    
    for split in ['train', 'val', 'test']:
        (processed_dir / split / 'images').mkdir(parents=True, exist_ok=True)
        (processed_dir / split / 'labels').mkdir(parents=True, exist_ok=True)
    
    print('Collecting images...')
    all_data = []
    
    for defect_name, class_id in defect_types.items():
        defect_path = raw_dir / defect_name
        
        if not defect_path.exists():
            print(f'Warning: {defect_name} folder not found!')
            continue
        
        images = list(defect_path.glob('*.jpg')) + list(defect_path.glob('*.png')) + list(defect_path.glob('*.bmp'))
        print(f'{defect_name}: {len(images)} images')
        
        for img in images:
            all_data.append((img, class_id, defect_name))
    
    print(f'Total images: {len(all_data)}')
    
    if len(all_data) == 0:
        print('ERROR: No images found!')
        return
    
    random.seed(42)
    random.shuffle(all_data)
    
    train_size = int(0.7 * len(all_data))
    val_size = int(0.15 * len(all_data))
    
    train_data = all_data[:train_size]
    val_data = all_data[train_size:train_size + val_size]
    test_data = all_data[train_size + val_size:]
    
    print(f'Train: {len(train_data)}, Val: {len(val_data)}, Test: {len(test_data)}')
    
    for split_name, split_data in [('train', train_data), ('val', val_data), ('test', test_data)]:
        for idx, (img_path, class_id, defect_name) in enumerate(split_data):
            new_name = f'{defect_name}_{idx}{img_path.suffix}'
            dest_img = processed_dir / split_name / 'images' / new_name
            shutil.copy(img_path, dest_img)
            
            label_file = processed_dir / split_name / 'labels' / f'{Path(new_name).stem}.txt'
            with open(label_file, 'w') as f:
                f.write(f'{class_id} 0.5 0.5 1.0 1.0\n')
    
    print('Dataset preparation complete!')

if __name__ == '__main__':
    prepare_pcb_dataset()
