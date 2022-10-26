import os

import click
from nbconvert import SlidesExporter


@click.command(name='slideshow')
@click.argument('notebook')
def make_slideshow(notebook):
    if os.path.exists(notebook):
        os.system(
            f'jupyter nbconvert {notebook} --to slides --post serve  --SlidesExporter.reveal_scroll=true --SlidesExporter.reveal_theme=simple')
    else:
        raise ValueError(f'File {notebook} not found.')

if __name__ == '__main__':
    make_slideshow()
