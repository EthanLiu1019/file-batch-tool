import click
from filebatch.rename import batch_rename
from filebatch.archive import zip_folder

@click.group()
def cli():
    """FileBatchTool: 极简文件批处理工具"""
    pass

@cli.command()
@click.option('--path', required=True, type=click.Path(exists=True), help='目标文件夹路径')
@click.option('--prefix', default='', help='文件名前缀')
@click.option('--suffix', default='', help='文件名后缀')
@click.option('--start', default=1, type=int, help='起始编号')
@click.option('--ext', default=None, help='修改扩展名')
@click.option('--preview', is_flag=True, help='仅预览，不执行重命名')
def rename(path, prefix, suffix, start, ext, preview):
    """批量重命名文件"""
    batch_rename(path, prefix, suffix, start, ext, preview)

@cli.command()
@click.option('--path', required=True, type=click.Path(exists=True), help='要打包的文件夹路径')
@click.option('--output', default='archive.zip', help='输出 zip 文件路径')
@click.option('--dry-run', is_flag=True, help='预览将打包的内容')
def zip(path, output, dry_run):
    """打包文件夹为 ZIP"""
    zip_folder(path, output, dry_run)

if __name__ == '__main__':
    cli()
