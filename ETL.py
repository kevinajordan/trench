# -*- coding: utf-8 -*-
import os
import csv
from TrafficProcessor import TrafficProcessor as processor

class ETL:
    def __init__(self):
        self.data = []
        self.labels = []
    
    def load_data(self, file_path, label):
        files = os.listdir(file_path)
        n_files = 0
        for file in files:
            try:
                data_processor = processor(file_path + file)
                n_files += 1
            except:
                print(f'Error: Failed to parse {file_path + file}')
                continue

            tmpTLS = data_processor.getTLSInfo()
            tmpBD = data_processor.getByteDistribution()
            tmpIPT = data_processor.getIndividualFlowIPTs()
            tmpPL = data_processor.getIndividualFlowPcktLengths()
            tmpMTD = data_processor.getIndividualFlowMetadata()

            if all([tmpMTD != 0, tmpPL != None, tmpIPT != None]):
                for i in range(len(tmpMTD)):
                    if len(tmpTLS[i]) > 1:
                        tmp_data = []

                        tmp_data.extend(tmpTLS[i])
                        tmp_data.extend(tmpBD[i])
                        tmp_data.extend(tmpIPT[i])
                        tmp_data.extend(tmpPL[i])
                        tmp_data.extend(tmpMTD[i])
                        tmp_data.append(label)
                        
                        with open('traffic_dataset.csv', 'a') as csvfile:
                            writer = csv.writer(csvfile, delimiter=",")
                            writer.writerow(tmp_data)
