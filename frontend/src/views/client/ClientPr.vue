<template>
  <div>
    <ClientHeader />

    <v-container>
      <v-row class="ma-1">
        <h2>店舗紹介ブログ</h2>
      </v-row>
      <div v-for="client_info in client_pr" :key="client_info.id">
        <p><v-img :src="client_info.img" width="100%" class="mx-auto ma-5"></v-img></p>
        <p>{{client_info.text}}</p>
        <v-col class="d-flex justify-end"> 
          <p>{{client_info.created_at}}</p>
        </v-col>
        <v-divider></v-divider>
      </div>
    </v-container>

    <div class="push"></div>
    <ClientBottomNavi />
  </div>
</template>

<script>
  import ClientHeader from '@/components/client/ClientHeader.vue'
  import ClientBottomNavi from '@/components/client/ClientBottomNavi.vue'
  import api from '@/services/api'

  export default {
    name: 'CliantPr',
    data(){
      return {
        client_pr: []
      }
    },
    components: {
      ClientHeader,
      ClientBottomNavi
    },
    mounted() {
      api({
        method: 'get',
        url: '/api/v1/api/client_pr/'
      })
      .then(response => this.client_pr = response.data.results.filter(shop => shop.author == this.id))
      .catch(error => console.log(error))
    },
    computed: {
      id() {
        return this.$store.getters['auth/id']
      },
    }
  }
</script>

<style>

</style>
