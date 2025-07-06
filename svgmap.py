import graphviz
import os
import re

# === Config ===
dot_path = "gate_regions.dot"
output_image_path = "gate_regions.svg"
readme_path = "README.md"
image_relative_path = output_image_path  # This is how it will appear in the README

# === Generate SVG from DOT ===
def render_dot_to_svg(dot_path, output_path):
    with open(dot_path, "r") as f:
        dot_source = f.read()
    graph = graphviz.Source(dot_source)
    graph.render(output_path, format="svg", cleanup=True)
    print(f"Rendered: {output_path}")

# === Update README.md ===
def update_readme_with_image(readme_path, image_path):
    image_markdown = f"![Graphviz Graph]({image_path})"

    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# Graph\n\n{image_markdown}\n")
        print("Created new README.md")
        return

    with open(readme_path, "r") as f:
        content = f.read()

    pattern = r"!\[Graphviz Graph\]\([^)]+\)"
    if re.search(pattern, content):
        content = re.sub(pattern, image_markdown, content)
    else:
        content += f"\n\n{image_markdown}\n"

    with open(readme_path, "w") as f:
        f.write(content)
    print("Updated README.md")

# === Run ===
if __name__ == "__main__":
    render_dot_to_svg(dot_path, output_image_path.replace(".svg", ""))
    update_readme_with_image(readme_path, image_relative_path)
