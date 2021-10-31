<template>
  <div>
    <TopNavi />
    <v-divider></v-divider>

    <v-img
      class="white--text align-end google-map"
      height="300px"
      src="@/assets/googlemap.jpeg" width="100%"
    ></v-img>

    <v-card
      :loading="loading"
      class="mx-auto my-12 rounded-t-xl"
    >
      <v-container 
        v-for="(shop,i) in shop_Info" :key="i"
        class="py-10 px-6 pt-3 layer-top"
      >
        <v-row justify="center" class="ma-3">
          <h2 class="title font-weight-bold">店舗一覧</h2>
        </v-row>
        <v-divider></v-divider>
        <v-carousel :show-arrows="false" height="240" :class="`rounded-lg mt-8`">
          <a :href="`/client/shop/${shop.id}/`">
            <v-carousel-item
              :src="shop.img"
              v-ripple
            ></v-carousel-item>
          </a>
        </v-carousel>
        <v-row
          align="center"
          class="mt-3 ml-0"
        >
          <v-rating
            :value="4.5"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
          ></v-rating>

          <div class="grey--text ms-4">
            4.5 (413)
          </div>
          <!-- <v-row>
            <v-col>
          <vue-star animate="animated rubberBand" color="#F05654!important">
              <span slot="icon" class="fa fa-heart" @click="handleClick"></span>
            </vue-star></v-col>
            </v-row> -->
            
        </v-row>
        <v-card-title class="px-0 pb-0">{{shop.name}}</v-card-title>

        <v-card-text class="px-0">
          <div>{{shop.place}}</div>
          <div>{{shop.tel}}</div>
        </v-card-text>
      </v-container>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
    </v-card>

    <BottomNavi />
  </div>
</template>

<script>
  import TopNavi from '@/components/TopNavi.vue'
  import BottomNavi from '@/components/BottomNavi.vue'
  import api from '@/services/api'
  // import Vue from 'vue'
  // import VueStar from 'vue-star'
  // Vue.component('VueStar', VueStar)

  export default {
    name: 'Mypage',
    data() {
      return {
        shop_Info: [],
        items: [
          {
            src: 'https://pbs.twimg.com/media/FB47c-UXoAMPF7G.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
          },
        ],
      }
    },
    components: {
      TopNavi,
      BottomNavi,
      // VueStar
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/api/client',
      })
      .then(response => this.shop_Info = response.data.results.filter(prefecture => prefecture.assesment_price.client_shop.prefectures === this.$route.params['prefecture']))
      .catch(error => console.log(error))
    },
    computed: {

    }
  }
</script>

<style scoped>
  .google-map{
    position: fixed;
    /* z-index: -1; */
  }

  #app .VueStar {
    /* position: relative;
    width: 50px;
    height: 50px; */
  }
  .VueStar__icon .fa {
    font-size: 2em;
    cursor: pointer;
  }

  .v-carousel__controls {
    /* height: 40px; */
  }

  .layer-top {
    z-index: 1;
    margin-top: 240px;
  }
</style>