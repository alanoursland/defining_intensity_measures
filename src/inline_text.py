import os

def inline_tex(main_file):
    with open(main_file, 'r', encoding='utf-8') as f:  # UTF-8 encoding here
        content = f.read()

    while True:
        import_command_start = content.find(r'\input{')
        if import_command_start == -1:
            break

        import_command_end = content.find('}', import_command_start)
        import_file = content[import_command_start + 7:import_command_end]
        import_file = os.path.join(os.path.dirname(main_file), import_file)
        if not import_file.endswith('.tex'):
            import_file += '.tex'

        try:
            with open(import_file, 'r', encoding='utf-8') as infile:  # UTF-8 encoding here
                import_content = infile.read()
                import_content = import_content.replace(r'\documentclass[12pt]{article}', '')
                import_content = import_content.replace(r'\begin{document}', '')
                import_content = import_content.replace(r'\end{document}', '')
                content = content[:import_command_start] + import_content + content[import_command_end + 1:]
        except FileNotFoundError:
            print(f"Error: File '{import_file}' not found.")
            return

    with open("inlined_chapter.tex", 'w', encoding='utf-8') as outfile:  # UTF-8 encoding here
        outfile.write(content)

inline_tex("../paper/chapter.tex")