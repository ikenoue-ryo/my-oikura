<template>
  <v-item-group class="d-flex overflow-x-auto">
    <div v-for="item in cars" :key="item" class="mr-4">
      <v-scroll-y-transition>
        <v-card
          class="mx-auto"
          max-width="260"
          v-ripple
        >
          <a :href="`/offer-form/${item.offer.offer.id}/`">
          <v-img
            :src="item.item_image"
            height="200px"
          ></v-img>
          </a>
        </v-card>
      </v-scroll-y-transition>
      <v-card-subtitle class="pb-0">
        {{item.item_name}} {{ item.grade }}
      </v-card-subtitle>

      <v-card-text class="text--primary">
        <div>走行距離： {{item.mileage}}</div>
        <div>査定金額： {{item.assessed_amount}}</div>
      </v-card-text>
    </div>
  </v-item-group>
</template>

<script>
  import api from '../services/api'

  export default {
    name: 'Home',
    data(){
      return {
        cars: [],
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
        url: '/api/v1/api/assesment_price/'
      })
      .then(response => this.cars = response.data.results.map((item)=>({
        offer:item,
        item_image:item.offer.image,
        item_name:item.offer.item_name,
        grade:item.offer.grade,
        model_year:item.offer.model_year + ' 年',
        mileage:item.offer.mileage.toLocaleString() + ' km',
        assessed_store:item.client_shop.name,
        assessed_amount:item.value.toLocaleString() + ' 円',
        img:item.client_shop.img,
      })))
      .catch(error => console.log(error))
    },
  }
</script>

