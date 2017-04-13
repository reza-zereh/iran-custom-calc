'use strict';

class declarationCalc {

    constructor(itemsCount = 0) {
        this.declaration = {
            items: {
                price: [],
                rate: [],
                exchangeRate: 0
            },
            freight: {
                price: 0,
                exchangeRate: 0
            },
            insurance: 0
        };
        this.itemsCount = itemsCount;
    }

    /**
     * Set basic values to declaration object
     * 
     * @param {Array.number} price 
     * @param {Array.number} rate
     * @param {number} priceExchangeRate
     * @param {number} freight
     * @param {number} freightExchangeRate 
     * @param {number} insurance 
     * 
     */
    setBaseValues(price, rate, priceExchangeRate, freight, freightExchangeRate, insurance) {
        if (this.itemsCount != price.length || this.itemsCount != rate.length) {
            throw new Error(`Error: Items count is not equal to ${this.itemsCount}`);
        }

        this.declaration.items.price = price.map(item => Number(item));
        this.declaration.items.rate = rate.map(item => Number(item));
        this.declaration.items.exchangeRate = Number(priceExchangeRate);
        this.declaration.freight.price = Number(freight);
        this.declaration.freight.exchangeRate = Number(freightExchangeRate);
        this.declaration.insurance = Number(insurance);
    }

    print() {
        console.log(JSON.stringify(this.declaration, null, 2));
    }
}


// manual tests
let declaration = new declarationCalc(2);
declaration.setBaseValues([1200, 2313], [5, 10], 3200, 1200, 3200, 17);
declaration.print();