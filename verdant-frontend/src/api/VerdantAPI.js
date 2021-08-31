import StockMetadataBO from "./StockMetadataBO";
import InteractionsBO from "./InteractionsBO";
/*
Singleton Abstarktion des backend REST interfaces. Es handelt sich um eine access methode
*/
export default class VerdantAPI {
  //singletone instance
  static #api = null;

  // Lokales Python backend
  #VerdantServerBaseURL = "";

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

  /**
   *  Returns a Promise which resolves to a json object.
   *  The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500.
   *  fetchAdvanced throws an Error also an server status errors
   */
  #fetchAdvanced = (url, init) =>
    fetch(url, init).then((res) => {
      // The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500.
      if (!res.ok) {
        throw Error(`${res.status} ${res.statusText}`);
      }
      return res.json();
    });

  //StocksMetadata
  getAllStockMetadata() {
    return this.#fetchAdvanced(this.#StockMetadataURL()).then(
      (responseJSON) => {
        let stockBO = StockMetadataBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(stockBO);
        });
      }
    );
  }

  getStockPrediction(stockArray) {
    return this.#fetchAdvanced(this.#StockPredictionURL(), {
      method: "PUT",
      headers: {
        Accept: "application/json, text/plain",
        "Content-type": "application/json",
      },
      body: JSON.stringify(stockArray),
    }).then((responseJSON) => {
      console.log(responseJSON);
      // zuruck kommt ein array, wir benoetigen aber nur ein Objekt aus dem array
      let responseStockArray = InteractionsBO.fromJSON(responseJSON);
      return new Promise(function (resolve) {
        resolve(responseStockArray);
      });
    });
  }
}
