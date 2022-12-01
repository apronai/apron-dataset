import argparse
import csv
import cv2
import os
from tqdm import tqdm
import datasets


def parse_arguments():
    parser = argparse.ArgumentParser(description='visualize annotation bounding-boxes')
    parser.add_argument('--images', type=str, required=True, help='input image directory')
    parser.add_argument('--bboxes', type=str, required=True,
                        help='input directory containing bounding-box annotations as csv files')
    parser.add_argument('--output_dir', type=str, required=True, help='output directory for generated visualizations')
    parser.add_argument('--dataset', type=str, default=None, help='name of dataset defining label colors')
    return parser.parse_args()


def visualize_annotations(images, bboxes, output_dir, dataset=None):
    labels = datasets.DATASETS[dataset] if dataset in datasets.DATASETS else None

    os.makedirs(output_dir, exist_ok=True)
    for file_name in tqdm(os.listdir(images), desc='visualizing annotations'):
        with open(os.path.join(bboxes, f'{os.path.splitext(file_name)[0]}.csv'), 'r') as anno_file:
            image = cv2.imread(os.path.join(images, file_name), cv2.IMREAD_COLOR)
            anno = csv.DictReader(anno_file)
            for row in anno:
                cv2.rectangle(image, (int(row['tlx']), int(row['tly'])), (int(row['brx']), int(row['bry'])),
                              (0, 255, 0) if labels is None else labels.get_label_color(int(row['label']), bgr=True), 2)
            cv2.imwrite(os.path.join(output_dir, file_name), image)


def main():
    args = parse_arguments()
    visualize_annotations(args.images, args.bboxes, args.output_dir, args.dataset)


if __name__ == '__main__':
    main()
