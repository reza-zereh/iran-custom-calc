'use strict';

class DeclarationCalc {

    constructor(itemsCount, invoiceTotal) {
        this.itemsCount = itemsCount;
        this.invoiceTotal = invoiceTotal;
        this.declaration = {
            items: [],
            invoiceExchangeRate: 0,
            freight: {
                price: 0,
                exchangeRate: 1,
                priceInRial: 0
            },
            insurance: 0
        };
        this.hasFreight = false;
        this.hasInsurance = false;
    }

    /**
     * Set basic values to declaration object
     * 
     * @param {Array.number} prices 
     * @param {Array.number} rates
     * @param {number} priceExchangeRate
     * @param {number} freight
     * @param {number} freightExchangeRate 
     * @param {number} insurance 
     * 
     */
    setBaseValues(prices, rates, priceExchangeRate, freight = 1, freightExchangeRate = 1, insurance = 1) {
        // TODO: check prices and rates to be array

        if (this.itemsCount != prices.length || this.itemsCount != rates.length) {
            throw new Error(`Error: Items count is not equal to ${this.itemsCount}`);
        }

        this.declaration.invoiceExchangeRate  = Number(priceExchangeRate);
        this.declaration.freight.price        = Number(freight);
        this.declaration.freight.exchangeRate = Number(freightExchangeRate);
        this.declaration.freight.priceInRial  = this.declaration.freight.price * this.declaration.freight.exchangeRate;
        this.declaration.insurance            = Number(insurance);

        this.haveFreightAndInsurance(freight, insurance);
        this.buildItems(prices, rates);

        if (!this.checkItemsTotal()) {
            throw new Error(`Error: Items total price is not equal to ${this.invoiceTotal}`);
        }
    }

    /**
     * set 'hasFreight' and 'hasInsurance' and calculate insurance price if does not have any insurance
     * 
     * @param {Number} freight 
     * @param {Number} insurance 
     */
    haveFreightAndInsurance(freight, insurance) {
        this.hasFreight = freight > 1 ? true : false;
        this.hasInsurance = insurance > 1 ? true : false;

        // In case there is no insurance letter
        if (!this.hasInsurance) {
            this.declaration.insurance = Math.round(
                ((this.invoiceTotal * this.declaration.invoiceExchangeRate) + this.declaration.freight.priceInRial) * 0.5 / 100
            );
        }
    }

    /**
     * Build diffrent parts of value table for each item
     * 
     * @param {Array.Number} prices 
     * @param {Array.Number} rates 
     */
    buildItems(prices, rates) {
        // Convert 'prices' and 'rates' array items to number
        prices = prices.map(item => Number(item));
        rates = rates.map(item => Number(item));

        // Build diffrent parts of value table for each item
        for(var i=0; i < this.itemsCount; i++) {
            this.declaration.items.push({
                price      : prices[i],
                priceInRial: Math.round(prices[i] * this.declaration.invoiceExchangeRate),
                rate       : rates[i],
                freight    : this.hasFreight ? Math.round(prices[i] * this.declaration.freight.priceInRial / this.invoiceTotal) : 1,
                insurance  : Math.round(prices[i] *  this.declaration.insurance / this.invoiceTotal)
            });
        }
    }

    /**
     * Check equality of sum of items price and invoiceTotal
     * 
     * @returns {boolean}
     */
    checkItemsTotal() {
        let itemsTotal = 0;
        this.declaration.items
            .forEach(item => {
                return itemsTotal += item.price;
            });
        return itemsTotal == this.invoiceTotal;
    }

    /**
     * Do customs calculations for each item
     */
    doCalculations() {
        this.declaration.items
            .forEach(item => {
                item.totalCIF = item.priceInRial + item.freight + item.insurance;
                item.value_041 = Math.round(item.totalCIF * item.rate / 100);
                // TODO: should read these values from another file
                item.redCross_042 = Math.ceil(item.value_041 * 1 / 100);
                item.environment_042 = Math.ceil(item.totalCIF * 0.5 / 1000);
                item.tax_047 = Math.round((item.value_041 + item.totalCIF) * 6 / 100);
                item.tax_048 = Math.round((item.value_041 + item.totalCIF) * 3 / 100);
                item.itemTotal = item.value_041 + item.redCross_042 + item.environment_042 + item.tax_047 + item.tax_048;
            });
    }

    /**
     * Returns an array containing all of the items
     * 
     * @returns {Array.Object}
     */
    getItems() {
        return this.declaration.items;
    }

    print() {
        console.log(JSON.stringify(this.declaration, null, 2));
    }
}

module.exports = DeclarationCalc;
