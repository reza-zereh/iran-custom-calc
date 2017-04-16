<template>
    <div>
        <form method="post" @submit.prevent="">
            <legend class="title is-2">اطلاعات پایه اظهارنامه</legend>
            <div class="columns">
                <div class="column">
                    <div class="field">
                        <label class="label">ارزش کل فاکتور</label>
                        <p class="control">
                            <input class="input" type="number" required v-model="invoiceTotal">
                        </p>
                    </div>
                </div>
                <div class="column">
                    <div class="field">
                        <label class="label">نرخ ارز فاکتور</label>
                        <p class="control">
                            <input class="input" type="number" required v-model="invoiceExchangeRate">
                        </p>
                    </div>
                </div>
            </div>
            
            <div class="field">
                <label class="label">تعداد اقلام اظهارنامه</label>
                <p class="control">
                    <input class="input" type="number" required v-model="itemsCount">
                </p>
            </div>

            <div class="field is-clearfix">
                <label class="label">آیا کالا کرایه حمل دارد؟</label>
                <p class="control is-pulled-right">
                    <label class="radio">
                        <input type="radio" name="has_freight" required 
                            :checked="hasFreightCharge"
                            @click="hasFreightToggle"
                        >
                        بلی
                    </label>
                    <label class="radio">
                        <input type="radio" name="has_freight" required 
                            :checked="hasFreightCharge == false"
                            @click="hasFreightToggle"
                        >
                        خیر
                    </label>
                </p>
            </div>

            <div class="columns">
                <div class="column">
                    <div class="field">
                        <label class="label">مبلغ کرایه حمل</label>
                        <p class="control">
                            <input class="input" type="number" 
                                v-model="freightCharge"
                                :disabled="hasFreightCharge == false"
                            >
                        </p>
                    </div>
                </div>
                <div class="column">
                    <div class="field">
                        <label class="label">نرخ ارز کرایه حمل</label>
                        <p class="control">
                            <input class="input" type="number" 
                                v-model="freightExchangeRate"
                                :disabled="hasFreightCharge == false"
                            >
                        </p>
                    </div>
                </div>
            </div>

            <div class="field is-clearfix">
                <label class="label">آیا کالا بیمه نامه دارد؟</label>
                <p class="control is-pulled-right">
                    <label class="radio">
                        <input type="radio" name="has_insurance" required 
                            :checked="hasInsurance"
                            @click="hasInsuranceToggle"
                        >
                        بلی
                    </label>
                    <label class="radio">
                        <input type="radio" name="has_insurance" required 
                            :checked="hasInsurance == false"
                            @click="hasInsuranceToggle"
                        >
                        خیر
                    </label>
                </p>
                
            </div>

            <div class="field">
                <label class="label">مبلغ بیمه نامه</label>
                <p class="control">
                    <input class="input" type="number" 
                        v-model="insuranceCost"
                        :disabled="hasInsurance == false"
                    >
                </p>
            </div>

            <div class="field is-grouped">
                <p class="control">
                    <button type="submit" class="button is-primary is-medium">تایید</button>
                </p>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                invoiceTotal: 0,
                invoiceExchangeRate: 1,
                itemsCount: 1,
                hasFreightCharge: false,
                freightCharge: 1,
                freightExchangeRate: 1,
                hasInsurance: false,
                insuranceCost: 0
            }
        },

        methods: {
            hasFreightToggle() {
                this.hasFreightCharge = !this.hasFreightCharge;
            },

            hasInsuranceToggle() {
                this.hasInsurance = !this.hasInsurance;
            }
        }
    }
</script>