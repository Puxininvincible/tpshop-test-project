import pandas as pd
import json
import os


def excel_to_json(excel_path, json_path, blank_as_null=True):
    """
    将 Excel 转换为 JSON
    :param excel_path: Excel 文件路径
    :param json_path: 输出 JSON 文件路径
    :param blank_as_null: 空白单元格是否转为 null（True→null，False→""）
    """
    # 1. 读取 Excel，指定所有列按字符串读取（避免前导零丢失）
    # dtype=str 确保所有数据按文本读取，保留前导零和原始格式
    df = pd.read_excel(excel_path, dtype=str)

    # 2. 处理空白单元格
    if blank_as_null:
        # 空白单元格→NaN→转换为 None（JSON 中为 null）
        df = df.where(pd.notna(df), None)
    else:
        # 空白单元格→空字符串 ""
        df = df.fillna("")

    # 3.将 success 列的字符串转为布尔值
    if "success" in df.columns:  # 确保列存在
        # 转换逻辑："true"→True，"false"→False（忽略大小写）
        df["success"] = df["success"].str.lower().map({"true": True, "false": False})

    # 4. 转换为 JSON 并保存
    # 确保输出目录存在
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        # orient="records" 输出列表格式 [{}, {}, ...]
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=2)

    print(f"转换完成！JSON 文件保存至：{json_path}")


# 示例：转换你的测试数据
if __name__ == "__main__":
    # Excel 路径（替换为你的文件路径）
    excel_file = r"C:\Users\Administrator\Desktop\邮箱注册测试用例数据.xlsx"
    # 输出 JSON 路径
    json_file = r"C:\Users\Administrator\Desktop\tpshop项目实战 - 副本\tpshop_auto_test\data\register_email.json"
    # 转换（blank_as_null=True 表示空白单元格→null，False 则→""）
    excel_to_json(excel_file, json_file, blank_as_null=False)