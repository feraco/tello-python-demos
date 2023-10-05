import os
import nbformat

def convert_py_to_ipynb(py_file_path, ipynb_file_path):
    with open(py_file_path, 'r', encoding='utf-8') as py_file:
        code = py_file.read()
    
    nb = nbformat.v4.new_notebook()
    nb.cells.append(nbformat.v4.new_code_cell(code))
    
    with open(ipynb_file_path, 'w', encoding='utf-8') as ipynb_file:
        nbformat.write(nb, ipynb_file)

def convert_all_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".py"):
            py_file_path = os.path.join(directory_path, filename)
            ipynb_file_path = os.path.join(directory_path, 
filename.replace(".py", ".ipynb"))
            convert_py_to_ipynb(py_file_path, ipynb_file_path)
            print(f"Converted {py_file_path} to {ipynb_file_path}")

# Example usage:
convert_all_in_directory ('/Users/wwhs-research/Downloads/UPH_DJITello-main/MachineLearning')

