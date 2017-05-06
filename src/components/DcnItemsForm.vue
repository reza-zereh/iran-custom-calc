<template>
    <div>
        <dcn-item v-for="n in itemsCount" 
            :item-number="n"
            :items="declarationItems" 
            :key="n.id">
        </dcn-item>

        <button type="button" class="button is-primary" @click="backToDcnBasics">Back</button>
        <button type="button" class="button is-primary" @click="collectItemsCost">Next</button>
    </div>
</template>

<script>
    import DcnItem from './DcnItem.vue';

    export default {
        components: {
            'dcn-item': DcnItem
        },

        props: {
            itemsCount: {
                type: Number,
                required: true
            },
            declarationItems: {
                type: Array,
                required: true
            }
        },

        methods: {
            backToDcnBasics() {
                Event.$emit('backToDcnBasics');
            },
            collectItemsCost() {
                Event.$emit('collectItemsCost');
            }
        }
    }
</script>