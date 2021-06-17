from concurrent import futures
import asyncio
import pandas as pd
from pathlib import Path
from numpy.core.getlimits import iinfo
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from timeit import default_timer as timer
from classRead import *

"""

    showcasing using asyncio to get the job done concurrently

"""

class ReadCsvFiles:

    def __init__(self, file, column, fileformat, worker, *args, **kwargs):

        self.file = str(file)
        self.column = str(column)
        self.fileformat = str(fileformat)
        self.worker = int(worker)
        

    def csvGlob(self):

        source_to_read = Path(self.file).rglob("*." + self.fileformat)
        return list(source_to_read)
      

    def csvColumn(self):
        
        folder = list(self.csvGlob())
        for csv_file in folder:
            df = pd.read_csv(csv_file )
            headerList = ['color', 'name', 'quantity', 'city']
            df.to_csv(csv_file, header=headerList, index=False)
            df = pd.read_csv(csv_file )
            column_output = df[self.column]
            print(column_output)
    

    def avgColumn(self):
        
        folder = self.csvGlob()
        for cfile in folder:
            df = pd.read_csv(cfile)
            mean = df[self.column].mean()
            print(cfile, "{:.2f}".format(mean))


    def threadingFunc(self):
        file_folder = self.csvGlob()
        with ThreadPoolExecutor(max_workers=self.worker) as executor:
            executor.map(self.avgColumn(), file_folder)


   
    async def csvConcurrency(self):
        file_folder = self.csvGlob()
        futures = [loop.run_in_executor(
            executor,
            self.avgColumn(),
            file
        ) for file in file_folder]
        await asyncio.gather(*futures)




if __name__ == '__main__':


    try:
        p = ReadCsvFiles('intelepeer', 'quantity', 'csv', 3)
        executor = ProcessPoolExecutor()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(p.csvConcurrency())
        # asyncio.ensure_future(csvConcurrency())
        # loop.run_forever()

    except Exception as e:
        print('There was a problem:')
        print(str(e))
    # except KeyboardInterrupt:
    #     pass

    finally:
        print("closing loops")
        loop.close()

