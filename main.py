import random
import os
import time
a=1
b=12
c=1
d=500000


for i in range(1,2): 
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = open(f"{timestr}.tex","w")
    string =f'''
    \\documentclass[12pt]{{article}}

    \\usepackage{{adjustbox}}
    \\usepackage{{amsmath}}
    \\newcommand{{\\mul}}[3][]{{
        \\quad\\large{{ \\begin{{tabular}}{{r}}
        \\textbf{{#3}}\\\\
    $\\boldsymbol{{\\times}}$ \\textbf{{#2}}\\\\
    \\hline \\vspace{{3pt}}
    \\textbf{{#1}}\\\\
    \\vspace{{10pt}}\\\\
    \\end{{tabular}}
    }}}}

    \\begin{{document}}
    \\adjustbox{{max width=\\columnwidth}}{{
        \\begin{{tabular}}{{ccccccc}}

        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\
        \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} & \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}} &\\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}& \\mul{{ {random.randint(a,b)} }}{{{random.randint(c,d)}}}\\\\

    \\end{{tabular}}}}

    \\end{{document}}
    '''

    for line in string.split('\n'):
        file.write(line+'\n')


    file.close()
    os.system(f'latexmk -pdf {timestr}.tex >/dev/null 2>&1')
    os.system(f'latexmk -c {timestr}.tex >/dev/null 2>&1')
    os.system(f'rm {timestr}.tex >/dev/null 2>&1')
    os.system(f'mv {timestr}.pdf out/{timestr}.pdf >/dev/null 2>&1')
    os.system(f'zathura out/{timestr}.pdf & disown >/dev/null 2>&1')
    print(f'{i} done')