import StockMetadataBO from "./StockMetadataBO";
import InteractionsBO from "./InteractionsBO";
/*
Singleton Abstarktion des backend REST interfaces. Es handelt sich um eine access methode
*/
export default class VerdantAPI {
  //singletone instance
  static #api = null;

  // Lokales Python backend
  #VerdantServerBaseURL = "/verdantApp";

  // ------------------------ GET ------------------------------
  //getStockMetadata: all
  #StockMetadataURL = () => `${this.#VerdantServerBaseURL}/stocks/metadata`;
  #StockPredictionURL = () => `${this.#VerdantServerBaseURL}/recommender`;

  /*
	Singleton/Einzelstuck instanz erhalten
	*/
  static getAPI() {
    if (this.#api == null) {
      this.#api = new VerdantAPI();
    }
    return this.#api;
  }
  /*
	Gibt einen Error zuruck auf JSON Basis. fetch() gibt keine Errors wie 404 oder 500 zuruck. Deshaltb die func fetchAdvanced 
	*/
  #fetchAdvanced = (url, init) =>
    fetch(url, init, { credentials: "include" }).then((res) => {
      //fetch() gibt keine Errors wie 404 oder 500 zuruck
      if (!res.ok) {
        throw Error(`${res.status} ${res.statusText}`);
      }
      return res.json();
    });

  //StocksMetadata
  getAllStockMetadata() {
    return this.#fetchAdvanced("/verdantApp/stocks/metadata").then(
      (responseJSON) => {
        console.log(responseJSON);
        let stockBO = StockMetadataBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(stockBO);
        });
      }
    );
  }

  getStockPrediction(stockArray) {
    return this.#fetchAdvanced(this.#StockPredictionURL(), {
      method: "GET",
      headers: {
        Accept: "application/json, text/plain",
        "Content-type": "application/json",
      },
      body: JSON.stringify(stockArray),
    }).then((responseJSON) => {
      // zuruck kommt ein array, wir benoetigen aber nur ein Objekt aus dem array
      let responseStockArray = InteractionsBO.fromJSON(responseJSON);
      return new Promise(function (resolve) {
        resolve(responseStockArray);
      });
    });
  }
}
