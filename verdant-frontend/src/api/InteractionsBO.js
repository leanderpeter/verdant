import BusinessObject from "./BusinessObject";

export default class InteractionBO extends BusinessObject {
  constructor(auuid, aholdingName, atickerSymbol) {
    super();
    this.uuid = auuid;
    this.holdingName = aholdingName;
    this.tickerSymbol = atickerSymbol;
  }

  getUuid() {
    return this.uuid;
  }

  setUuid(auuid) {
    this.uuid = auuid;
  }

  getHoldingName() {
    return this.holdingName;
  }

  setHoldingName(aholdingName) {
    this.holdingName = aholdingName;
  }
  getTickerSymbol() {
    return this.tickerSymbol;
  }

  setTickerSymbol(atickerSymbol) {
    this.tickerSymbol = atickerSymbol;
  }

  /**
   * Returns an Array of PlayerBOs from a given JSON structure
   */
  static fromJSON(Interaction) {
    let results = null;
    if (Array.isArray(Interaction)) {
      results = [];
      Interaction.forEach((c) => {
        Object.setPrototypeOf(c, InteractionBO.prototype);
        results.push(c);
      });
    } else {
      // Es gibt wohl nur ein Objekt
      let c = Interaction;
      Object.setPrototypeOf(c, InteractionBO.prototype);
      results = c;
    }
    return results;
  }
}
