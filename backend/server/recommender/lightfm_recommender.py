
from ..db.interactions_mapper import InteractionMapper
from ..db.stock_metadata_mapper import StockMetadataMapper

from scipy.sparse import csr_matrix
import numpy as np

import pandas as pd

from lightfm.cross_validation import random_train_test_split
from lightfm.evaluation import auc_score, precision_at_k, recall_at_k
from lightfm import LightFM
from skopt import forest_minimize


class Recommender():
    def __init__(self):
        self.__user_stock_interaction = None
        self.__user_dict = None
        self.__item_dict = None
        self.__user_stock_interaction_csr = None
        self.__metadata_csr = None
        self.__interactions = None

        self.__model = None

    def preprocess(self, interactions, metadata, additional_data=None):

        if additional_data != None:
            # here we add the incoming data from a user to the
            # mysql database
            pass

        # testing, pls delete after
        interactions['rating'] = 1
        metadata_selected = metadata[['stock_symbol', 'industry']]
        interactions_selected = interactions[[
            'uuid', 'rating', 'stock_symbol']]

        metadata['show_symbol'] = metadata['stock_symbol']

        item_dict = {}
        df = metadata[['stock_symbol', 'show_symbol']
                      ].sort_values('stock_symbol').reset_index()

        for i in range(df.shape[0]):
            item_dict[(df.loc[i, 'stock_symbol'])] = df.loc[i, 'show_symbol']
        # dummify/one-hot-encode categorical features
        metadata_selected_transformed = pd.get_dummies(
            metadata_selected, columns=['industry'])
        metadata_selected_transformed = metadata_selected_transformed.sort_values(
            'stock_symbol').reset_index().drop('index', axis=1)

        # convert to csr matrix
        metadata_csr = csr_matrix(
            metadata_selected_transformed.drop('stock_symbol', axis=1).values)

        user_stock_interaction = pd.pivot_table(
            interactions_selected, index='uuid', columns='stock_symbol', values='rating')

        # fill missing values with 0
        user_stock_interaction = user_stock_interaction.fillna(0)

        user_id = list(user_stock_interaction.index)
        user_dict = {}
        counter = 0
        for i in user_id:
            user_dict[i] = counter
            counter += 1

        # convert to csr matrix
        user_stock_interaction_csr = csr_matrix(user_stock_interaction.values)
        # print(user_stock_interaction_csr)

        return user_stock_interaction_csr, user_stock_interaction, user_dict, item_dict, metadata_csr

    def fit(self, user_stock_interaction_csr):
        model = LightFM(loss='warp',
                        random_state=2016,
                        learning_rate=0.001,
                        no_components=150,
                        user_alpha=0.000005)

        model = model.fit(user_stock_interaction_csr,
                          epochs=100,
                          num_threads=16, verbose=False)

        return model

    def predict(self, model, interactions, user_id, user_dict,
                item_dict, metadata_csr, threshold=0, nrec_items=5, show=True):

        n_users, n_items = interactions.shape

        user_x = user_dict[user_id]

        scores = pd.Series(model.predict(
            user_x, np.arange(n_items), item_features=metadata_csr))

        scores.index = interactions.columns

        scores = list(pd.Series(scores.sort_values(ascending=False).index))
        return scores[0:10]

        """
        known_items = list(pd.Series(interactions.loc[user_id, :]
                                     [interactions.loc[user_id, :] > threshold].index).sort_values(ascending=False))

        scores = [x for x in scores if x not in known_items]
        return_score_list = scores[0:nrec_items]
        known_items = list(
            pd.Series(known_items).apply(lambda x: item_dict[x]))
        scores = list(pd.Series(return_score_list).apply(
            lambda x: item_dict[x]))
        if show == True:
            print("User: " + str(user_id))
            print("Known Likes:")
            counter = 1
            for i in known_items:
                print(str(counter) + '- ' + i)
                counter += 1

            print("\n Recommended Items:")
            counter = 1
            for i in scores:
                print(str(counter) + '- ' + i)
                counter += 1"""
