import os
import zipfile

def zip_folder(folder_path, output_path=None):
    """
    将指定文件夹打包为 zip 文件
    :param folder_path: 要打包的文件夹路径
    :param output_path: 输出 zip 文件路径（默认与文件夹同名）
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"路径不存在或不是文件夹: {folder_path}")

    if output_path is None:
        output_path = folder_path.rstrip("/\\") + ".zip"

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)
                print(f"添加到压缩包: {arcname}")

    print(f"打包完成: {output_path}")
