# O_9o0 前回の記事

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
👉  │    └── 📄 nonnumsv_test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
"""
python -m tests.nonnumsv_test -m src.nonnumsv -c NonNumSVO1o0g1o2o0
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
👉  │       └── 📄 __init__.py
    ├── 📂 tests
    │    └── 📄 nonnumsv_test.py
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
「　👇 以下の既存ファイルに１行追加してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 nonnumsv
    │   │   └── 📄 __init__.py
👉  │   └── 📄 __init__.py
    ├── 📂 tests
    │    └── 📄 nonnumsv_test.py
    ├── 📄 .gitignore
    ├── 📄 LICENSE
    └── 📄 README.md
```

```py
# ...略...


from .nonnumsv import NonNumSVO1o0g1o2o0
```

### O1o2o1o0 コマンド実行

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de6036b15fb.png)  
「　👇 このコマンドを実行すると」  

Input:  

```shell
python -m tests.nonnumsv_test -m src.nonnumsv -c NonNumSVO1o0g1o2o0
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
    │   │   ├── 📂 o1o0g1o3o0
👉  │   │   │   └── 📄 __init__.py
    │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │    └── 📄 nonnumsv_test.py
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
    │   │   ├── 📂 o1o0g1o3o0
    │   │   │   └── 📄 __init__.py
👉  │   │   └── 📄 __init__.py
    │   └── 📄 __init__.py
    ├── 📂 tests
    │    └── 📄 nonnumsv_test.py
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
python -m tests.nonnumsv_test -m src.nonnumsv.o1o0g1o3o0 -c NonNumSVO1o0g1o3o0
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

おわり
