function note {
    $date = Get-Date -Format "dd/MM/yyyy"
    $name = Read-Host -Prompt "Name?" 

    $template = "\documentclass[a4paper,11pt]{article}
    \usepackage[utf8]{inputenc}
    
    \usepackage{tgheros}
    \renewcommand*\familydefault{\sfdefault} 
    \usepackage[T1]{fontenc}
    
    \newcommand{\imp}{\ensuremath\Rightarrow\ }
    
    \usepackage{parskip}
    
    \usepackage[dvipsnames]{xcolor}
    \newcommand{\blue}[1]{\textcolor{RoyalBlue}{#1}}
    \newcommand{\red}[1]{\textcolor{WildStrawberry}{#1}}
    \newcommand{\gre}[1]{\textcolor{ForestGreen}{#1}}
    
    \usepackage{enumitem}
    \setlist{nosep}
    
    \usepackage{geometry}
    \geometry{
     a4paper,
     left=25mm,
     top=30mm,
     }
    
    \newenvironment{boxed}
        {\begin{center}
        \begin{tabular}{|p{0.9\textwidth}|}
        \hline\\
        }
        { 
        \\\\\hline
        \end{tabular} 
        \end{center}
        }
    
    \usepackage{fancyhdr}
    \usepackage{lastpage}
    \pagestyle{fancy}
    \fancyhead[L]{$date}
    \fancyfoot[C]{\thepage/\pageref{LastPage}}
    
    \renewcommand{\headrulewidth}{0pt}
    
    \title{\textbf{Notitie sjabloon}}
    \author{Arthur Van Loo}
    \date{$date}
    
    \begin{document}
    
    \maketitle
    \noindent
    
    
    \end{document}"

    mkdir "$name"
    $path = '.\{0}\{0}.tex' -f $name
    New-Item -Path $path -ItemType File
    
    $template | Out-File -FilePath  $path
}