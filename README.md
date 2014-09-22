pytex
==========
若手の会 - オープンタスク
論文(TeX)を書くときに使えるツールを作りたい.


##目指すこと
データと文書の分離.

データ(実験結果) → json
文書 → tex

使い方:
latexからjsonファイルを読み出す方法が特に無い. (別の手段が使えるからか？)
CSVファイルを読み込むことはできるっぽい. 

##Install
```zsh
git clone https://github.com/YANS2014/pytex.git
```

##Usage
簡単なテンプレートエンジンみたいなもので
実現できないかと思いました

texファイル(~/Documents/ReportTool/src/sample.json)
``` tex
%%% config
% data1:/home/takeno/Documents/ReportTool/src/data.json
%%%
\documentclass[twocolumn,uplatex]{jsarticle} 
\usepackage[dvipdfmx]{graphicx}                                     
\usepackage{tabularx,setspace,booktabs,multirow} 

% subfigure の packages 設定

\begin{document}

\title{tex中にjsonファイルの内容を埋め込む} 
\author{
    若手 太郎,
}
\date{takeno@jnlp.org} 
\maketitle

データを分離したい.
例えば私の名前は{@ data['worker'] @}を表示したい

\section{実験結果}
今回チューニングをグリッドサーチで行った
結果は{@ data["expt1"]["parameters"]["gamma"] @}であった.
そして精度は{@ data["expt1"]["precesion"] @}であった

\end{document}
```

jsonファイル(~/Documents/ReportTool/src/data.json)
``` json
{
    "author" : "長岡 太郎",
    "expt1" : {
        "precesion" : 0.70,
        "recall" : 0.45,
        "parameters" : 
            { 
                "alpha" : 0.75,
                "beta": 0.50,
                "gamma" : 210
            },
        "timestamp" : "2014-07-15"
    },
    "expt2" : {
        "precesion" : 0.70,
        "recall" : 0.45,
        "parameters" : 
            { 
                "alpha" : 0.75,
                "beta": 0.50,
                "gamma" : 210
            },
        "timestamp" : "2014-08-25"
    },
    "timestamp" : "2014-09-23"
}
```

コマンド
``` python
python pytex.py < src/sample.tex > reports.tex
```

結果
``` tex
%%% config
% data:/home/takeno/Documents/pytex/src/data.json
%%%
\documentclass[uplatex]{jsarticle}
\usepackage[dvipdfmx]{graphicx}
\usepackage{tabularx,setspace,booktabs,multirow}


\begin{document}

\title{tex中にjsonファイルの内容を埋め込む}
\author{
長岡 太郎
}
\maketitle

データを分離したい.
例えば私の名前は長岡 太郎を表示したい


\section{実験結果}
今回チューニングをグリッドサーチで行った
パラメータは$\gamma$ は 210であった.
そして精度は0.7であった

\end{document}
 
```

