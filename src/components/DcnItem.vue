<template>
  <div>
    <div class="field">
      <label class="label">ارزش قلم&nbsp;{{itemNumber}}</label>
      <p class="control">
        <input class="input" type="text" v-model="price" @blur="insertPrice">
      </p>
    </div>
    
    <div class="field">
      <label class="label">ماخذ قلم&nbsp;{{itemNumber}}</label>
      <p class="control">
        <input class="input" type="text" v-model="rate">
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      itemNumber: {
        required: true,
        type: Number
      },
      items: {
        required: true,
        type: Object
      }
    },

    data() {
      return {
        price: '',
        rate: ''
      }
    },

    methods: {
      insertPrice() {
        if (this.price !== "" || !this.price) {
          this.items.prices[this.itemNumber - 1] = this.price;
        }
      }
    }
  }
</script>
