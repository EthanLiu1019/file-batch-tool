import os

def batch_rename(folder_path, prefix="file_", start=1):
    """
    批量重命名文件
    :param folder_path: 文件夹路径
    :param prefix: 新文件名前缀
    :param start: 起始编号
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"路径不存在或不是文件夹: {folder_path}")

    files = os.listdir(folder_path)
    count = start
    for filename in files:
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            ext = os.path.splitext(filename)[1]  # 保留原扩展名
            new_name = f"{prefix}{count}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"重命名: {filename} → {new_name}")
            count += 1

