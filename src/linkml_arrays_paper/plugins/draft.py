#!/usr/bin/env python3
import argparse
import json
import sys


plugin = {
    "name": "Draft Text",
    "directives": [
        {
            "name": "draft",
            "doc": "Idk gray it out and stuff",
        }
    ],
}


def declare_result(content):
    """Declare result as JSON to stdout

    :param content: content to declare as the result
    """
    json.dump(content, sys.stdout, indent=2)
    # Successfully exit
    raise SystemExit(0)

def get_body(data: dict) -> dict:
    if data.get('type', None ) == 'mystDirectiveBody':
        return data
    else:
        for child in data.get('children', []):
            if res := get_body(child):
                return res


def run_directive(name, data):
    """Execute a directive with the given name and data

    :param name: name of the directive to run
    :param data: data of the directive to run
    """
    assert name == "draft"

    body = get_body(data['node'])

    res = {
        "type": "div",
        'style': {
            'padding': "0.5em",
            'font-style': 'italic',
            'background-color': 'var(--jp-layout-color1)',
            'position': 'relative',
            'margin-bottom': '1em'
        },
        'children': [
            {
                "type": "div",
                "value": "DRAFT",
                "style": {
                    "position": "absolute",
                    "right": 0,
                    "z-index": -1,
                    "transform": "rotate(90deg)",
                    "font-weight": "bold",
                    "color": "var(--jp-layout-color4)",
                    "font-size": "2em",
                    "transform-origin": "bottom",
                },
                "children": [
                    {
                        'type': 'text',
                        'value': 'DRAFT',
                    }
                ]
            },
            *body['children']
        ]
    }

    return [res]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        stdin = sys.stdin.read()
        data = json.loads(stdin)
        declare_result(run_directive(args.directive, data))
    elif args.transform:
        raise NotImplementedError
    elif args.role:
        raise NotImplementedError
    else:
        declare_result(plugin)
