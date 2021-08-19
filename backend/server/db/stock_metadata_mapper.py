#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.db.mapper import Mapper
from server.bo.stock_metadata import StockMetadata
import mysql.connector as connector
import pandas as pd


class StockMetadataMapper(Mapper):
    """Mapper-Klasse, die Bewertung Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_by_id(self, id):
        """Suchen eines Noduls mit vorgegebener ID

        :param id Primärschlüsselattribut aus der DB
        :return Modul-Objekt, das der übergebener id entspricht, 
                None wenn DB-Tupel nicht vorhanden ist
        """
        result = None

        cursor = self._connection.cursor()
        command = "SELECT id, ticker_symbol, average_rating, marcet_cap, average_volume, country_code, industry, sector, employees, overall_risk FROM metadata WHERE id = {}".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, ticker_symbol, average_rating, marcet_cap, average_volume,
             country_code, industry, sector, employees, overall_risk) = tuples[0]
            stock = StockMetadata()
            stock.set_id(id)
            stock.set_ticker(ticker_symbol)
            stock.set_average_rating(average_rating)
            stock.set_marcet_cap(marcet_cap)
            stock.set_average_volume(average_volume)
            stock.set_country_code(country_code)
            stock.set_industry(industry)
            stock.set_sector(sector)
            stock.set_employees(employees)
            stock.set_overall_risk(overall_risk)

            result = stock

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                        keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_all(self):
        """Auslesen aller metadata aus der Datenbank

        :return Eine Sammlung aller Modul-Objekten
        """
        result = []

        cursor = self._connection.cursor()

        command = "SELECT id, ticker_symbol, average_rating, marcet_cap, average_volume, country_code, industry, sector, employees, overall_risk FROM metadata"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, ticker_symbol, average_rating, marcet_cap, average_volume,
             country_code, industry, sector, employees, overall_risk) in tuples:
            stock = StockMetadata()
            stock.set_id(id)
            stock.set_ticker(ticker_symbol)
            stock.set_average_rating(average_rating)
            stock.set_marcet_cap(marcet_cap)
            stock.set_average_volume(average_volume)
            stock.set_country_code(country_code)
            stock.set_industry(industry)
            stock.set_sector(sector)
            stock.set_employees(employees)
            stock.set_overall_risk(overall_risk)
            result.append(stock)

        self._connection.commit()
        cursor.close()

        return result

    def insert(self, stock):
        """Einfügen eines metadata-Objekts

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param modul 
        :return das bereits übergebene Modul Objekt mit aktualisierten Daten (id)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM metadatas")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                stock.set_id(1)
            else:
                stock.set_id(maxid[0]+1)

        command = "INSERT INTO metadata (id, ticker_symbol, average_rating, marcet_cap, average_volume, country_code, industry, sector, employees, overall_risk) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (
            stock.get_id(),
            stock.get_ticker(),
            stock.get_average_rating(),
            stock.get_marcet_cap(),
            stock.get_average_volume(),
            stock.get_country_code(),
            stock.get_industry(),
            stock.get_sector(),
            stock.get_employees(),
            stock.get_overall_risk(),
        )
        cursor.execute(command, data)
        self._connection.commit()
        cursor.close()

        return stock

    def update(self, modul):
        """Überschreiben / Aktualisieren eines Modul Objekts in der DB

        :param modul
        :return aktualisiertes Modul-Objekt
        """
        pass

    def delete(self, id):
        """Löschen der Daten eines Modul-Objekts aus der Datenbank 
        Zuerst aus teilnahmen, dann projekte_hat_metadata und anschließend metadata Tabelle 
        dies geschiet anhand der id
        Das Löschen mehrerer Tabellen findet statt, da Fremdschlüßelbeziehungen bestehen

        :param id
        """
        pass

    def delete_by_id(self, projekt_id):
        """Löschen von Einträgen in projekte_hat_metadata nach projekt_id
        Hierdurch werden Modulwahloptionen für ein Projekt durch Fremdschlüsselbeziehungen entfernt

        :param projekt_id
        """
        pass

    def insert_list(self, metadata):
        """Einfügen eines metadata-Objekts

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param modul 
        :return das bereits übergebene Modul Objekt mit aktualisierten Daten (id)
        """

        for stock in metadata:
            cursor = self._connection.cursor()
            cursor.execute("SELECT MAX(id) AS maxid FROM metadata")
            tuples = cursor.fetchall()

            for (maxid) in tuples:
                if maxid[0] is None:
                    stock.set_id(1)
                else:
                    stock.set_id(maxid[0]+1)

            command = "INSERT INTO metadata (id, ticker_symbol, average_rating, marcet_cap, average_volume, country_code, industry, sector, employees, overall_risk) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data = (
                stock.get_id(),
                stock.get_ticker(),
                stock.get_average_rating(),
                stock.get_marcet_cap(),
                stock.get_average_volume(),
                stock.get_country_code(),
                stock.get_industry(),
                stock.get_sector(),
                stock.get_employees(),
                stock.get_overall_risk(),
            )
            cursor.execute(command, data)
            self._connection.commit()
            cursor.close()

        return metadata
