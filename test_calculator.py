#!/usr/bin/env python3
"""
計算機のテストスクリプト
バグの発見に使用
"""

from calculator import Calculator

def test_basic_operations():
    """基本操作のテスト"""
    calc = Calculator()
    
    print("=== 基本操作のテスト ===")
    assert calc.add(2, 3) == 5, "加算のテスト失敗"
    assert calc.subtract(10, 4) == 6, "減算のテスト失敗"
    assert calc.multiply(3, 4) == 12, "乗算のテスト失敗"
    assert calc.divide(15, 3) == 5.0, "除算のテスト失敗"
    print("✓ 基本操作のテストは全て成功")

def test_power_operations():
    """べき乗操作のテスト（バグがある）"""
    calc = Calculator()
    
    print("\n=== べき乗操作のテスト ===")
    
    # 正の指数のテスト
    result1 = calc.power(2, 3)
    expected1 = 8
    print(f"2^3 = {result1} (期待値: {expected1})")
    assert result1 == expected1, "正の指数のテスト失敗"
    
    # 負の指数のテスト（ここでバグが発現）
    result2 = calc.power(5, -2)
    expected2 = 0.04  # 5^(-2) = 1/25 = 0.04
    print(f"5^(-2) = {result2} (期待値: {expected2})")
    
    if result2 != expected2:
        print("❌ バグ1発見！負の指数の計算が間違っています")
        print(f"   実際の結果: {result2}")
        print(f"   期待される結果: {expected2}")
    else:
        print("✓ 負の指数のテストは成功")

def test_square_root_operations():
    """平方根操作のテスト"""
    calc = Calculator()
    
    print("\n=== 平方根操作のテスト ===")
    
    # 正の数の平方根テスト
    result1 = calc.square_root(9)
    expected1 = 3.0
    print(f"√9 = {result1} (期待値: {expected1})")
    assert result1 == expected1, "正の平方根のテスト失敗"
    
    # 負の数の平方根テスト（ここでバグが発現）
    try:
        result2 = calc.square_root(-4)
    except ValueError as e:
        print("❌ バグ2発見！負の数の平方根が適切に処理されていません")
        print(f"   エラー: {e}")

def test_integer_division():
    """整数除算のテスト（バグがある）"""
    calc = Calculator()
    
    print("\n=== 整数除算のテスト ===")
    
    # 整数除算のテスト（切り捨てを期待）
    result1 = calc.divide_integer(7, 2)
    expected1 = 3  # 7/2 = 3.5 → 切り捨てで3になるべき
    print(f"7 ÷ 2 (整数) = {result1} (期待値: {expected1})")
    
    if result1 != expected1:
        print("❌ バグ3発見！整数除算で四捨五入されています（切り捨てであるべき）")
        print(f"   実際の結果: {result1}")
        print(f"   期待される結果: {expected1}")
    else:
        print("✓ 整数除算のテストは成功")

def main():
    """メイン関数"""
    try:
        test_basic_operations()
        test_power_operations()
        test_square_root_operations()
        test_integer_division()
        
        print("\n=== テスト結果 ===")
        print("✓ 基本機能は正常")
        print("❌ 3つのバグが発見されました：")
        print("  1. べき乗の負の指数処理")
        print("  2. 平方根の負数処理")
        print("  3. 整数除算の丸め処理")
        
    except AssertionError as e:
        print(f"テストエラー: {e}")
    except Exception as e:
        print(f"予期しないエラー: {e}")

if __name__ == "__main__":
    main()