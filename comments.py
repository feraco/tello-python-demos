import nbformat as nbf
import os

def convert_comments_to_markdown(notebook_path):
    with open(notebook_path, 'r') as f:
        nb = nbf.read(f, as_version=4)

    new_cells = []
    for cell in nb.cells:
        if cell.cell_type == 'code':
            code = cell.source.split('\n')
            markdown = []
            new_code = []

            for line in code:
                if line.strip().startswith("#"):
                    markdown.append(line.strip("# "))
                else:
                    new_code.append(line)
                    
            # Add any collected markdown and code as new cells
            if markdown:
                new_cells.append(nbf.v4.new_markdown_cell("\n".join(markdown)))
            if new_code:
                new_cells.append(nbf.v4.new_code_cell("\n".join(new_code)))
        else:
            new_cells.append(cell)

    nb.cells = new_cells
    
    with open(notebook_path, 'w') as f:
        nbf.write(nb, f)

def convert_all_notebooks(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".ipynb"):
            notebook_path = os.path.join(directory_path, filename)
            convert_comments_to_markdown(notebook_path)

# Example usage:
convert_all_notebooks('/Users/wwhs-research/Downloads/UPH_DJITello-main/Simple_Commands')
