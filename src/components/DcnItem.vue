<template>
  <div class="columns">
    <div class="column">
      <div class="field">
        <label class="label">ارزش قلم&nbsp;{{itemNumber}}</label>
        <p class="control">
          <input class="input"
                type="text"
                v-model="price"
          >
        </p>
      </div>
    </div>

    <div class="column">
      <div class="field">
        <label class="label">ماخذ قلم&nbsp;{{itemNumber}}</label>
        <p class="control">
          <input class="input"
                type="text"
                v-model="rate">
        </p>
      </div>
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
      required: false,
      type: Array
    }
  },

  data() {
    return {
      price: '',
      rate: ''
    }
  },

  mounted() {
    Event.$on('collectItemsCost', () => {
      this.items.push({
        itemNumber: Number(this.itemNumber),
        price: Number(this.price),
        rate: Number(this.rate)
      });
    });
  }
}
</script>
