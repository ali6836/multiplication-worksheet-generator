import random
import os
import time
output = str(input("Open documents? y/n: "))
match output:
    case 'y':
        output = 1
    case 'n':
        output = 0
a=2
b=12
c=int(input('Lowest value: '))
d=int(input('Highest value: '))
k=int(input('Number of PDFs: '))
j=int(input('Number of pages per PDF: '))

CHECK_FOLDER = os.path.isdir('out')
if not CHECK_FOLDER:
    os.makedirs('out')
    print("created folder : ", 'out')

for i in range(0,k): 
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = open(f"{timestr}.tex","w")
    string =f'''
    \\documentclass[12pt]{{article}}
    \\usepackage[a4paper, total={{7in, 10in}}]{{geometry}}
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
    '''
    end=f'''
    \\end{{document}}
    '''
    new=f'''
    \\pagebreak
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
    '''

    for line in string.split('\n'):
        file.write(line+'\n')
    for p in range(0,j-1):
        for line in new.split('\n'):
            file.write(line+'\n')
    for line in end.split('\n'):
        file.write(line+'\n')


    file.close()
    os.system(f'latexmk -pdf {timestr}.tex >/dev/null 2>&1')
    os.system(f'latexmk -c {timestr}.tex >/dev/null 2>&1')
    os.system(f'rm {timestr}.tex >/dev/null 2>&1')
    os.system(f'mv {timestr}.pdf out/{timestr}.pdf >/dev/null 2>&1')
    if output:
        os.system(f'zathura out/{timestr}.pdf & disown >/dev/null 2>&1')
    print(f'[{i+1}/{k}] Outputted to out/{timestr}.pdf')