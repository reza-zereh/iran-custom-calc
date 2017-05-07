<template>
  <div id="app">

    <dcn-basics :basic-info="declarationBasics" v-if="isDcnBasicsActive"></dcn-basics>
    <div v-if="!isDcnBasicsActive">
      <dcn-items-form 
        :items-count="declarationBasics.itemsCount"
        :declaration-items="declarationItems">
      </dcn-items-form>
    </div>
  </div>
</template>

<script>
  import DcnBasics from './components/DcnBasics.vue';
  import DcnItem from './components/DcnItem.vue';
  import DcnItemsForm from './components/DcnItemsForm.vue';
  import DeclarationCalc from './lib/DeclarationCalc.js';

  export default {
    components: {
      'dcn-basics': DcnBasics,
      'dcn-item': DcnItem,
      'dcn-items-form': DcnItemsForm
    },

    data() {
      return {
        isDcnBasicsActive: true,

        declarationBasics: {
          invoiceTotal: 0,
          invoiceExchangeRate: 1,
          itemsCount: 1,
          hasFreightCharge: false,
          freightCharge: 1,
          freightExchangeRate: 1,
          hasInsurance: false,
          insuranceCost: 0
        },

        declarationItems: [],
        prices: [],
        rates: []
      }
    },

    mounted() {
      // TODO: Use vue-router instead of v-if and these booleans
      Event.$on('backToDcnBasics', () => {
        this.isDcnBasicsActive = true;
      }),
      Event.$on('basicInfoCollected', () => {
        this.isDcnBasicsActive = false;
      }),

      // Fires when declaration items are collected
      // Read price & rate from `declarationItems` and push them into `prices` and `rates` array
      // Then calls `executeDeclarationCalcs()` to do calculation stuffs
      Event.$on('itemsCostCollected', () => {
        this.declarationItems.forEach((item) => {
          this.prices[item.itemNumber - 1] = Number(item.price);
          this.rates[item.itemNumber - 1] = Number(item.rate);
        });
        this.executeDeclarationCalcs();
      })
    },

    methods: {
      executeDeclarationCalcs() {
        // Create a new instance of DeclarationCalc class
        // and pass itemsCount and invoiceTotal as arguments
        let declaration = new DeclarationCalc(
          this.declarationBasics.itemsCount, 
          this.declarationBasics.invoiceTotal
        );

        // Call `setBaseValues()` to setting required info for declaration 
        declaration.setBaseValues(
          this.prices,
          this.rates,
          this.declarationBasics.invoiceExchangeRate,
          this.declarationBasics.freightCharge,
          this.declarationBasics.freightExchangeRate,
          this.declarationBasics.insuranceCost,
        );

        // Call `doCalculations()` to calculate declaration costs
        declaration.doCalculations();

        // TODO: Show result in a new component instead of console
        // Print result to the console
        declaration.print();
        alert('Check the console for result!');
      }

    }
    
  }
</script>