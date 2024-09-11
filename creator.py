import argparse
import json
import os


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", "-l", type=int, default=50)
    parser.add_argument("--output", "-o", type=str, default="output")
    return parser.parse_args()


def edge_generator(id, src, dst):
    return {
        "id": id,
        "label": ["edge"],
        "src": src,
        "dst": dst,
        "property": {"name": f"e{id}"},
    }


def node_generator(id):
    return {"id": id, "label": ["node"], "property": {"name": f"v{id}"}}


def graph_generator(length):
    start = 1
    nodes = [node_generator(1)]
    edges = []
    for i in range(start, length + 1):
        nodes.append(node_generator(3 * i - 1))
        nodes.append(node_generator(3 * i))
        nodes.append(node_generator(3 * i + 1))
        edges.append(edge_generator(4 * i - 3, 3 * i - 2, 3 * i - 1))
        edges.append(edge_generator(4 * i - 2, 3 * i - 2, 3 * i))
        edges.append(edge_generator(4 * i - 1, 3 * i - 1, 3 * i + 1))
        edges.append(edge_generator(4 * i, 3 * i, 3 * i + 1))
    return nodes, edges


def output_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # ディレクトリがなければ作成
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main(length, output):
    nodes, edges = graph_generator(length)

    output_json(nodes, os.path.join(output, "nodes.json"))
    output_json(edges, os.path.join(output, "edges.json"))
    print(f"ノードとエッジのデータが {output} ディレクトリに保存されました。")


if __name__ == "__main__":
    args = arg_parser()
    main(args.length, args.output)
