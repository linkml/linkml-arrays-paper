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
            "arg": {
                "type": "string",
                "doc": "Additional subtype of draft item to display as label",
            },
            "body": True,
        }
    ],
}

CONTAINER_STYLE = {
    "padding": "0.5em 4em 0.5em 1.5em",
    "font-style": "italic",
    "background-color": "var(--jp-layout-color1)",
    "position": "relative",
    "margin-bottom": "1em",
    "min-height": "8em",
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "center",
}

LABEL_CONTAINER_STYLE = {
    "position": "absolute",
    "right": "0.5em",
    "top": "0.75em",
    "z-index": -1,
    "writing-mode": "vertical-rl",
}

DRAFT_LABEL_STYLE = {
    "font-weight": "bold",
    "color": "var(--jp-layout-color4)",
    "font-size": "2em",
    "line-height": "1em",
}

ARG_LABEL_STYLE = {
    "color": "var(--tw-prose-code)",
    "font-size": "2em",
    "font-family": "var(--jp-code-font-family)",
    "font-size": "1em",
    "font-style": "normal",
    "line-height": "1em",
}


def declare_result(content):
    """Declare result as JSON to stdout

    :param content: content to declare as the result
    """
    json.dump(content, sys.stdout, indent=2)
    # Successfully exit
    raise SystemExit(0)


def get_body(data: dict) -> dict:
    if data.get("type", None) == "mystDirectiveBody":
        return data
    else:
        for child in data.get("children", []):
            if res := get_body(child):
                return res


def make_labels(arg: str | None) -> dict:
    draft_label = {
        "type": "div",
        "value": "DRAFT",
        "style": DRAFT_LABEL_STYLE,
        "children": [
            {
                "type": "text",
                "value": "DRAFT",
            }
        ],
    }

    container = {
        "type": "div",
        "style": LABEL_CONTAINER_STYLE,
        "value": "DRAFT",
        "children": [
            draft_label,
        ],
    }
    if arg is not None:
        arg_label = {
            "type": "div",
            "style": ARG_LABEL_STYLE,
            "value": "DRAFT",
            "children": [{"type": "text", "value": arg}],
        }
        container["children"].append(arg_label)

    return container


def run_directive(name, data):
    """Execute a directive with the given name and data

    :param name: name of the directive to run
    :param data: data of the directive to run
    """
    assert name == "draft"

    arg = data.get("arg", None)

    body = get_body(data["node"])

    res = {
        "type": "div",
        "style": CONTAINER_STYLE,
        "children": [make_labels(arg), *body["children"]],
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
