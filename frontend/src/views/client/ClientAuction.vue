<template>
  <div>
    <TopNavi />
    <v-divider></v-divider>

    <v-row justify="center" class="ma-3">
      <h2 class="title font-weight-bold">査定一覧</h2>
    </v-row>
    <v-divider></v-divider>

    <v-container 
        v-for="(offer_Item,i) in offer_Items.results" :key="i"
        class="py-0 px-6 layer-top"
      >
      <v-carousel :show-arrows="false" height="240" :class="`rounded-lg mt-8`">
        <a :href="`/client/shop/${offer_Item.id}/`">
          <v-carousel-item
            :src="offer_Item.image"
            v-ripple
          ></v-carousel-item>
        </a>
      </v-carousel>
      <v-card-title class="px-0 pb-0">{{offer_Item.item_name}}</v-card-title>
      <v-card-text class="px-0">
        <div>グレード: {{offer_Item.grade}}</div>
        <div>走行距離: {{offer_Item.mileage}} km</div>
      </v-card-text>
    <v-divider></v-divider>

    </v-container>

    <div class="push"></div>
    <ClientBottomNavi />
  </div>
</template>

<script>
  import TopNavi from '@/components/TopNavi.vue'
  import ClientBottomNavi from '@/components/client/ClientBottomNavi.vue'
  import api from '@/services/api'
  export default {
    name: 'CliantAuction',
    data(){
      return {
        offers: '',
        headers: [
            { text: '依頼ID', value: 'offer_id', align: 'center' },
            {
              text: '商品写真',
              align: 'start',
              sortable: false,
              value: 'name',
            },
            { text: '商品名', value: 'calories', align: 'center' },
            { text: '住所', value: 'address', align: 'center' },
            { text: '査定依頼日', value: 'carbs', align: 'center' },
            { text: 'カテゴリ', value: 'category', align: 'center' },
            { text: '依頼者', value: 'offer', align: 'center' },
            { text: '査定金額', value: 'money', align: 'center' },
          ],
        offer_Items: [],
        assesmentprice: [],
      }
    },
    components: {
      TopNavi,
      ClientBottomNavi
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

      api({
        method: 'get',
        url: '/api/v1/api/assesment_price/'
      })
      .then(response => this.assesment_price = response.data.results)
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
