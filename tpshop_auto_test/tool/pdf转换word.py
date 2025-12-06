from pdf2docx import Converter
import os


def pdf_to_word(pdf_path, word_path=None):
    """
    将PDF文件转换为Word文件

    参数:
        pdf_path: PDF文件的路径
        word_path: 输出Word文件的路径，默认为与PDF同目录同名称的.docx文件
    """
    # 检查PDF文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误：PDF文件 '{pdf_path}' 不存在")
        return

    # 如果未指定Word路径，则生成默认路径
    if not word_path:
        # 获取PDF文件的目录和文件名（不含扩展名）
        pdf_dir = os.path.dirname(pdf_path)
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        word_path = os.path.join(pdf_dir, f"{pdf_name}.docx")

    try:
        # 创建转换器实例
        cv = Converter(pdf_path)
        # 转换PDF到Word
        cv.convert(word_path, start=0, end=None)  # start和end参数用于指定转换的页码范围
        cv.close()
        print(f"转换成功！Word文件已保存至：{word_path}")
    except Exception as e:
        print(f"转换失败：{str(e)}")


if __name__ == "__main__":
    # 示例：转换单个PDF文件
    pdf_file = input("请输入PDF文件路径：").strip()
    pdf_to_word(pdf_file)

    # 如需批量转换，可以使用以下代码（取消注释并修改路径）
    # pdf_dir = "存放PDF的目录路径"
    # for filename in os.listdir(pdf_dir):
    #     if filename.endswith(".pdf"):
    #         pdf_path = os.path.join(pdf_dir, filename)
    #         pdf_to_word(pdf_path)