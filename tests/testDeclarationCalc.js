const DeclarationCalc = require('../src/lib/DeclarationCalc');

// manual tests
let declaration = new DeclarationCalc(1, 500);
// declaration.setBaseValues([1200.1, 1100.2], [5, 10], 3200);
declaration.setBaseValues([500], [15], 4702, 860.44, 4702, 318000);
declaration.doCalculations();
// declaration.print();
console.log(declaration.getItems());
console.log(declaration.checkItemsTotal());