ReportTool
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


##Usage
簡単なテンプレートエンジンみたいなもので
実現できないかと思いました

texファイル(~/Documents/ReportTool/src/sample.json)
``` tex
%%% config
% data:~/Documents/ReportTool/src/data.json
%%%
\documentclass[twocolumn,uplatex]{jsarticle} 
\usepackage[dvipdfmx]{graphicx}                                     
\usepackage{tabularx,setspace,booktabs,multirow} 

……
\section{実験結果}

実験結果を\ref{tbl:baseline}に示す.
今回チューニングをグリッドサーチで行った
パラメータは{# data["parameters"]["gamma"] #}であった.
そして精度は{# data["precesion"] * 100 #}\%であった
```

jsonファイル(~/Documents/ReportTool/src/data.json)
``` json
{
    "worker" : "長岡 太郎",
    "precesion" : 0.70,
    "recall" : 0.45,
    "parameters" : 
        { 
            "alpha" : 0.75,
            "beta": 0.50,
            "gamma" : 210
        },
    "timestamp" : "20140823"
}
```

コマンド
``` python
python pytex.py src/sample.tex > reports.tex
```

結果
``` tex
%%% config
% data:~/Documents/ReportTool/src/data.json
%%%
\documentclass[twocolumn,uplatex]{jsarticle} 
\usepackage[dvipdfmx]{graphicx}                                     
\usepackage{tabularx,setspace,booktabs,multirow} 

……
\section{実験結果}
実験結果を\ref{tbl:baseline}に示す.
今回チューニングをグリッドサーチで行った
パラメータは0.75であった.
そして精度は70\%であった.
```

