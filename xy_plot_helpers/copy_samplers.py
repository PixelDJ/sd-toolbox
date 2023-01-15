import os
import ast
import pyperclip

root_path = input("Enter the location of the 'stable diffusion' folder (default: F:\\ai-art\\stable-diffusion-local): ") or "F:\\ai-art\\stable-diffusion-local"

if os.path.isdir(root_path):
    file_path = os.path.join(root_path, "modules\\sd_samplers.py")
    if os.path.isfile(file_path):
        with open(file_path) as f:
            print(f'Parsing {file_path}...')
            file_contents = f.read()
            tree = ast.parse(file_contents)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == 'samplers_k_diffusion' for target in node.targets):
                    print("Found samplers_k_diffusion")
                    samplers_k_diffusion_list = node.value
                    samplers = []
                    for i in range(len(samplers_k_diffusion_list.elts)):
                        sampler = samplers_k_diffusion_list.elts[i].elts[0].s
                        samplers.append(sampler)
                        print(sampler)
                    pyperclip.copy(', '.join(samplers))
                    print("Samplers copied to clipboard.")
    else:
        print("The file does not exist.")
else:
    print("The directory does not exist.")
