<template>
  <div>
    <v-img
      :src="assesments.offer.image" 
      width="100%" 
      class="mx-auto ma-0"
    >
      <v-icon @click="$router.back()" class="ma-4">mdi-arrow-left</v-icon>
    </v-img>

    <v-container class="pa-8">
      <v-row justify="center">
        <v-col>
          <v-btn
            type="submit"
            color="pink darken-1"
            x-large
            block
            class="white--text font-weight-bold title"
          >
            <span class="body-2 align-end">査定額</span> {{ assesments.value | priceLocaleString }} 円
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <h2>{{ assesments.offer.item_name }}</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col>{{ assesments.offer.item_date }}年</v-col>
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
        assesments: []
      }
    },
    components: {
      BottomNavi,
    },
    filters: {
      priceLocaleString: function (value) {
          return value.toLocaleString()
      }
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/assesment_price'
      })
      .then(response => this.assesments = response.data.results.find(assesments_info => assesments_info.id == this.$route.params['id']))
      .catch(error => console.log(error))
    }
  }
</script>

<style>
  .push {
    height: 55px;/*フッターと同じ高さに指定*/
  }
</style>