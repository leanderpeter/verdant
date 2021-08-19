#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.db.mapper import Mapper
from server.bo.interaction import Interaction
import mysql.connector as connector
import pandas as pd


class InteractionMapper(Mapper):
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
        command = "SELECT id, uuid, ticker_symbol FROM ineractions WHERE id={}".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, uuid, ticker_symbol) = tuples[0]
            interaction = Interaction()
            interaction.set_id(id)
            interaction.set_uuid(uuid)
            interaction.set_ticker(ticker_symbol)
            result = interaction

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                        keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_all(self):
        """Auslesen aller interactions aus der Datenbank

        :return Eine Sammlung aller Modul-Objekten
        """
        result = []

        cursor = self._connection.cursor()

        command = "SELECT id, uuid, holding_name, ticker_symbol FROM interactions"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, uuid, holding_name, ticker_symbol) in tuples:
            interactions = Interaction()
            interactions.set_id(id)
            interactions.set_uuid(uuid)
            interactions.set_ticker(ticker_symbol)
            interactions.set_interaction_name(holding_name)
            result.append(interactions)

        self._connection.commit()
        cursor.close()

        return result

    def insert(self, interaction):
        """Einfügen eines interactions-Objekts

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param modul 
        :return das bereits übergebene Modul Objekt mit aktualisierten Daten (id)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM interactions")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                interaction.set_id(1)
            else:
                interaction.set_id(maxid[0]+1)

        command = "INSERT INTO interactions (id, uuid, holding_name, ticker_symbol) VALUES (%s,%s,%s,%s)"
        data = (
            interaction.get_id(),
            interaction.get_uuid(),
            interaction.get_interaction_name(),
            interaction.get_ticker(),
        )
        cursor.execute(command, data)
        self._connection.commit()
        cursor.close()

        return interaction

    def update(self, modul):
        """Überschreiben / Aktualisieren eines Modul Objekts in der DB

        :param modul
        :return aktualisiertes Modul-Objekt
        """
        pass

    def delete(self, id):
        """Löschen der Daten eines Modul-Objekts aus der Datenbank 
        Zuerst aus teilnahmen, dann projekte_hat_Interactions und anschließend Interactions Tabelle 
        dies geschiet anhand der id
        Das Löschen mehrerer Tabellen findet statt, da Fremdschlüßelbeziehungen bestehen

        :param id
        """
        pass

    def delete_by_id(self, projekt_id):
        """Löschen von Einträgen in projekte_hat_Interactions nach projekt_id
        Hierdurch werden Modulwahloptionen für ein Projekt durch Fremdschlüsselbeziehungen entfernt

        :param projekt_id
        """
        pass

    def insert_list(self, interactions):
        """Einfügen eines interactions-Objekts

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param modul 
        :return das bereits übergebene Modul Objekt mit aktualisierten Daten (id)
        """

        for interaction in interactions:
            cursor = self._connection.cursor()
            cursor.execute("SELECT MAX(id) AS maxid FROM interactions")
            tuples = cursor.fetchall()

            for (maxid) in tuples:
                if maxid[0] is None:
                    interaction.set_id(1)
                else:
                    interaction.set_id(maxid[0]+1)

            command = "INSERT INTO interactions (id, uuid, holding_name, ticker_symbol) VALUES (%s,%s,%s,%s)"
            data = (
                interaction.get_id(),
                interaction.get_uuid(),
                interaction.get_interaction_name(),
                interaction.get_ticker(),
            )
            cursor.execute(command, data)
            self._connection.commit()
            cursor.close()

        return interactions
