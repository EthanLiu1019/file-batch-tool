import os
import click
import fnmatch

def parse_size(size_str):
    """解析大小字符串，如 100KB, 10MB"""
    units = {"B":1, "KB":1024, "MB":1024**2, "GB":1024**3}
    size_str = size_str.upper()
    for unit in units:
        if size_str.endswith(unit):
            return int(size_str.replace(unit, "")) * units[unit]
    return int(size_str)

@click.command()
@click.option('--path', required=True, type=click.Path(exists=True), help='目标文件夹路径')
@click.option('--empty', is_flag=True, help='删除空文件夹')
@click.option('--pattern', default=None, help='删除匹配模式的文件，如 *.tmp')
@click.option('--min-size', default=None, help='删除小于指定大小的文件，如 100KB')
@click.option('--max-size', default=None, help='删除大于指定大小的文件，如 10MB')
@click.option('--dry-run', is_flag=True, help='预览模式，不执行删除')
def clean(path, empty, pattern, min_size, max_size, dry_run):
    """文件清理功能"""
    min_bytes = parse_size(min_size) if min_size else None
    max_bytes = parse_size(max_size) if max_size else None

    for root, dirs, files in os.walk(path, topdown=False):
        # 删除空文件夹
        if empty:
            for d in dirs:
                dir_path = os.path.join(root, d)
                if not os.listdir(dir_path):
                    if dry_run:
                        click.echo(f"将删除空文件夹: {dir_path}")
                    else:
                        os.rmdir(dir_path)
                        click.echo(f"已删除空文件夹: {dir_path}")

        # 删除文件
        for f in files:
            file_path = os.path.join(root, f)
            size = os.path.getsize(file_path)

            # 模式匹配
            if pattern and fnmatch.fnmatch(f, pattern):
                if dry_run:
                    click.echo(f"将删除文件: {file_path}")
                else:
                    os.remove(file_path)
                    click.echo(f"已删除文件: {file_path}")
                continue

            # 按大小清理
            if min_bytes and size < min_bytes:
                if dry_run:
                    click.echo(f"将删除小文件: {file_path} ({size} bytes)")
                else:
                    os.remove(file_path)
                    click.echo(f"已删除小文件: {file_path}")
                continue

            if max_bytes and size > max_bytes:
                if dry_run:
                    click.echo(f"将删除大文件: {file_path} ({size} bytes)")
                else:
                    os.remove(file_path)
                    click.echo(f"已删除大文件: {file_path}")
                continue
