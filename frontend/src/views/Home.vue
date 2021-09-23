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
            一括査定スタート
          </v-btn>
        </v-container>
        </v-col>
      </v-row>

      <v-row class="ma-1">
        <h2>査定依頼一覧</h2>
        <p class="ma-2">依頼件数：{{offer_Items.count}}件</p>
      </v-row>
      <div>
      <!-- <a href="/offer-form/1"> -->
      <v-data-table
        :headers="headers"
        :items="offer_Items.results"
        :items-per-page="5"
        class="elevation-1"
      >
        <template v-slot:body="{ items: offer_Items }">
          <tbody>
            <tr v-for="offer_Item in offer_Items" :key="offer_Item.item_name">
              <td class="pa-3"><v-img :src="offer_Item.image" width="100" max-height="100"></v-img></td>
              <td><a :href="`/offer-form/${offer_Item.id}/`">{{ offer_Item.item_name }}</a></td>
              <td>{{ offer_Item.item_date }}年</td>
              <td>{{ offer_Item.created_at }}</td>
              <td>
                <v-chip
                  class="ma-2"
                  :color="chipColor(offer_Item.category.name)"
                  text-color="black"
                >
                  {{ offer_Item.category.name }}
                </v-chip>
              </td>
              <td>{{ offer_Item.item_name }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <!-- </a> -->
      </div>
    </v-container>
  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import axios from 'axios'
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
            { text: '商品名', value: 'calories' },
            { text: '製造日', value: 'fat' },
            { text: '査定依頼日', value: 'carbs' },
            { text: 'カテゴリ', value: 'category' },
            { text: 'Iron (%)', value: 'iron' },
          ],
        offer_Items: []
      }
    },
    components: {
      Header,
      GlobalMenu,
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
      }
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/offers/'
      })
      .then(response => this.offer_Items = response.data)
      .catch(error => console.log(error))
    }
  }
</script>

<style>
  ul li {
    display: inline-block;
    margin: 10px
  }
</style>