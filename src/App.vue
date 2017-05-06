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

        declarationItems: []
      }
    },

    mounted() {
      Event.$on('backToDcnBasics', () => {
        this.isDcnBasicsActive = true;
      }),
      Event.$on('basicInfoCollected', () => {
        this.isDcnBasicsActive = false;
      });
    }
    
  }
</script>