import sys
import pandas as pd
from time import sleep


def main():
    # Open the given excel file
    df_excel = pd.read_excel(sys.argv[1])
    
    # 1. get the personality id
    # 2. check all of the other rows if they marked as "Y"
    # 3. If true:
    #       Get the Drug_ID for the column
    #       Write to output excel file Personality_ID, Drug_ID

    personalityID_list = df_excel["Personality_ID"].tolist()
    id_list = []
    drug_list = []
    idx = 0
    for id in personalityID_list:
        colList = df_excel[1:]
        colList = colList[1:]
        for col in colList:
            if col != "Personality_ID":
                colValue = df_excel[col][idx]
                if colValue == "Y":
                    id_list.append(id)
                    drug_list.append(col)
        idx += 1
    
    rowList = []
    colList = ["Personality_ID","Drug_Name"]
    for i in range(len(id_list)):
        rowList.append([id_list[i],drug_list[i]])

    df_out = pd.DataFrame(rowList,columns=colList)
    df_out.to_excel("output.xlsx", index=False)


        




main()