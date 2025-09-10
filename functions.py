# Loading .pytext files

def header(file_path):
    try:
        with open(file_path, 'r') as file:
            global line_num
            line_num = 1
            for line in file:
                line = line.strip()
                start_idx = line.find("[*")
                end_idx = line.rfind("*]")
                if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                    print(f"Found start char '{"[*"}' at index: {start_idx} on line {line_num}")
                    print(f"Found end char '{"*]"}' at index: {end_idx} on line {line_num}")
                    global header_text
                    global header_text_with_tags
                    header_text = line[start_idx + 1:end_idx]
                    header_text_with_tags = line[start_idx:end_idx + 3]
                    print(f"Extracted text: {header_text}")
                    print(f"Line {line_num}: {line}")
                line_num += 1
                return True
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

def sub_header(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            start_idx = content.find('(sh"')
            end_idx = content.rfind('"sh)')
            if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                global sh_text
                sh_text = content[start_idx + 4:end_idx]  # exclude start and end chars
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

def double_sub_header(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            start_idx = content.find('(dsh"')
            end_idx = content.rfind('"dsh)')
            if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                global dsh_text
                dsh_text = content[start_idx + 5:end_idx]  # exclude start and end chars
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

def bold(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            start_idx = content.find("[*")
            end_idx = content.rfind("*]")
            if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                global bold_text
                bold_text = content[start_idx + 2:end_idx]  # exclude start and end chars
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

def italic(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            start_idx = content.find("{*")
            end_idx = content.rfind("*}")
            if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                global italic_text
                italic_text = content[start_idx + 2:end_idx]  # exclude start and end chars
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

def underline(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            start_idx = content.find("(*")
            end_idx = content.rfind("*)")
            if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                global underline_text
                underline_text = content[start_idx + 2:end_idx]  # exclude start and end chars
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False