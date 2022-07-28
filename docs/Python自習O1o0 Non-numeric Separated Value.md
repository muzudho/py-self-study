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
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o2o0 -c NonNumSV
"""
import argparse
from src.dimport import Dimport


def solve(quiz):
    """解く"""

    # Command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-m', help='module')
    ap.add_argument('-c', help='class')
    args = ap.parse_args()

    # Dynamic class import
    NonNumSV = Dimport.load(args.m, args.c)

    return NonNumSV.parse(quiz)


def check(answer):
    """答え合わせ"""

    if answer is None:
        print("[Error] vec is none")
    else:
        vec_size = len(answer)
        if vec_size == 5:
            print("size is ok")
        else:
            print(f"[Error] the size is different. size:{vec_size}")

        if answer == ["ABC", "123", "DEF", "456", "GHI"]:
            print("correct!")
        else:
            print(f"[Error] the response is different. vec:{answer}")


# Do!
answer = solve(quiz="ABC123DEF456GHI")

# Check!
check(answer)
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
class NonNumSV:
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
from .o1o0g1o2o0 import NonNumSV as NonNumSVO1o0g1o2o0
#    -----------        --------    ------------------
#    1                  2           3
# 1. 同じディレクトリーにある o1o0g1o2o0 ディレクトリー
# 2. クラス
# 3. クラスの別名
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


from .nonnumsv.o1o0g1o2o0 import NonNumSV
```

### O1o2o1o0 コマンド実行

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 このコマンドを実行すると」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o2o0 -c NonNumSV
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
class NonNumSV:
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
# ...略...


from .o1o0g1o3o0 import NonNumSV as NonNumSVO1o0g1o3o0


# ...略...
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　モジュールの検索パスを 手動で書くの めんどくさいけど 仕方ない」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o3o0 -c NonNumSV
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
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSV
"""
import re


class NonNumSV:
    """Non-numeric separated value"""

    __pat = re.compile(r"^([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)([A-Z]+)$")

    @staticmethod
    def parse(text):
        m = NonNumSV.__pat.match(text)
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


from .o1o0g1o4o0 import NonNumSV as NonNumSVO1o0g1o4o0


# ...略...
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSV
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
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSV
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

    # もとの文字列と一致するかチェック
    text2 = ''.join(vec)
    if text2 != characters:
        is_error = True
        print("[Error] the string is different")
        print(f"> actual  :{text2}")
        print(f"> expected:{characters}")

    if not is_error:
        # 数字，非数字が 交互かチェック
        is_prev_numeric = vec[0].isnumeric()
        for i in range(1, len(vec)):
            is_numeric = vec[i].isnumeric()
            if is_prev_numeric == is_numeric:
                # Error
                is_error = True
                break

            is_prev_numeric = is_numeric

    if not is_error:
        print("correct!")
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　👇 以下のコマンドを打鍵しましょう」  

Input:  

```shell
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSV
```

Output:  

```plaintext
question:w_d4,D5P`ZoSk~J"ztA@2h6n=Wr<0E7$IF:{*gvXK-ci)]H(es;y/j+f1qbC?NV!'%}&.x\#aQR8B3TlLY^U|Gmpu[9MO>
answer:None
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
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o6o0 -c NonNumSV
"""
import re


class NonNumSV:
    """Non-numeric separated value"""

    # * `^` - 文の始端
    # * `\d` - 半角数字
    # * `\d+` - 半角数字（1つ以上）
    # * `( )` - キャプチャーグループ
    __pat_num = re.compile(r"^(\d+)")
    # * `\D` - 半角数字以外
    __pat_nonnum = re.compile(r"^(\D+)")

    @staticmethod
    def parse(text):
        vec = []
        start = 0

        # 数字列か？
        m = NonNumSV.__pat_num.match(text[start:])
        if m:
            # 数字列だ
            token = m.group(1)
            vec.append(token)
            start += len(token)

        while True:
            # 非数字の文字列か？
            m = NonNumSV.__pat_nonnum.match(text[start:])
            if m is None:
                break

            # 非数字の文字列だ
            token = m.group(1)
            vec.append(token)
            start += len(token)

            # 数字列か？
            m = NonNumSV.__pat_num.match(text[start:])
            if m is None:
                break

            # 数字列だ
            token = m.group(1)
            vec.append(token)
            start += len(token)

        return vec
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
# ...略...


from .o1o0g1o6o0 import NonNumSV as NonNumSVO1o0g1o6o0


# ...略...
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```plaintext
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o6o0 -c NonNumSV
```

Output:  

```plaintext
question:Vq&Rrj$g6_%)|A;Fa`oH]OY}QK8.,9hG[vN<3i^1IbS?C/LPXJwDU@xWn\7!E+k'0f(t{>ue5=Tl*:Zmc#Bp-2d"yzM~s4
answer:['Vq&Rrj$g', '6', '_%)|A;Fa`oH]OY}QK', '8', '.,', '9', 'hG[vN<', '3', 'i^', '1', 'IbS?C/LPXJwDU@xWn\\', '7', "!E+k'", '0', 'f(t{>ue', '5', '=Tl*:Zmc#Bp-', '2', 'd"yzM~s', '4']
correct!
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de6041600db.png)  
「　答えは合ってるみたいだが、本当に合ってんのかな？」  

## O1o7o0 間違った答えを返そうぜ？

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　じゃあ、わざと答えの一部を　スワップ（入れ替え）して　答えればいいんだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de606300faf.png)  
「　テストを試そうってのね」  

おわり