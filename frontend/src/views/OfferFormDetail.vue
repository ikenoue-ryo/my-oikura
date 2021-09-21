<template>
  <div>
    <Header />
    <GlobalMenu />

      <p>ID: {{offer_Items.id}}</p>
      <p>製造日: {{offer_Items.item_date}}</p>
      <p>カテゴリ: {{offer_Items.category.name}}</p>
      <v-img :src="offer_Items.image" width="100" max-height="100"></v-img>
      <p>作成日: {{offer_Items.created_at}}</p>
      <p>更新日: {{offer_Items.updated_at}}</p>

  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import axios from 'axios'
  import api from '../services/api'

  export default Vue.extend({
    name: 'Home',
    data: () => ({
      offer_Items: []
    }),
    components: {
      Header,
      GlobalMenu,
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/offers/' + this.$route.params['id']
      })
      .then(response => this.offer_Items = response.data)
      .catch(error => console.log(error))
    }
  })
</script>

<style>

</style>