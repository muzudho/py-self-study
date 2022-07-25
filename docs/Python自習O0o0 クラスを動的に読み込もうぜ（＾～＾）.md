# O_9o0 以前の記事

📖 [Python自習O_9o0 目次だぜ（＾～＾）](https://crieit.net/posts/Python-62de8a581dbea) - 目次  

# O0o0 今回の記事

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　Python でクラスを動的に読み込むの、どうやるんだぜ？」  

📖 [How to Dynamically Load Modules or Classes in Python](https://www.geeksforgeeks.org/how-to-dynamically-load-modules-or-classes-in-python/)  
📖 [How to dynamically load a Python class](https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class)  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de69e692e4f.png)  
「　👆　ググれだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de69fef19a3.png)  
「　いろんな記事があって　どれがベストプラクティスか分かんないのよね」  

# O1o0 クラスの静的インポート

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　まず　ふつうにクラスをロードしてみようぜ。  
👇 以下のファイルを作成してくれだぜ」  

```plaintext
    └── 📂 src
        └── 📂 hello
👉          └── 📄 __init__.py
```

```py
class Hello:
    def __init__():
        pass

    @classmethod
    @property
    def message(clazz):
        return "Hello, world!!"
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　次に  
👇 以下のファイルを作成してくれだぜ」  

```plaintext
    ├── 📂 src
    │   └── 📂 hello
    │       └── 📄 __init__.py
    └── 📂 tests
👉      └── 📄 hello_test.py
```

```py
"""
python -m tests.hello_test
"""
from src.hello import Hello

print(Hello.message)
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　じゃあ  
👇 以下のコマンドを打鍵してくれだぜ」  

Input:  

```py
python -m tests.hello_test
```

Output:  

```plaintext
Hello, world!!
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　これが　よくやるクラスのロードだぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de69e692e4f.png)  
「　これだと `from src.hello import Hello` と、クラスの名前が埋め込んであるから、このクラスを読み込むな」  

# O2o0 クラスの動的インポート

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de69fef19a3.png)  
「　そのファイルか、クラスの名前を コマンドラインから指定したいのよ。  
例えば」  

```shell
python -m tests.hello_test src.welcome
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de69fef19a3.png)  
「　👆 みたいな感じにできないの？」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de69e692e4f.png)  
「　from ～ import 文の名前ストラクチャーを教えてくれだぜ」  

```plaintext
from src.hello import Hello
     ---------        -----
     1                2
1. module name
2. class name
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👆 これが代表的な例だぜ。こうじゃないケースもあるが今は省くぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de69e692e4f.png)  
「　じゃあ」  

```plaintext
obj = load( module_name, class_name)
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de69e692e4f.png)  
「　👆　こんな感じで　クラスのインスタンスを取得できる関数が作れればいいわけかだぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👇 サンプルコードを真似ようぜ。  
以下のファイルを作成してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 dimport
👉  │   │   └── 📄 __init__.py
    │   └── 📂 hello
    │      └── 📄 __init__.py
    └── 📂 tests
        └── 📄 hello_test.py
```

```py
"""
📖 [How to Dynamically Load Modules or Classes in Python](https://www.geeksforgeeks.org/how-to-dynamically-load-modules-or-classes-in-python/)  
📖 [How to dynamically load a Python class](https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class)  
"""


class Dimport:
    @staticmethod
    def load(module_name, class_name):
        # __import__ method used
        # to fetch module
        module = Dimport.load_module(module_name)

        # getting attribute by
        # getattr() method
        return getattr(module, class_name)

    @staticmethod
    def load_module(name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)

        return mod
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👇 サンプルコードを真似ようぜ。  
以下のファイルを作成してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 dimport
    │   │   └── 📄 __init__.py
    │   └── 📂 hello
    │      └── 📄 __init__.py
    └── 📂 tests
👉      ├── 📄 dimport_test.py
        └── 📄 hello_test.py
```

```py
"""
python -m tests.dimport_test
"""
from src.dimport import Dimport

print(Dimport.load("src.hello", "Hello").message)
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👇　以下のコマンドを打鍵してくれだぜ」  

Input:  

```py
python -m tests.dimport_test
```

Output:  

```plaintext
AttributeError: module 'src' has no attribute 'hello'
```

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462de69e692e4f.png)  
「　👆 `src` は `hello` なんか持ってない、というエラーが出たぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　動的にインポートするときは　ディレクトリーを自動で検索してくれないのか。じゃあ 手動で設定しようぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👇 以下のファイルを作成してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 dimport
    │   │   └── 📄 __init__.py
    │   ├── 📂 hello
    │   │  └── 📄 __init__.py
👉  │   └── 📄 __init__.py
    └── 📂 tests
        ├── 📄 dimport_test.py
        └── 📄 hello_test.py
```

```py
from .hello import Hello
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👆 `src` が何を持ってるか 書いてやればいいわけだぜ」  

Input:  

```py
python -m tests.dimport_test
```

Output:  

```py
Hello, world!!
```

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762de69fef19a3.png)  
「　👆 クラスの動的読取はできそうね」

# O3o0 コマンドライン引数に対応

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👇 以下のファイルを作成してくれだぜ」  

```plaintext
    ├── 📂 src
    │   ├── 📂 dimport
    │   │   └── 📄 __init__.py
    │   ├── 📂 hello
    │   │  └── 📄 __init__.py
    │   └── 📄 __init__.py
    └── 📂 tests
        ├── 📄 dimport_test.py
👉      ├── 📄 dimport_test2.py
        └── 📄 hello_test.py
```

```py
"""
python -m tests.dimport_test2 -m src.hello -c Hello
"""
import argparse
from src.dimport import Dimport

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-m', help='module')
ap.add_argument('-c', help='class')
args = ap.parse_args()

print(Dimport.load(args.m, args.c).message)
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👇　以下のコマンドを打鍵してくれだぜ」  

Input:  

```py
python -m tests.dimport_test2 -m src.hello -c Hello
```

Output:  

```py
Hello, world!!
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62de69c8ba5ab.png)  
「　👆　でけたな」

# 次の記事

📖 [Python自習O1o0 Non-numeric Separated Value](https://crieit.net/posts/Python-O1o0-Non-numeric-Separated-Value)  

# 関連する記事

📖 [Python自習O_9o0 目次だぜ（＾～＾）](https://crieit.net/posts/Python-62de8a581dbea)  

おわり