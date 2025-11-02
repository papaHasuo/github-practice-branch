#!/usr/bin/env python3
"""
シンプルな計算機アプリケーション
基本的な四則演算をサポート
"""

class Calculator:
    """基本的な計算機クラス"""
    
    def __init__(self):
        """計算機の初期化"""
        self.result = 0
        self.history = []
    
    def add(self, a, b):
        """加算"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """減算"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乗算"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除算"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """べき乗（バグ含む）"""
        # BUG: 負の指数の処理が間違っている
        if b < 0:
            result = a ** b  # 本来はa ** (-b)の逆数を返すべき
            result = result * -1  # 間違った処理：負数を掛けている
        else:
            result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def square_root(self, a):
        """平方根"""
        import math
        if a < 0:
            raise ValueError("負の数の平方根は計算できません")
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def divide_integer(self, a, b):
        """整数除算（バグ含む）"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        # BUG: 切り捨て除算のつもりが四捨五入になっている
        result = round(a / b)  # 本来はint(a / b)または a // b を使うべき
        self.history.append(f"{a} ÷ {b} (整数) = {result}")
        return result
    
    def percentage(self, value, total):
        """パーセンテージ計算"""
        if total == 0:
            raise ValueError("全体の値がゼロの場合、パーセンテージは計算できません")
        result = (value / total) * 100
        self.history.append(f"{value} / {total} × 100 = {result}%")
        return result
    
    def get_history(self):
        """計算履歴を取得"""
        return self.history.copy()
    
    def clear_history(self):
        """計算履歴をクリア"""
        self.history.clear()

def main():
    """メイン関数"""
    calc = Calculator()
    
    print("=== シンプル計算機 ===")
    print("使用例:")
    
    # 計算例
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    # 新機能：べき乗（バグ含む）
    print(f"2 ^ 3 = {calc.power(2, 3)}")
    print(f"5 ^ -2 = {calc.power(5, -2)}")  # ここでバグが発生
    
    # 新機能：平方根（バグ含む）
    print(f"√9 = {calc.square_root(9)}")
    try:
        print(f"√-4 = {calc.square_root(-4)}")  # ここでバグが発生
    except ValueError as e:
        print(f"エラー: {e}")
    
    # 新機能：整数除算（バグ含む）
    print(f"7 ÷ 2 (整数) = {calc.divide_integer(7, 2)}")  # バグ: 3.5が4に丸められる
    
    # 新機能：パーセンテージ計算
    print(f"25 / 100 = {calc.percentage(25, 100)}%")
    print(f"75 / 200 = {calc.percentage(75, 200)}%")
    
    print("\n計算履歴:")
    for entry in calc.get_history():
        print(f"  {entry}")

if __name__ == "__main__":
    main()