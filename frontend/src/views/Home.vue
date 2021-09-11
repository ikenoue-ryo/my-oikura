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

      <h2>査定依頼一覧</h2>

      <v-data-table
        :headers="headers"
        :items="offer_Items"
        :items-per-page="5"
        class="elevation-1"
      >
        <template v-slot:body="{ items: offer_Items }">
          <tbody>
            <tr v-for="offer_Item in offer_Items" :key="offer_Item.item_name" class="custom-tr">
              <td>{{ offer_Item.item_name }}</td>
              <td>{{ offer_Item.item_date }}</td>
              <td>{{ offer_Item.item_name }}</td>
              <td>{{ offer_Item.item_date }}</td>
              <td>{{ offer_Item.item_name }}</td>
              <td>{{ offer_Item.item_name }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>

    </v-container>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import axios from 'axios'

  export default Vue.extend({
    name: 'Home',
    data: () => ({
      offers: '',
      headers: [
          {
            text: '商品名',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: '製造日', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
      offer_Items: []
    }),
    components: {
      Header,
      GlobalMenu,
    },
    mounted(){
      axios.get('http://127.0.0.1:8000/api/offers/')
        .then(response => this.offer_Items = response.data.results)
        .catch(error => console.log(error))
      }
  })
</script>

<style>
  ul li {
    display: inline-block;
    margin: 10px
  }
</style>