<template>
  <div id="app">

    <dcn-basics :basic-info="declarationBasics" v-if="isDcnBasicsActive"></dcn-basics>

    <div v-if="isDcnItemsFormActive">
      <dcn-items-form 
        :items-count="declarationBasics.itemsCount"
        :declaration-items="declarationItems"
      >
      </dcn-items-form>
    </div>

    <div v-if="isDcnResultActive" style="direction: ltr;">
      <pre>
        {{calculatedDeclaration}}
      </pre>
    </div>

    <!--<router-view></router-view>-->
  </div>
</template>

<script>
  import DeclarationCalc from './lib/DeclarationCalc.js';

  import DcnBasics from './components/DcnBasics.vue';
  import DcnItemsForm from './components/DcnItemsForm.vue';

  export default {
    components: {
      'dcn-basics'    : DcnBasics,
      'dcn-items-form': DcnItemsForm
    },

    data() {
      return {
        isDcnBasicsActive   : true,
        isDcnItemsFormActive: false,
        isDcnResultActive   : false,

        declarationBasics: {
          invoiceTotal       : 0,
          invoiceExchangeRate: 1,
          itemsCount         : 1,
          hasFreightCharge   : false,
          freightCharge      : 1,
          freightExchangeRate: 1,
          hasInsurance       : false,
          insuranceCost      : 0
        },

        declarationItems     : [],
        prices               : [],
        rates                : [],
        calculatedDeclaration: {} 
      }
    },

    mounted() {
      // TODO: Use vue-router instead of v-if and these booleans
      Event.$on('backToDcnBasics', () => {
        this.isDcnBasicsActive = true;
        this.isDcnItemsFormActive = false;
        this.isDcnResultActive = false;
      }),
      Event.$on('basicInfoCollected', () => {
        this.isDcnItemsFormActive = true;
        this.isDcnBasicsActive = false;
        this.isDcnResultActive = false;
      }),

      // Fires when declaration items are collected
      // Read price & rate from `declarationItems` and push them into `prices` and `rates` array
      // Then calls `executeDeclarationCalcs()` to do calculation stuffs
      Event.$on('itemsCostCollected', () => {
        this.declarationItems.forEach((item) => {
          this.prices[item.itemNumber - 1] = Number(item.price);
          this.rates[item.itemNumber - 1]  = Number(item.rate);
        });
        this.executeDeclarationCalcs();
        
        this.isDcnResultActive    = true;
        this.isDcnItemsFormActive = false;
        this.isDcnBasicsActive    = false;
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

        this.calculatedDeclaration = declaration.getItems();
      }

    }
    
  }
</script>