import os
import shutil

def copy_files_with_prefix(source_folder):
    # 遍历源文件夹中的所有子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 获取当前文件的完整路径
            file_path = os.path.join(root, file)
            # 计算相对路径，用于构造新文件名
            relative_path = os.path.relpath(file_path, source_folder)
            # 分割相对路径得到子文件夹部分和文件名
            dirs_only, filename = os.path.split(relative_path)
            # 构建新文件名：子文件夹前缀 + 文件名
            new_filename = f"{dirs_only.replace(os.sep, '-')}-{filename}"
            # 目标文件的完整路径（在根目录下）
            destination_file_path = os.path.join(source_folder, new_filename)
            
            # 复制文件到根目录并重命名
            shutil.copy2(file_path, destination_file_path)

# 使用函数，指定源文件夹路径
source_folder = 'D:\\tes\\99things\\source\\99things\\img'  # 请替换为你的源文件夹路径
copy_files_with_prefix(source_folder)
