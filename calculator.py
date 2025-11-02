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
    
    print("\n計算履歴:")
    for entry in calc.get_history():
        print(f"  {entry}")

if __name__ == "__main__":
    main()