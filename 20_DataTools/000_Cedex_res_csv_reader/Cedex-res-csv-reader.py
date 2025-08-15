import os
import re
import time
import numpy as np
import pandas as pd

# record setting
rec = "Start recording:"

# seeking path of csv files
path = ""
dic = os.listdir(
    os.path.abspath(
        "."
    )
)

# file sequence initialize
fseq = 1

# dataframe construction
for f in dic:
    if "res" in f and f.endswith(".csv"):
        fpath = f

        # setting effective columns
        col = ["Test","Date","Order-Time","Time","Result","Unit","Sample","Flags"]

        # deploy pandas csv reading & output as excel
        if fpath == "":
            rec = str(rec) + "\nNot match, Skipped......"
        else:
            data=pd.read_csv(
                fpath,
                encoding = "utf8",
                sep = ";",
                dtype = {"Test":str,"Date":str,"Time":str,"Order-Time":str,"Result":float,"Unit":str,"Sample":str,"Flags":str},
                na_values = "NaN",
                thousands = ",",
                decimal = ".",
            )[col]
        
        # insert new columns, delete olds
        data.insert(
            0,
            "ProjectName",
            pd.Series()
        )
        data.insert(
            1,
            "LotNum",
            pd.Series()
        )
        data.insert(
            2,
            "RawDate",
            pd.Series()
        )
        data["RawDate"].astype(str)
        data.insert(
            3,
            "TestDate",
            pd.to_datetime(
                data["Date"]
            )
        )
        data.drop(
            "Date",
            axis = 1,
            inplace = True
        )

        # slicing sample index, filling Projectnames/Lots/RawDate.
        i = 0
        item = str(
            data.loc[i,"Sample"]
        )
        while i < len(data):
            item = str(
                data.loc[i,"Sample"]
            )
            slicetarget = item
            
            searchres1 = re.search(
                " ",
                slicetarget
            )
            if searchres1:
                searchres1arr = np.array(searchres1.span())
                sliceposition1 = slicepo1 = int(searchres1arr[0])
                sliceres1 = slicetarget[:slicepo1]
                data.loc[i,"ProjectName"] = sliceres1
            else:
                searchres1 = re.search(
                    "-",
                    slicetarget
                )
                if searchres1:
                    searchres1arr = np.array(searchres1.span())
                    sliceposition1 = slicepo1 = int(searchres1arr[0])
                    sliceres1 = slicetarget[:slicepo1]
                    data.loc[i,"ProjectName"] = sliceres1
                else:
                    sliceres1 = "NaN"
                    data.loc[i,"ProjectName"] = sliceres1

            searchres2 = re.search(
                " D",
                slicetarget
            )
            if searchres2:
                searchres2arr = np.array(searchres2.span())
                sliceposition2 = slicepo2 = int(searchres2arr[0])+2
                sliceres3 = slicetarget[slicepo2:]
                check3 = re.search(
                    " ",
                    sliceres3
                )
                if check3:
                    check3arr =  np.array(check3.span())
                    sliceposition = slicepo = int(check3arr[0])
                    sliceres3 = sliceres3[:slicepo]
                else:
                    check3 = re.search(
                        "-",
                        sliceres3
                    )
                    if check3:
                        check3arr =  np.array(check3.span())
                        sliceposition = slicepo = int(check3arr[0])
                        sliceres3 = sliceres3[:slicepo]
                    else:
                        sliceres3 = sliceres3
                data.loc[i,"RawDate"] = str(sliceres3)
            else:
                searchres2 = re.search(
                    " d",
                    slicetarget
                    )
                if searchres2:
                    searchres2arr = np.array(searchres2.span())
                    sliceposition2 = slicepo2 = int(searchres2arr[0])+2
                    sliceres3 = slicetarget[slicepo2:]
                    check3 = re.search(
                        " ",
                        sliceres3
                    )
                    if check3:
                        check3arr =  np.array(check3.span())
                        sliceposition = slicepo = int(check3arr[0])
                        sliceres3 = sliceres3[:slicepo]
                    else:
                        check3 = re.search(
                            "-",
                            sliceres3
                            )
                        if check3:
                            check3arr =  np.array(check3.span())
                            sliceposition = slicepo = int(check3arr[0])
                            sliceres3 = sliceres3[:slicepo]
                        else:
                            sliceres3 = sliceres3
                    data.loc[i,"RawDate"] = str(sliceres3)
                else:
                    searchres2 = re.search(
                        "-D",
                        slicetarget
                    )
                    if searchres2:
                        searchres2arr = np.array(searchres2.span())
                        sliceposition2 = slicepo2 = int(searchres2arr[0])+2
                        sliceres3 = slicetarget[slicepo2:]
                        check3 = re.search(
                            " ",
                            sliceres3
                        )
                        if check3:
                            check3arr =  np.array(check3.span())
                            sliceposition = slicepo = int(check3arr[0])
                            sliceres3 = sliceres3[:slicepo]
                        else:
                            check3 = re.search(
                                "-",
                                sliceres3
                            )
                            if check3:
                                check3arr =  np.array(check3.span())
                                sliceposition = slicepo = int(check3arr[0])
                                sliceres3 = sliceres3[:slicepo]
                            else:
                                sliceres3 = sliceres3
                        data.loc[i,"RawDate"] = str(sliceres3)
                    else:
                        searchres2 = re.search(
                            "-d",
                            slicetarget
                        )
                        if searchres2:
                            searchres2arr = np.array(searchres2.span())
                            sliceposition2 = slicepo2 = int(searchres2arr[0])+2
                            sliceres3 = slicetarget[slicepo2:]
                            check3 = re.search(
                                " ",
                                sliceres3
                            )
                            if check3:
                                check3arr =  np.array(check3.span())
                                sliceposition = slicepo = int(check3arr[0])
                                sliceres3 = sliceres3[:slicepo]
                            else:
                                check3 = re.search(
                                    "-",
                                    sliceres3
                                )
                                if check3:
                                    check3arr =  np.array(check3.span())
                                    sliceposition = slicepo = int(check3arr[0])
                                    sliceres3 = sliceres3[:slicepo]
                                else:
                                    sliceres3 = sliceres3
                            data.loc[i,"RawDate"] = str(sliceres3)
                        else:
                            sliceres3 = "NaN"
                            data.loc[i,"RawDate"] = str(sliceres3)
            if searchres1 and searchres2:
                slicepo3 = slicepo1 + 1
                slicepo4 = slicepo2 - 2
                sliceres2 = slicetarget[slicepo3:slicepo4]
                sliceres2 = sliceres2.replace(" ","-",1)
                data.loc[i,"LotNum"] = sliceres2
            else:
                sliceres1 = "NaN"
                sliceres2 = "NaN"
                sliceres3 = "NaN"
                data.loc[i,"LotNum"] = sliceres2
            i = i + 1
        
        else:
            rec = str(rec) + "\nMatch, Processed......" + "Total test results: " + str(i)
        
        # output
        
        i = time.strftime(
            "%Y-%m-%d-%H.%M.%S",
            time.localtime()
        )
        outpath = str(
            "output" + str(i) + "-" + str(fseq) + ".csv"
        )
        fseq = fseq + 1

        data.to_csv(
            outpath,
            sep = ","
        )
    else:
        rec = str(rec) + "\nNot match, skipped......"

# finishing
rec = str(rec) + "\nProcess finished."
print(rec)
