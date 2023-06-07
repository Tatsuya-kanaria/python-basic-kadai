# クラスの定義（例：class Product: ...... ）
class クラス名:
    # コンストラクタの定義
    def __init__(self, name, etc):
        # 初期化の内容
        self.name = name
        self.etc = etc

    # メソッドの定義（例：public show_name(): ...... ）
    # def メソッド名():
        # 一連の処理

    def set_name(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

# インスタンス化（例：shampoo = Product()）
インスタンス名 = クラス名()

# プロパティへのアクセス（例：shampoo.name）
インスタンス名.プロパティ名

# メソッドへのアクセス（例：shampoo.show_name()）
インスタンス名.メソッド名()
