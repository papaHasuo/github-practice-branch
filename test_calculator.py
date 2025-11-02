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
        print("❌ バグ発見！負の指数の計算が間違っています")
        print(f"   実際の結果: {result2}")
        print(f"   期待される結果: {expected2}")
    else:
        print("✓ 負の指数のテストは成功")

def main():
    """メイン関数"""
    try:
        test_basic_operations()
        test_power_operations()
    except AssertionError as e:
        print(f"テストエラー: {e}")
    except Exception as e:
        print(f"予期しないエラー: {e}")

if __name__ == "__main__":
    main()