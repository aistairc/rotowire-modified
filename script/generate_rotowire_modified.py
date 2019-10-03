import os
import json
import codecs
import argparse


def generate_dataset(src, lookup):
    dataset = []
    for line in lookup:
        line = line.strip().split(',')
        src_type = int(line[0])
        src_id = int(line[1])
        author = line[2]
        record = src[src_type][src_id]
        record["author"] = author
        dataset.append(record)
    return dataset


def main():
    parser = argparse.ArgumentParser(prog='Script for rotowire-modified')
    parser.add_argument('--src_dir', default='', type=str)

    args = parser.parse_args()

    # load src datasets
    with codecs.open(os.path.join(args.src_dir, 'train.json'), 'r', 'utf-8') as f:
        train_src = json.load(f)
    with codecs.open(os.path.join(args.src_dir, 'valid.json'), 'r', 'utf-8') as f:
        valid_src = json.load(f)
    with codecs.open(os.path.join(args.src_dir, 'test.json'), 'r', 'utf-8') as f:
        test_src = json.load(f)

    src = [train_src, valid_src, test_src]

    # load lookup tables
    with codecs.open(os.path.join(os.path.dirname(__file__), 'train-lookup.txt'), 'r', 'utf-8') as f:
        train_lookup = f.readlines()
    with codecs.open(os.path.join(os.path.dirname(__file__), 'valid-lookup.txt'), 'r', 'utf-8') as f:
        valid_lookup = f.readlines()
    with codecs.open(os.path.join(os.path.dirname(__file__), 'test-lookup.txt'), 'r', 'utf-8') as f:
        test_lookup = f.readlines()

    # generate modified datasets
    train_modified = generate_dataset(src, train_lookup)
    valid_modified = generate_dataset(src, valid_lookup)
    test_modified = generate_dataset(src, test_lookup)

    # dump modified datasets
    out_dir = 'rotowire-modified'
    try:
        os.makedirs(out_dir)
    except OSError as ex:
        print(ex)
        return

    with codecs.open(os.path.join(out_dir, 'train.json'), 'w', 'utf-8') as f:
        json.dump(train_modified, f)
    with codecs.open(os.path.join(out_dir, 'valid.json'), 'w', 'utf-8') as f:
        json.dump(valid_modified, f)
    with codecs.open(os.path.join(out_dir, 'test.json'), 'w', 'utf-8') as f:
        json.dump(test_modified, f)
    return


if __name__ == '__main__':
    main()
