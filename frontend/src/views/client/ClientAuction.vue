<template>
  <div>
    <ClientHeader />
    <ClientGlobalMenu />

    <v-container>
      <v-row class="ma-1">
        <h2>依頼一覧</h2>
        <p class="ma-2">依頼件数：{{offer_Items.count}}件</p>
        <!-- {{offer_Items}}<br><br><br> -->

        <!-- {{assesmentprice}} -->
      </v-row>
      <div>
      <v-data-table
        :headers="headers"
        :items="offer_Items.results"
        :items-per-page="5"
        class="elevation-1"
      >
        <template v-slot:body="{ items: offer_Items }">
          <tbody>
            <tr v-for="offer_Item in offer_Items" :key="offer_Item.item_name">
              <td class="text-center"><a :href="`/offer-form/${offer_Item.id}/`">{{ offer_Item.id }}</a></td>
              <td class="pa-3 text-center"><v-img :src="offer_Item.image" width="100" max-height="100"></v-img></td>
              <td class="text-center"><a :href="`/offer-form/${offer_Item.id}/`">{{ offer_Item.item_name }}</a></td>
              <td class="text-center"><a href="https://www.google.com/maps/search/?api=1&query=福岡県福岡市博多区" target="_blank">福岡県福岡市博多区</a></td>
              <td class="text-center">{{ offer_Item.created_at }}</td>
              <td class="text-center">
                <v-chip
                  class="ma-2"
                  :color="chipColor(offer_Item.category.name)"
                  text-color="black"
                >
                  {{ offer_Item.category.name }}
                </v-chip>
              </td>
              <td class="text-center"><router-link :to="`/offer-user/${offer_Item.profile.user.name}`">{{ offer_Item.profile.nickname }}</router-link></td>
              <td class="text-center">5,000円</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      </div>
    </v-container>

    {{offer_Items.results[0].profile.postal_code}}
  </div>
</template>

<script>
  import ClientHeader from '@/components/client/ClientHeader.vue'
  import ClientGlobalMenu from '@/components/client/ClientGlobalMenu.vue'
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
      ClientHeader,
      ClientGlobalMenu,
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
