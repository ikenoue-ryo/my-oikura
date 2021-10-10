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
        <p class="ma-2">ただいまの査定総数：{{assesment_price.count}}件</p>
      </v-row>
      <div>
      <v-data-table
        :headers="headers"
        :items="assesment_price.results"
        :items-per-page="5"
        class="elevation-1"
      >
        <template v-slot:body="{ items: assesment_price }">
          <tbody>
            <tr v-for="assesment in assesment_price" :key="assesment.item_name">
              <td class="pa-3 text-center"><v-img :src="assesment.offer.image" width="100" max-height="100"></v-img></td>
              <td class="text-center"><a :href="`/offer-form/${assesment.offer.id}/`">{{ assesment.offer.item_name }}</a></td>
              <td class="text-center">{{ assesment.offer.grade }}</td>
              <td class="text-center">{{ assesment.offer.model_year }}年</td>
              <td class="text-center">{{ assesment.offer.mileage|priceLocaleString }} km</td>
              <td class="text-center"><router-link :to="`/client/shop/${assesment.client_shop.id}`">{{ assesment.client_shop.name}}</router-link></td>
              <td v-if="assesment" class="font-weight-bold text-center">{{assesment.value|priceLocaleString}}円</td>
              <td v-else class="text-center">-</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      </div>
    </v-container>

    <!-- {{assesment_price}} -->
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
              text: '商品写真',
              align: 'start',
              sortable: false,
              value: 'name',
            },
            { text: '商品名', value: 'calories', align: 'center' },
            { text: 'グレード', value: 'grade', align: 'center' },
            { text: '年式', value: 'year', align: 'center' },
            { text: '走行距離', value: 'carbs', align: 'center' },
            { text: '査定店舗', value: 'offer', align: 'center' },
            { text: '査定額', value: 'money', align: 'center' },
          ],
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
      chipColor(category) {
        if(category == '家電') {
          return 'yellow'
        }
        if(category == '家具') {
          return 'primary'
        }
        if(category == 'PC') {
          return 'black'
        }
        if(category == 'ファッション') {
          return 'orange'
        }
        if(category == '') {
          return 'black'
        }
      },
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/api/offers/'
      })
      .then(response => this.offer_Items = response.data)
      .catch(error => console.log(error))
      // this.category_name = this.$route.query.name
      // console.log(this.$route.query.category)

      api({
        method: 'get',
        url: '/api/v1/api/assesment_price/'
      })
      .then(response => this.assesment_price = response.data)
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