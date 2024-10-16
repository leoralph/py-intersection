import click
import pandas as pd

@click.command()

@click.argument('left', type=click.File('r'))
@click.argument('right', type=click.File('r'))

@click.option('--left-column', '-lc', default='ID', help='First column to compare')
@click.option('--right-column', '-rc', default='ID', help='Second column to compare')

@click.option('--output', '-o', default='output.csv', help='Output file')


def intersection(left_column, right_column, left, right, output):
    df1 = pd.read_csv(left)
    df2 = pd.read_csv(right)

    intersection = pd.merge(
        df1,
        df2, 
        how='inner',
        left_on=left_column,
        right_on=right_column
    )

    intersection.to_csv(output, index=False)

if __name__ == '__main__':
    intersection()