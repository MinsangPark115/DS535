import numpy as np
import pandas as pd
import torch
import os
from tqdm import tqdm


def getFileList() :
    return os.listdir(os.getcwd() + "/test")

class Evaluation :
    def __init__(self, file_nm):
        # import
        df_raw = pd.read_csv("raw_data.csv", index_col=0)[:-1]  # last row에 cluster 뺌
        df_raw.index = pd.to_numeric(df_raw.index)
        df_predict = pd.read_csv(os.getcwd() + "/test/"+file_nm, index_col=0)

        self.df_raw = df_raw
        self.df_predict = df_predict

        ## DATASET 값 맞추기
        mov_id = [mov_id for mov_id in self.df_predict.index if mov_id not in self.df_raw.index]
        self.df_raw = self.df_raw.reset_index()

        # nan list 준비
        a = np.empty(len(self.df_raw.columns))
        a[:] = np.nan

        for i in mov_id:
            a[0] = i
            self.df_raw.loc[len(self.df_raw)] = a

        self.df_raw = self.df_raw.set_index('movieId').sort_index()


        self.df_raw.columns = self.df_predict.columns

        # if print 3883 okay.

    def rmse_mape(self):

        df_predict_copy = self.df_predict
        df_raw_copy = self.df_raw

        diff = []
        denom = []
        cnt = 0

        for r in tqdm(df_predict_copy.index):
            preds = df_predict_copy.loc[r]
            targets = df_raw_copy.loc[r]
            for idx in range(len(preds)):
                pred = preds[idx]
                target = targets[idx]
                if np.isnan(target):
                    continue
                else:
                    cnt += 1
                    diff.append(pred - target)
                    denom.append(target)

        # rmse
        tmp = np.array(diff) * np.array(diff)
        print("RMSE : ", np.sqrt((1 / cnt) * np.sum(tmp)))

        # map
        tmp = np.array(diff) / np.array(denom)
        print("MAPE : ", (100 / cnt) * np.sum(np.abs(tmp)))

        self.rmse = np.sqrt((1 / cnt) * np.sum(tmp))
        self.mape = (100 / cnt) * np.sum(np.abs(tmp))

    def precision_recall(self):
        # if rating is over 4, we see this as liked set.
        df_liked = self.df_raw[self.df_raw >= 4]
        df_recommend = self.df_predict[self.df_predict >= 4]

        # If generated matrix show different ratings order, then this metrics would be meaningful.
        # other than that, not really.
        # additional works) number of users for F1-micro, F1-macro

        # here dataframe operation.
        # raw = df_raw.values
        # predict = df_predict.values

        cnt = 0
        precisions = []
        recalls = []

        # for each user : just check 10 user's metrics
        for user in self.df_predict.columns:
            like_item = self.df_raw.index[self.df_raw[user] >= 4]
            recommend_item = self.df_predict.index[self.df_predict[user] >= 4]

            intersec = like_item.intersection(recommend_item)
            precision = 0
            recall = 0
            try:
                precision = len(intersec) / len(recommend_item)
                prec = 1
            except ZeroDivisionError:
                prec = 0
            #         print("no recommend item over 4")
            # recall
            try:
                recall = len(intersec) / len(like_item)
                rec = 1
            except ZeroDivisionError:
                rec = 0
            #         print("no liked item over 4")

            if prec * rec == 1 :  # both are okay
                cnt += 1
                precisions.append(precision)
                recalls.append(recall)

        print("Result for valid {} num. of users : ".format(cnt))
        print("*precision : ", sum(precisions) / cnt, " recall : ", sum(recalls) / cnt)

        self.prec =  sum(precisions) / cnt
        self.reca =  sum(recalls) / cnt


    def do_evaluation(self):

        Evaluation.rmse_mape(self)
        Evaluation.precision_recall(self)
        Evaluation.inter_list_diversity(self)

        print(self.rmse)
        print(self.mape)
        print(self.prec)
        print(self.reca)
        print(self.intra_list_diversity)