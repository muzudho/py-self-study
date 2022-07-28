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
「　👇 テストを書いて置いたから、これに合うようにコードを書きなさい」  

```plaintext
    ├── 📂 tests
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
👉  │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv -c NonNumSVO1o0g1o2o0
"""
import argparse
from src.dimport import Dimport

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-m', help='module')
ap.add_argument('-c', help='class')
args = ap.parse_args()

# Dynamic class import
NonNumSV = Dimport.load(args.m, args.c)

# Code
vec = NonNumSV.parse("ABC123DEF456GHI")

if vec is None:
    print("[Error] vec is none")
else:
    vec_size = len(vec)
    if vec_size == 5:
        print("size is ok")
    else:
        print(f"[Error] the size is different. size:{vec_size}")

    if vec == ["ABC", "123", "DEF", "456", "GHI"]:
        print("correct!")
    else:
        print(f"[Error] the response is different. vec:{vec}")
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　フーン　じゃあ　スケルトンから作るか」  

## O1o2o0 Skeleton

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを作ってくれだぜ」  

```plaintext
    ├── 📂 src
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o2o0    
👉  │           └── 📄 __init__.py
    ├── 📂 tests
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
class NonNumSVO1o0g1o2o0:
    """Non-numeric separated value"""

    @staticmethod
    def parse(text):
        return []
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のファイルを作ってくれだぜ」  

```plaintext
    ├── 📂 src
    │   └── 📂 nonnumsv
    │       ├── 📂 o1o0g1o2o0    
    │       │   └── 📄 __init__.py
👉  │       └── 📄 __init__.py
    ├── 📂 tests
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
from .o1o0g1o2o0 import NonNumSVO1o0g1o2o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 前のレッスンで作った、以下の既存ファイルに１行追加してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │       ├── 📂 o1o0g1o2o0    
    │       │   └── 📄 __init__.py
    │       └── 📄 __init__.py
👉  │   └── 📄 __init__.py
    ├── 📂 tests
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .nonnumsv.o1o0g1o2o0 import NonNumSVO1o0g1o2o0
```

### O1o2o1o0 コマンド実行

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 このコマンドを実行すると」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o2o0 -c NonNumSVO1o0g1o2o0
```

Output:  

```shell
[Error] the size is different. size:0
[Error] the response is different. vec:[]
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👆 エラーが出るわけだな」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　`parse` 静的メソッドを実装しろだぜ」

## O1o3o0 まず、そのまま出そうぜ

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
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
class NonNumSVO1o0g1o3o0:
    """Non-numeric separated value"""

    @staticmethod
    def parse(text):
        return ["ABC", "123", "DEF", "456", "GHI"]
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　お父んのフォルダー名の付け方　狂ってて　わらう」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　クラス名の付け方も　狂ってるわよ」  

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
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
from .o1o0g1o3o0 import NonNumSVO1o0g1o3o0


# ...略...
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　モジュールの検索パスを 手動で書くの めんどくさいけど 仕方ない」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o3o0 -c NonNumSVO1o0g1o3o0
```

Output:  

```shell
size is ok
correct!
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　そりゃ正解よ」  

## O1o4o0 正規表現を使って出そうぜ

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　今までは　練習の枠組みを用意したわけだぜ。  
ここからが本番だぜ」  

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
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSVO1o0g1o4o0
"""
import re


class NonNumSVO1o0g1o4o0:
    """Non-numeric separated value"""

    __pat = re.compile(r"^([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)([A-Z]+)$")

    @staticmethod
    def parse(text):
        m = NonNumSVO1o0g1o4o0.__pat.match(text)
        if m:
            return [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]

        return None
```

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
    │   └── 📂 nonnumsv
    │       └── 📂 o1o0g1o1o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .o1o0g1o4o0 import NonNumSVO1o0g1o4o0


# ...略...
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSVO1o0g1o4o0
```

Output:  

```shell
size is ok
correct!
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　でけたな」  

## O1o5o0 Questioner 出題を増やしましょう

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　パターンの数を増やすわよ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のファイルを作りなさい」  

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
    │   └── 📂 nonnumsv
    │       ├── 📂 o1o0g1o1o0
    │       │   └── 📄 test.py
    │       └── 📂 o1o0g1o5o0
👉  │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv -c NonNumSVO1o0g1o4o0
"""
import argparse
import random
from src.dimport import Dimport

# Command line arguments
# ----------------------
ap = argparse.ArgumentParser()
ap.add_argument('-m', help='module')
ap.add_argument('-c', help='class')
args = ap.parse_args()

# Dynamic class import
# --------------------
NonNumSV = Dimport.load(args.m, args.c)

# Question
# --------
characters = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
# Shuffle
characters = ''.join(random.sample(characters, len(characters)))
print(f"question:{characters}")

# Answer
# ------
vec = NonNumSV.parse(characters)
print(f"answer:{vec}")

# Check
# -----
if vec is None:
    print("[Error] vec is none")
elif len(vec) < 2:
    print(f"[Error] vec length is small. len:{len(vec)} (< 2)")
else:
    is_error = False
    is_prev_numeric = vec[0].isnumeric()
    for i in range(1, len(vec)):
        is_numeric = vec[i].isnumeric()
        if is_prev_numeric == is_numeric:
            # Error
            is_error = True
            print(f"[Error] elements:{vec[i-1]}, {vec[i]}")
            break

    if not is_error:
        print("correct!")
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のコマンドを打鍵しましょう」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv -c NonNumSVO1o0g1o4o0
```

Output:  

```plaintext
[Error] vec is none
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　そりゃ動かないぜ。問題が変わってるからな」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　更新してくれだぜ」  

## O1o6o0 いろんなパターンに対応しようぜ？

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
    │   └── 📂 nonnumsv
    │       ├── 📂 o1o0g1o1o0
    │       │   └── 📄 test.py
    │       └── 📂 o1o0g1o5o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o6o0 -c NonNumSVO1o0g1o6o0
"""
import re


class NonNumSVO1o0g1o6o0:
    """Non-numeric separated value"""

    # * `^ $` - 文の始端から終端まで
    # * `\d` - 半角数字
    # * `\D` - 半角数字以外
    # * `(?: )` - ただの括弧
    # * `( )?` - グループ，ただし省略可
    # * `( )*` - グループ，0個以上にマッチ
    __pat = re.compile(r"^(?:(\D+)?(\d+)?)*$")

    @staticmethod
    def parse(text):
        m = NonNumSVO1o0g1o6o0.__pat.match(text)

        if m:
            # タプルをリストに変換
            return list(m.groups())

        return None
```

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
    │   └── 📂 nonnumsv
    │       ├── 📂 o1o0g1o1o0
    │       │   └── 📄 test.py
    │       └── 📂 o1o0g1o5o0
    │           └── 📄 test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
from .o1o0g1o6o0 import NonNumSVO1o0g1o6o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```plaintext
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o6o0 -c NonNumSVO1o0g1o6o0
```

Output:  

```plaintext
question:.b>1k"HOFA^a+,0deofG%@_{J<2`8Q}XtN=g?Vsn!p63E9Shqx[$Kc#i4;RUjL~CY5M7W(Py:rB/v]-|&)*Tl'\IDuZzwm
answer:["W(Py:rB/v]-|&)*Tl'\\IDuZzwm", '7']
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　文字数が足りてないぜ」  

おわり