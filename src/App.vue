<template>
  <div id="app">

    <dcn-basics :basic-info="declarationBasics"></dcn-basics>
    <dcn-item :item-number="2" :items="declarationItems"></dcn-item>
  </div>
</template>

<script>
  import DcnBasics from './components/DcnBasics.vue';
  import DcnItem from './components/DcnItem.vue';

  export default {
    components: {
      'dcn-basics': DcnBasics,
      'dcn-item': DcnItem
    },

    data() {
      return {
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

        declarationItems: {
          prices: [],
          rates: []
        }
      }
    }
    
  }
</script>