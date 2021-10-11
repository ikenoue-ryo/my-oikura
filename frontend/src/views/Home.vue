<template>
  <div>
    <Header />
    <GlobalMenu />

    <v-container>
      <v-row>
        <v-col>
        <v-container>
          <v-btn
            depressed
            color="primary"
            x-large
            href="offer-form"
          >
            査定を依頼する
          </v-btn>
        </v-container>
        </v-col>
      </v-row>

      <v-row class="ma-1">
        <h2>査定結果</h2>
        <p class="ma-2">ただいまの査定件数：{{cars.length}}件</p>
      </v-row>
      <template>
        <v-card>
          <v-card-title>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="cars"
            :search="search"
          >
            <template v-slot:item.item_image="{ item }">
              <v-img :src="item.item_image" width="100" max-height="100" class="mx-auto ma-5"></v-img>
            </template>
            <template v-slot:[`item.item_name`]="{ item }">
              <a :href="`/offer-form/${item.offer.offer.id}/`"> {{ item.item_name }}</a>
            </template>
            <template v-slot:[`item.assessed_store`]="{ item }">
              <a :href="`/client/shop/${item.offer.client_shop.id}/`"> {{ item.assessed_store }}</a>
            </template>
          </v-data-table>
        </v-card>
      </template>

    </v-container>

  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import api from '../services/api'

  export default {
    name: 'Home',
    data(){
      return {
        offers: '',
        headers: [
          {
            text: 'item_image',
            align: 'center',
            sortable: false,
            value: 'item_image',
          },
          { text: 'item_name', value: 'item_name', align: 'center' },
          { text: 'grade', value: 'grade', align: 'center' },
          { text: 'model_year', value: 'model_year', align: 'center' },
          { text: 'mileage', value: 'mileage', align: 'center' },
          { text: 'assessed_store', value: 'assessed_store', align: 'center' },
          { text: 'assessed_amount', value: 'assessed_amount', align: 'center', filter: this.filters },
        ],
        search: '',
        cars: [],
        offer_Items: [],
        assesment_price: [],
      }
    },
    components: {
      Header,
      GlobalMenu,
    },
    filters: {
      priceLocaleString: function (value) {
          return value.toLocaleString()
      }
    },
    methods: {
      // chipColor(category) {
      //   if(category == '家電') {
      //     return 'yellow'
      //   }
      //   if(category == '家具') {
      //     return 'primary'
      //   }
      //   if(category == 'PC') {
      //     return 'black'
      //   }
      //   if(category == 'ファッション') {
      //     return 'orange'
      //   }
      //   if(category == '') {
      //     return 'black'
      //   }
      // },
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/api/offers/'
      })
      .then(response => this.offer_Items = response.data)
      .catch(error => console.log(error))

      api({
        method: 'get',
        url: '/api/v1/api/assesment_price/'
      })
      .then(response => this.cars = response.data.results.map((item)=>({
        offer:item,
        item_image:item.offer.image,
        item_name:item.offer.item_name,
        grade:item.offer.grade,
        model_year:item.offer.model_year + ' 年',
        mileage:item.offer.mileage.toLocaleString() + ' km',
        assessed_store:item.client_shop.name,
        assessed_amount:item.value.toLocaleString() + ' 円',
      })))
      .catch(error => console.log(error))
    },
  }
</script>

<style>
  ul li {
    display: inline-block;
    margin: 10px
  }
</style>