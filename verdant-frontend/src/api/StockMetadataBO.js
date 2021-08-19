import BusinessObject from "./BusinessObject";

export default class StockMetadataBO extends BusinessObject {
  constructor(
    aTickerSymbol,
    aAverageRating,
    aMarcetCap,
    aAverageVolume,
    aCountryCode,
    aIndustry,
    aSector,
    aEmployees,
    aOverallRisk
  ) {
    super();
    this.TickerSymbol = aTickerSymbol;
    this.AverageRating = aAverageRating;
    this.MarcetCap = aMarcetCap;
    this.AverageVolume = aAverageVolume;
    this.CountryCode = aCountryCode;
    this.Industry = aIndustry;
    this.Sector = aSector;
    this.Employees = aEmployees;
    this.OverallRisk = aOverallRisk;
  }

  getTickerSymbol() {
    return this.TickerSymbol;
  }

  setTickerSymbol(aTickerSymbol) {
    this.TickerSymbol = aTickerSymbol;
  }

  getAverageRating() {
    return this.AverageRating;
  }

  setAverageRating(aAverageRating) {
    this.AverageRating = aAverageRating;
  }

  getMarcetCap() {
    return this.MarcetCap;
  }

  setMarcetCap(aMarcetCap) {
    this.MarcetCap = aMarcetCap;
  }

  getAverageVolume() {
    return this.AverageVolume;
  }

  setAverageVolume(aAverageVolume) {
    this.AverageVolume = aAverageVolume;
  }

  getCountryCode() {
    return this.CountryCode;
  }

  setCountryCode(aCountryCode) {
    this.CountryCode = aCountryCode;
  }

  getIndustry() {
    return this.Industry;
  }

  setIndustry(aIndustry) {
    this.Industry = aIndustry;
  }

  getSector() {
    return this.Sector;
  }

  setSector(aSector) {
    this.Sector = aSector;
  }

  getEmployees() {
    return this.Employees;
  }

  setEmployees(aEmployees) {
    this.Employees = aEmployees;
  }

  getOverallRisk() {
    return this.OverallRisk;
  }

  setOverallRisk(aOverallRisk) {
    this.OverallRisk = aOverallRisk;
  }

  /**
   * Returns an Array of PlayerBOs from a given JSON structure
   */
  static fromJSON(metadata) {
    let results = null;
    if (Array.isArray(metadata)) {
      results = [];
      metadata.forEach((c) => {
        Object.setPrototypeOf(c, StockMetadataBO.prototype);
        results.push(c);
      });
    } else {
      // Es gibt wohl nur ein Objekt
      let c = metadata;
      Object.setPrototypeOf(c, StockMetadataBO.prototype);
      results = c;
    }
    return results;
  }
}
