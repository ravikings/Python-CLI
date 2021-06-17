""" Author: Abdulrafiu rabiu Date: 06-16-2021 """

import pandas as pd
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import click


class ReadCsvFiles:

    """
    A class used to represent an csv file manipulation operatons

    ...

    Attributes
    ----------
    csvGlob : str
        Task to retrun the list of files in the folder
    csvColumn : str
        Task to retrun the colomn of a file
    avgColumn : int
        Task to retrun the average of a column
    threadingFunc : int
        Task to retrun the average of a column for files in the folder, using threading

    Inputs
    ----------
    file: str
        use to indicate file working directory
    column: str
        use to indicate columns needed 
    fileformat: str
        use to indidate file format 
    worker: int
        a flag to indicate maximum number of workers

    Methods
    -------
    csvGlob(file)
        retruns lists of files in the folder

    csvColumn(quantity)
        Prints the colomn values for quantity

    avgColumn(quantity)
        Prints the average values for quantity column

    """

    def __init__(self, file: str, column: str, fileformat: str, concurrency=1):

        self.file = file
        self.column = column
        self.fileformat = fileformat
        self.worker = concurrency

    # get files from directory

    def csvGlob(self):

        source_to_read = Path(self.file).rglob("*." + self.fileformat)
        return list(source_to_read)

    # Get speficied column from files

    def csvColumn(self):

        folder = list(self.csvGlob())
        for csv_file in folder:
            #df = pd.read_csv(csv_file,  header=None)
            df = pd.read_csv(csv_file)
            headerList = ['color', 'name', 'quantity', 'city']
            df.to_csv(csv_file, header=headerList, index=False)
            df = pd.read_csv(csv_file)
            column_output = df[self.column]
            # print(df[self.column])
            print(column_output)

    # carrying out calculation for columns
    def avgColumn(self) -> int:

        folder = self.csvGlob()
        res = []
        for cfile in folder:
            df = pd.read_csv(cfile)
            mean = df[self.column].mean()
            add = str(cfile) + " " + str(round(mean, 2))
            res.append(add)
        return res

    # using threading to get calaculations for multiple files
    def threadingFunc(self):
        file_folder = self.csvGlob()
        with ThreadPoolExecutor(max_workers=self.worker) as executor:
            executor.map(self.avgColumn(), file_folder)


@click.command()
@click.option('--file', help='specific file location.',  type=str)
@click.option('--column',  help='column location to perform calaculation.',  type=str)
@click.option('--fileformat', help='file format you want to work with',  type=str)
@click.option('--concurrency', help='please specific number of worker to get the job done',  type=int)
def cli(file, column, fileformat, concurrency):
    output = ReadCsvFiles(file, column, fileformat, concurrency)
    val = output.avgColumn()
    for i in val:
        click.echo(i)


if __name__ == '__main__':
    cli()

# python classRead.py --file intelepeer --column quantity --fileformat csv --concurrency 2

# p = ReadCsvFiles("intelepeer", "quantity", "csv", 2)
# x = p.csvColumn()

# for i in x:
#     print(i)
