const DeclarationCalc = require('./DeclarationCalc');

// manual tests
let declaration = new DeclarationCalc(2, 2300.3);
declaration.setBaseValues([1200.1, 1100.2], [5, 10], 3200);
// declaration.setBaseValues([1200.1, 1100.2], [5, 10], 3200, 1200, 3200, 1700);
declaration.doCalculations();
// declaration.print();
console.log(declaration.getItems());
console.log(declaration.checkItemsTotal());