<template v-else>
  <v-item-group class="d-flex overflow-x-auto">
    <v-container v-for="shop in shop_Info" :key="shop">
      <v-scroll-y-transition>
        <v-card
          class="mx-auto"
          max-width="260"
          v-ripple
        >
          <a :href="`/client/shop/${shop.id}/`">
          <v-img
            :src="shop.img"
            height="200px"
            :class="`rounded-lg`"
          ></v-img>
          </a>
        </v-card>
      </v-scroll-y-transition>
      <v-card-subtitle class="pb-0">
        {{shop.place}} {{ shop.grade }}
      </v-card-subtitle>

      <v-card-text class="text--primary">
        <div>{{shop.tel}}</div>
        <div>{{shop.email}}</div>
      </v-card-text>
    </v-container>
  </v-item-group>
</template>

<script>
  import api from '../services/api'

  export default {
    name: 'ShopSlider',
    data(){
      return {
        shop_Info: [],
      }
    },
    components: {
    },
    filters: {
      priceLocaleString: function (value) {
          return value.toLocaleString()
      }
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/api/client',
      })
      .then(response => this.shop_Info = response.data.results)
      .catch(error => console.log(error))
    },
  }
</script>

