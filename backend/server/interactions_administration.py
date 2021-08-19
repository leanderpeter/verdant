from .db.interactions_mapper import InteractionMapper
from .db.stock_metadata_mapper import StockMetadataMapper

from .bo.interaction import Interaction
from .bo.stock_metadata import StockMetadata

from .recommender.lightfm_recommender import Recommender

import pandas as pd
from tqdm import tqdm


class InteractionAdministration():
    def __init__(self):
        pass

    # function to import interactions from .csv format into MySQL Database
    # call this function on deployment or on import
    def import_interaction_data(self, *args):
        interactions = pd.read_csv(
            '/home/l/verdant/backend/server/lightfm-datasets-soon-deprecated/lightfm-interactions-sn1-0.csv', sep=',')
        # mySQL cant work with numpy nan so we fill in Strings 'NaN'
        interactions = interactions.fillna('NaN')
        interactions = self.pandas_to_interaction_bo(interactions)

        with InteractionMapper() as mapper:
            return mapper.insert_list(interactions)

    # function to import metadata from .csv format into MySQL Database
    # call this function on deployment or on import
    def import_metadata(self, *args):
        metadata = pd.read_csv(
            '/home/l/verdant/backend/server/lightfm-datasets-soon-deprecated/lightfm-metadata-sn1-0.csv', sep=',')
        # mySQL cant work with numpy nan so we fill in Strings 'NaN'
        metadata = metadata.fillna('NaN')
        metadata = self.pandas_to_metadata_bo(metadata)

        with StockMetadataMapper() as mapper:
            return mapper.insert_list(metadata)

    # inline function of import_interaction_data() converts pandas rows to
    # interaction business object

    def pandas_to_interaction_bo(self, dataframe):
        interactions = []
        for index, row in tqdm(dataframe.iterrows()):
            interaction = Interaction()
            interaction.set_id(index)
            interaction.set_interaction_name(f'Placeholder_{index}')
            interaction.set_ticker(row['stock_symbol'])
            interaction.set_uuid(row['uuid'])
            interactions.append(interaction)
        return interactions

    # inline function of import_metadata_data() converts pandas rows to
    # metadata business object
    def pandas_to_metadata_bo(self, dataframe):
        metadata_list = []
        for index, row in tqdm(dataframe.iterrows()):
            stock = StockMetadata()
            stock.set_id(index)
            stock.set_ticker(row['stock_symbol'])
            stock.set_average_rating(row['average_rating'])
            stock.set_marcet_cap(row['marcet_cap'])
            stock.set_average_volume(row['averageVolume'])
            stock.set_country_code(row['country_code'])
            stock.set_industry(row['industry'])
            stock.set_sector(row['sector'])
            stock.set_employees(row['employees'])
            stock.set_overall_risk(row['overall_risk'])
            metadata_list.append(stock)
        return metadata_list

    # returns a list of all interactions in the mysql database
    def get_all_interactions(self):
        with InteractionMapper() as mapper:
            return mapper.find_all()

    # returns a list of all metadata bos in the mysql database
    def get_all_metadata(self):
        with StockMetadataMapper() as mapper:
            return mapper.find_all()

    # transforms a list of interaction_bos into a pandas dataframe
    def interaction_bo_to_pandas(self, interactions_list):

        data = []
        for interaction in interactions_list:
            data_tmp = {'uuid': interaction.get_uuid(),
                        'holding_name': interaction.get_interaction_name(),
                        'stock_symbol': interaction.get_ticker()}
            data.append(data_tmp)
        df = pd.DataFrame(data=data)
        return df

    # transforms a list of metadata_bos into a pandas dataframe
    def metadata_bo_to_pandas(self, metadata_list):
        data = []
        for stock in metadata_list:
            data_tmp = {'stock_symbol': stock.get_ticker(),
                        'average_rating': stock.get_average_rating(),
                        'marcet_cap': stock.get_marcet_cap(),
                        'average_volume': stock.get_average_volume(),
                        'country_code': stock.get_country_code(),
                        'industry': stock.get_industry(),
                        'sector': stock.get_sector(),
                        'employees': stock.get_employees(),
                        'overall_risk': stock.get_overall_risk()}
            data.append(data_tmp)
        df = pd.DataFrame(data=data)
        return df

    # add interaction entry/object into mysql database
    def insert_interaction(self, interaction):
        with InteractionMapper() as mapper:
            return mapper.insert(interaction)

    # get all metadata stocks that are available
    def get_all_metadata(self):
        with StockMetadataMapper() as mapper:
            return mapper.find_all()

    def predict(self, query_stock_list):

        uuid = query_stock_list[0]['uuid']

        # add query_stock_list to database
        for interaction in query_stock_list:
            tmp = Interaction.from_dict(interaction)
            self.insert_interaction(tmp)

        # get all metadata from mysql Database and convert to pandas df
        metadata_df = self.metadata_bo_to_pandas(self.get_all_metadata())

        # get all interactions from mysql Database and convert to pandas df
        interactions_df = self.interaction_bo_to_pandas(
            self.get_all_interactions())

        # init recommender
        recom = Recommender()

        # preprocessing
        user_stock_interaction_csr, user_stock_interaction, user_dict, item_dict, metadata_csr = recom.preprocess(
            interactions_df, metadata_df)

        # model
        model = recom.fit(user_stock_interaction_csr)

        # scores of predictions
        scores = recom.predict(model, user_stock_interaction,
                               uuid, user_dict, item_dict, metadata_csr)
        print(scores)
        response = []
        for i in scores:
            tmp = Interaction()
            tmp.set_id(0)
            tmp.set_interaction_name('placeholder')
            tmp.set_ticker(i)
            tmp.set_uuid(uuid)
            response.append(tmp)
        return response
