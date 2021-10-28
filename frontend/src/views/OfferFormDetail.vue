<template>
  <div>
    <v-img 
      :src="offer_Items.image" 
      width="100%" 
      class="mx-auto ma-0"
    >
      <v-icon @click="$router.back()" class="ma-4">mdi-arrow-left</v-icon>
    </v-img>

    <v-container class="pa-8">
      <v-row>
        <v-col>
          <h2>{{ offer_Items.item_name }}</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col>{{ offer_Items.item_date }}年</v-col>
      </v-row>
    </v-container>

    <div class="push"></div>
    <BottomNavi />
  </div>
</template>

<script>
  import BottomNavi from '@/components/BottomNavi.vue'
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        offer_Items: []
      }
    },
    components: {
      BottomNavi,
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/api/offers/' + this.$route.params['id']
      })
      .then(response => this.offer_Items = response.data)
      .catch(error => console.log(error))
    }
  }
</script>

<style>
  .push {
    height: 55px;/*フッターと同じ高さに指定*/
  }
</style>