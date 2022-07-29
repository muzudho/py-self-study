# O_9o0 以前の記事

📖 [Python自習O_9o0 目次だぜ（＾～＾）](https://crieit.net/posts/Python-62de8a581dbea) - 目次  
📖 [Python自習O0o0 クラスを動的に読み込もうぜ（＾～＾）](https://crieit.net/posts/Python-62de830e6dd8e) - Dimport クラス  

# O0o0 今回の記事

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　自習しよ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　勝手にしろだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 最初のお題はこれよ」  

# O1o0 Non-numeric Separated Value

Input:  

```plaintext
ABC123DEF456GHI
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　何だぜ　これ？」  

Output:  

```plaintext
["ABC", "123", "DEF", "456", "GHI"]
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👆 文字列と、数字列を区別して　スプリットしなさい」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　input 無視して output をそのまま出せばいいのでは？」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　練習をしろ」  

## O1o1o0 Test

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　テストを書いて置いたから、これに合うようにコードを書きなさい」  

### O1o1o1o0 quest.py

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のファイルを新規作成しなさい」  

```plaintext
    ├── 📂 tests
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
👉  │           └── 📄 quest.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
class Questioner:
    """出題者"""

    def make_quiz(self):
        """答えのある問い作成"""
        return "ABC123DEF456GHI"

    def check(self, answer, quiz):
        """答え合わせ
        Returns
        -------
        str
            Error message or None
        """
        err_list = []

        if answer is None:
            err_list.append("[Error] vec is none")
        else:
            vec_size = len(answer)
            if vec_size != 5:
                err_list.append(
                    f"[Error] the size is different. size:{vec_size}")

            if answer != ["ABC", "123", "DEF", "456", "GHI"]:
                err_list.append(
                    f"[Error] the response is different. vec:{answer}")

        if 0 < len(err_list):
            return "\n".join(err_list)
        else:
            return None
```

### O1o1o2o0 test.py

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のファイルを新規作成しなさい」  

```plaintext
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
👉  │   │       └── 📄 test.py
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 quest.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o2o0 --ac Answerer
"""
import argparse
from src.dimport import Dimport  # Dynamic class import

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('--qm', help='questioner module')
ap.add_argument('--qc', help='questioner class')
ap.add_argument('--am', help='answerer module')
ap.add_argument('--ac', help='answerer class')
args = ap.parse_args()

# Plan
Questioner = Dimport.load(args.qm, args.qc)
quest = Questioner()
quiz = quest.make_quiz()
print(f"quiz:{quiz}")

# Do
Answerer = Dimport.load(args.am, args.ac)
answer = Answerer.to_answer(quiz)
print(f"answer:{answer}")

# Check
err = quest.check(answer, quiz)
if err is None:
    print("correct!")
else:
    print(err)
```

### O1o1o3o0 検索パス

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のファイルを新規作成しなさい」  

```plaintext
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
👉  │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
from .nonnumsv.o1o0g1o1o0.quest import Questioner as QuestionerO1o0g1o1o0
#    --------------------------        ----------    --------------------
#    1                                 2             3
# 1. 同じディレクトリーからの相対パス
# 2. クラス
# 3. クラスの別名
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　これでどこかに `Answerer` クラスを作って `to_answer` メソッドを付けてくれれば テストできるわよ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　フーン　じゃあ　スケルトンから作るか」  

## O1o2o0 Skeleton

### O1o2o_1o0 Answerer

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを作ってくれだぜ」  

```plaintext
    ├── 📂 src
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o2o0    
👉  │           └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
class Answerer:
    """Non-numeric separated value"""

    @staticmethod
    def to_answer(quiz):
        return []
```

### O1o2o_2o0 検索パス

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを作ってくれだぜ」  

```plaintext
    ├── 📂 src
    │   └── 📂 nonnumsv
    │       ├── 📂 o1o0g1o2o0    
    │       │   └── 📄 __init__.py
👉  │       └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
from .o1o0g1o2o0 import Answerer as AnswererO1o0g1o2o0
#    -----------        --------    ------------------
#    1                  2           3
# 1. 同じディレクトリーにある o1o0g1o2o0 ディレクトリー
# 2. クラス
# 3. クラスの別名
```

### O1o2o_3o0 検索パス

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 前のレッスンで作った、以下の既存ファイルに１行追加してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
👉  │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .nonnumsv.o1o0g1o2o0 import Answerer
```

### O1o2o1o0 コマンド実行

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 このコマンドを実行すると」  

Input:  

```shell
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o2o0 --ac Answerer
```

Output:  

```shell
quiz:ABC123DEF456GHI
answer:[]
[Error] the size is different. size:0
[Error] the response is different. vec:[]
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👆 エラーが出るわけだな」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　`to_answer` 静的メソッドを実装しろだぜ」

## O1o3o0 まず、そのまま出そうぜ

### O1o3o1o0 answerer

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを作ってくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
👉  │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o3o0 --ac Answerer
"""


class Answerer:
    """Non-numeric separated value"""

    @staticmethod
    def to_answer(text):
        return ["ABC", "123", "DEF", "456", "GHI"]
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　お父んのフォルダー名の付け方　狂ってて　わらう」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　クラス名の付け方も　狂ってるわよ」  

### O1o3o2o0 検索パス

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下の既存ファイルの冒頭に１行追加してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
👉  │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .o1o0g1o3o0 import Answerer as AnswererO1o0g1o3o0


# ...略...
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　モジュールの検索パスを 手動で書くの めんどくさいけど 仕方ない」  

### O1o3o3o0 コマンド

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```shell
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o3o0 --ac Answerer
```

Output:  

```shell
quiz:ABC123DEF456GHI
answer:['ABC', '123', 'DEF', '456', 'GHI']
correct!
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　そりゃ正解よ」  

## O1o4o0 正規表現を使って出そうぜ

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　今までは　練習の枠組みを用意したわけだぜ。  
ここからが本番だぜ」  

### O1o4o1o0 answerer

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを作ってくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
👉  │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o4o0 --ac Answerer
"""
import re


class Answerer:
    """Non-numeric separated value"""

    # * `^` - 行頭
    # * `( )` - キャプチャーグループ
    # * `[A-Z]` - 大文字のAからZ
    # * `[ ]+` - 1回以上
    # * `[0-9]` - 半角数字の0から9
    # * `$` - 行末
    __pat = re.compile(r"^([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)([A-Z]+)$")

    @staticmethod
    def to_answer(quiz):
        m = Answerer.__pat.match(quiz)
        if m:
            # `m.group( )` - 引数の数はパターンの括弧の位置に対応
            return [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]

        return None
```

### O1o4o2o0 検索パス

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下の既存ファイルの冒頭に１行追加してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
👉  │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .o1o0g1o4o0 import Answerer as AnswererO1o0g1o4o0


# ...略...
```

### O1o4o3o0 コマンド

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```shell
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o4o0 --ac Answerer
```

Output:  

```shell
quiz:ABC123DEF456GHI
answer:['ABC', '123', 'DEF', '456', 'GHI']
correct!
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　でけたな」  

## O1o5o0 問題のパターンを増やしましょう

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　パターンの数を増やすわよ」  

### O1o5o1o0 questioner

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のファイルを新規作成しなさい」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 quest.py
    │   │   └── 📂 o1o0g1o5o0
👉  │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o4o0 --ac Answerer
"""
import random


class Questioner:
    """出題者"""

    def make_quiz(self):
        """答えのある問い作成"""
        quiz = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        # Shuffle
        quiz = ''.join(random.sample(quiz, len(quiz)))
        return quiz

    def check(self, answer, quiz):
        """答え合わせ
        Returns
        -------
        str
            Error message or None
        """
        err_list = []

        if answer is None:
            err_list.append("[Error] answer is none")
        elif len(answer) < 2:
            err_list.append(
                f"[Error] answer length is small. len:{len(answer)} (< 2)")
        else:
            is_error = False

            # もとの文字列と一致するかチェック
            text2 = ''.join(answer)
            if text2 != quiz:
                is_error = True
                err_list.append("[Error] the string is different")
                err_list.append(f"> actual  :{text2}")
                err_list.append(f"> expected:{quiz}")

            if not is_error:
                # 数字，非数字が 交互かチェック
                is_prev_numeric = answer[0].isnumeric()
                for i in range(1, len(answer)):
                    is_numeric = answer[i].isnumeric()
                    if is_prev_numeric == is_numeric:
                        # Error
                        is_error = True
                        break

                    is_prev_numeric = is_numeric

        if 0 < len(err_list):
            return "\n".join(err_list)
        else:
            return None
```

### O1o5o2o0 検索パス

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下の既存ファイルに１行足しなさい」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 quest.py
    │   │   └── 📂 o1o0g1o5o0
    │   │       └── 📄 quest.py
👉  │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .nonnumsv.o1o0g1o5o0.quest import Questioner as QuestionerO1o0g1o5o0


# ...略...
```

### O1o5o3o0 コマンド

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のコマンドを打鍵しましょう」  

Input:  

```shell
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o4o0 --ac Answerer
```

Output:  

```plaintext
quiz:8pyi0tVKZ"n|/hec\+>=BjIdS<),Pvb%3'_ax-sA?;N2#FH76&T]5[MYk(RJE`oluLO:z{DXg}U4m1rfQw@.*$C!WGq^9~
answer:None
[Error] answer is none
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　そりゃ動かないぜ。問題が変わってるからな」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　更新してくれだぜ」  

## O1o6o0 いろんなパターンに対応しようぜ？

### O1o6o1o0 answerer

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを作ってくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o6o0
👉  │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 quest.py
    │   │   └── 📂 o1o0g1o5o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o6o0 --ac Answerer
"""
import re


class Answerer:
    """Non-numeric separated value"""

    # * `^` - 文の始端
    # * `\d` - 半角数字
    # * `\d+` - 半角数字（1つ以上）
    # * `( )` - キャプチャーグループ
    __pat_num = re.compile(r"^(\d+)")
    # * `\D` - 半角数字以外
    __pat_nonnum = re.compile(r"^(\D+)")

    @staticmethod
    def to_answer(quiz):
        answer = []
        start = 0

        # 数字列か？
        m = Answerer.__pat_num.match(quiz[start:])
        if m:
            # 数字列だ
            token = m.group(1)
            answer.append(token)
            start += len(token)

        while True:
            # 非数字の文字列か？
            m = Answerer.__pat_nonnum.match(quiz[start:])
            if m is None:
                break

            # 非数字の文字列だ
            token = m.group(1)
            answer.append(token)
            start += len(token)

            # 数字列か？
            m = Answerer.__pat_num.match(quiz[start:])
            if m is None:
                break

            # 数字列だ
            token = m.group(1)
            answer.append(token)
            start += len(token)

        return answer
```

### O1o6o2o0 検索パス

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下の既存ファイルの冒頭に１行追加してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o6o0
    │   │   │   └── 📄 __init__.py
👉  │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 quest.py
    │   │   └── 📂 o1o0g1o5o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .o1o0g1o6o0 import Answerer as AnswererO1o0g1o6o0


# ...略...
```

### O1o6o3o0 コマンド

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```plaintext
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o6o0 --ac Answerer
```

Output:  

```plaintext
quiz:n*;7'Ip{DKr\A6c&SuW"T=U^)3#PxwN0h$]?La!zsV/1[YjJ49tZ`dRO(_Cm,glef5.%2bkXGQqy|~-Fi8v:BM}>oE<+H@
answer:['n*;', '7', "'Ip{DKr\\A", '6', 'c&SuW"T=U^)', '3', '#PxwN', '0', 'h$]?La!zsV/', '1', '[YjJ', '49', 'tZ`dRO(_Cm,glef', '5', '.%', '2', 'bkXGQqy|~-Fi', '8', 'v:BM}>oE<+H@']
correct!
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　答えは合ってるみたいだが、本当に合ってんのかな？」  

## O1o7o0 間違った答えを返そうぜ？

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　じゃあ、わざと答えの一部を　スワップ（入れ替え）して　答えればいいんだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　テストを試そうってのね」  

### O1o7o1o0 answerer

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを新規作成してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o6o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o7o0
👉  │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 quest.py
    │   │   └── 📂 o1o0g1o5o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o7o0 --ac Answerer
"""
import re
import random

from ..o1o0g1o6o0 import Answerer as AnswererG1o6o0
#    ------------        --------    --------------
#    1                   2           3
# 1. 隣のフォルダー
# 2. クラス
# 3. 別名


class Answerer:
    """Non-numeric separated value"""

    # * `^` - 文の始端
    # * `\d` - 半角数字
    # * `\d+` - 半角数字（1つ以上）
    # * `( )` - キャプチャーグループ
    __pat_num = re.compile(r"^(\d+)")
    # * `\D` - 半角数字以外
    __pat_nonnum = re.compile(r"^(\D+)")

    @staticmethod
    def to_answer(quiz):
        answer = AnswererG1o6o0.to_answer(quiz)

        # 要素数
        length = len(answer)

        # 要素が２個に満たなければスワップできません
        if length <= 2:
            raise ValueError(f"Couldn't swap. length:{length}")

        # ランダムなインデックスを２つ取得
        i1 = random.randint(1, length-1)
        i2 = random.randint(0, i1-1)

        # スワップ
        temp = answer[i1]
        answer[i1] = answer[i2]
        answer[i2] = temp

        return answer
```

### O1o7o2o0 検索パス

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下の既存ファイルの冒頭に１行追加してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o6o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o7o0
    │   │   │   └── 📄 __init__.py
👉  │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   └── 📂 o1o0g1o1o0
    │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 quest.py
    │   │   └── 📂 o1o0g1o5o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .o1o0g1o7o0 import Answerer as AnswererO1o0g1o7o0


# ...略...
```

### O1o7o3o0 コマンド

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```plaintext
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o7o0 --ac Answerer
```

Output:  

```plaintext
quiz:eV0LI6Ep-AT=[@f,\}">d#:xn/|$t47WORZ.%rN&Kq3;1lQm]9s*5J`bCuG~!oDz8kgF<(+j_ivyc?w^hMP2HUBY'XS{a)
answer:['eV', '0', 'Ep-AT=[@f,\\}">d#:xn/|$t', '6', 'LI', '47', 'WORZ.%rN&Kq', '3', ';', '1', 'lQm]', '9', 's*', '5', 'J`bCuG~!oDz', '8', 
'kgF<(+j_ivyc?w^hMP', '2', "HUBY'XS{a)"]
[Error] the string is different
> actual  :eV0Ep-AT=[@f,\}">d#:xn/|$t6LI47WORZ.%rN&Kq3;1lQm]9s*5J`bCuG~!oDz8kgF<(+j_ivyc?w^hMP2HUBY'XS{a)
> expected:eV0LI6Ep-AT=[@f,\}">d#:xn/|$t47WORZ.%rN&Kq3;1lQm]9s*5J`bCuG~!oDz8kgF<(+j_ivyc?w^hMP2HUBY'XS{a)
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　スワップしたのだから、エラーになって当然よ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　いつも正解って言ったり、いつも間違いというようなプログラムでないことは　分かったが……」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　そんなプログラム、きふわらべ　みたいだな」  

## O1o8o0 連続テストしようぜ？

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　テストしたいプログラムを１００回、　わざと間違えるプログラムを１００回、  
ランダムな順序で実行して、
テストしたいプログラムの答えが正解の回数、わざと間違えるプログラムの答えが間違いの回数を加算して、
実行回数当たりの　ちゃんと動いた回数の割合を出してくれだぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　じゃあ 100回ずつと言わず、 計2000回やって、小数点１桁の精度の百分率を出すかだぜ」  

### O1o8o1o0 answerer

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを新規作成してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o2o0    
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o4o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o6o0
    │   │   │   └── 📄 __init__.py
    │   │   ├── 📂 o1o0g1o7o0
    │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │   ├── 📂 general
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 test.py
    │   │   └── 📂 o1o0g1o8o0
👉  │   │       └── 📄 test.py
    │   ├── 📂 nonnumsv
    │   │   ├── 📂 o1o0g1o1o0
    │   │   │   └── 📄 quest.py
    │   │   └── 📂 o1o0g1o5o0
    │   │       └── 📄 quest.py
    │   └── 📄 __init__.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
```

おわり