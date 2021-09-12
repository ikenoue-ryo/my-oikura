<template>
  <div>
    <Header />
    <GlobalMenu />
    <!-- <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
      </v-row>
    </v-container> -->

  <v-container>
    <validation-observer
      ref="observer"
    >
      <form @submit.prevent="submit">
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="商品名"
            rules="required|max:10"
          >
            <v-text-field
              v-model="item_name"
              :counter="10"
              :error-messages="errors"
              label="商品名"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="製造年"
            rules="required|max:4"
          >
            <v-text-field
              v-model="item_date"
              :counter="4"
              :error-messages="errors"
              label="製造年"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
          <!-- <validation-provider
            v-slot="{ errors }"
            name="select"
            rules="required"
          >
            <v-select
              v-model="select"
              :items="items"
              :error-messages="errors"
              label="Select"
              data-vv-name="select"
              required
            ></v-select>
          </validation-provider>
        </v-col> -->
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            rules="required"
            name="checkbox"
          >
            <v-checkbox
              v-model="checkbox"
              :error-messages="errors"
              value="1"
              label="利用規約に同意"
              type="checkbox"
              required
            ></v-checkbox>
          </validation-provider>
        </v-col>

        <v-btn
          class="mr-4"
          type="submit"
          @click="submit"
        >
          送信
        </v-btn>
        <v-btn @click="clear">
          クリア
        </v-btn>
      </form>
    </validation-observer>
  </v-container>

  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import axios from 'axios'
  import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

  setInteractionMode('eager')

  extend('digits', {
    ...digits,
    message: '{_field_} needs to be {length} digits. ({_value_})',
  })

  extend('required', {
    ...required,
    message: '{_field_} can not be empty',
  })

  extend('max', {
    ...max,
    message: '{_field_} may not be greater than {length} characters',
  })

  extend('regex', {
    ...regex,
    message: '{_field_} {_value_} does not match {regex}',
  })

  extend('email', {
    ...email,
    message: 'Email must be valid',
  })

  export default Vue.extend({
    name: 'Home',
    data: () => ({
        item_name: '',
        item_date: '',
        select: null,
        // items: [
        //   'Item 1',
        //   'Item 2',
        //   'Item 3',
        //   'Item 4',
        // ],
        checkbox: null,
        offers: '',
    }),
    components: {
      Header,
      GlobalMenu,
      ValidationProvider,
      ValidationObserver,
    },
    methods: {
      submit() {
        this.$refs.observer.validate()
        axios.post('http://127.0.0.1:8000/api/offers/', {
          item_name: this.item_name,
          item_date: this.item_date,
        }).then(response => {
          console.log(response);
          const next = '/'
          this.$router.replace(next)
        }).catch(error => {
          console.log(error);
        })
      },
      clear() {
        this.item_name = ''
        this.item_date = ''
        // this.select = null
        this.checkbox = null
        this.$refs.observer.reset()
      }
    },
    // mounted(){
    //   axios.post('offers/')
    //   .then(response => this.offers = response.data)
    //   .catch(error => console.log(error))
    // }
  })
</script>

<style>
  ul li {
    display: inline-block;
    margin: 10px
  }
</style>