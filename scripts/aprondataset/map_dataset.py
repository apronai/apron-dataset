import argparse
import csv
import os
from tqdm import tqdm
import datasets


def parse_arguments():
    parser = argparse.ArgumentParser(description='map annotated classes between datasets')
    parser.add_argument('--bboxes_source', type=str, required=True,
                        help='source directory containing input annotations')
    parser.add_argument('--bboxes_target', type=str, required=True, help='target directory for mapped annotations')
    parser.add_argument('--dataset', type=str, required=True, help='name of target dataset')
    return parser.parse_args()


def map_dataset(bboxes_source, bboxes_target, dataset):
    if dataset not in datasets.DATASETS:
        raise RuntimeError(f'dataset {dataset} not defined in datasets.py')

    labels = datasets.DATASETS[dataset]

    os.makedirs(bboxes_target, exist_ok=True)
    for file_name in tqdm(os.listdir(bboxes_source), desc='mapping annotations to target dataset'):
        with open(os.path.join(bboxes_source, file_name), 'r', newline='', encoding='utf-8') as anno_file:
            anno = csv.DictReader(anno_file)
            with open(os.path.join(bboxes_target, file_name), 'w', newline='', encoding='utf-8') as output_file:
                output_anno = csv.DictWriter(output_file, fieldnames=anno.fieldnames)
                output_anno.writeheader()
                for row in anno:
                    mapped_id = labels.get_mapped_id(int(row['label']))
                    if mapped_id is not None:
                        row['label'] = labels.get_mapped_id(int(row['label']))
                        output_anno.writerow(row)


def main():
    args = parse_arguments()
    map_dataset(args.bboxes_source, args.bboxes_target, args.dataset)


if __name__ == '__main__':
    main()
