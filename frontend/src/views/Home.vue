<template>
  <div>

    <Header />

    <v-container>
    <GlobalMenu />

      <v-row class="ma-1">
        <h2>査定結果</h2>
        <p class="ma-2">ただいまの査定件数：{{cars.length}}件</p>
      </v-row>
      <template v-if="!$vuetify.breakpoint.xs">
        <v-card>
          <v-card-title>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="cars"
            :search="search"
          >
            <template v-slot:item.item_image="{ item }">
              <v-img :src="item.item_image" width="100" max-height="100" class="mx-auto ma-5"></v-img>
            </template>
            <template v-slot:[`item.item_name`]="{ item }">
              <a :href="`/offer-form/${item.offer.offer.id}/`"> {{ item.item_name }}</a>
            </template>
            <template v-slot:[`item.assessed_store`]="{ item }">
              <a :href="`/client/shop/${item.offer.client_shop.id}/`"> {{ item.assessed_store }}</a>
            </template>
          </v-data-table>
        </v-card>
      </template>
      <!-- sp -->
      <template v-else>
        <v-item-group class="d-flex overflow-x-auto">
          <v-container v-for="item in cars" :key="item">
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
          </v-container>
        </v-item-group>
      </template>
        
      <v-container class="my-10">
        <v-row class="ma-1">
          <h2>周辺エリアを検索</h2>
        </v-row>
        <template v-if="!$vuetify.breakpoint.xs">
          <div>
            PC
          </div>
        </template>
        <template v-else>
          <div class="tableshow_wrap">
            <div class="tableshow">
              <div class="div1 col-3" v-for="prefecture in prefectures" :key="prefecture">
                  <router-link :to="`/client-shop/${prefecture.en}/`">
                    <v-row align="center" v-ripple>
                      <v-col>
                        <v-img :src="prefecture.img" width="70" height="70" :class="`rounded-lg`"></v-img>
                      </v-col>
                      <v-col class="pa-0 font-weight-bold grey--text text--darken-4">
                        {{prefecture.name}}
                      </v-col>
                    </v-row>
                  </router-link>
              </div>
            </div>
          </div>
        </template>
      </v-container>
      
      <template v-if="!$vuetify.breakpoint.xs">
        <div>
          PC
        </div>
      </template>
      <template v-else>
        <v-container class="my-10">
          <v-card
            class="mx-auto"
            max-width="400"
            v-ripple
            dark
            :class="`rounded-t-xl rounded-b-xl`"
          >
            <v-row justify="center" class="mb-0">
              <v-card-subtitle class="pt-10 pb-0 white--text font-weight-bold headline">
                代理店募集中！
              </v-card-subtitle>
            </v-row>

            <v-card-text class="white--text text-center subtitle-1">
              <div>あなたもオーナーになりませんか？</div>
            </v-card-text>

            <v-card-actions>
              <v-row justify="center" class="mb-2">
                <v-btn
                  color="white"
                  text
                  class="pa-5"
                >
                  もっと詳しく
                </v-btn>
              </v-row>
            </v-card-actions>

            <v-img
              class="white--text align-end"
              height="300px"
              src="@/assets/main_satei.jpeg" width="100%"
              :class="`rounded-b-xl`"
            >
            </v-img>
          </v-card>
        </v-container>
      </template>

      <v-row class="ma-1">
        <h2>店舗を検索</h2>
      </v-row>
      <template v-if="!$vuetify.breakpoint.xs">
        PC
      </template>
      <!-- sp -->
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
    </v-container>

    <!-- <vue-star animate="animated rubberBand" color="#F05654!">
      <a slot="icon" class="fa fa-heart" @click="handleClick"></a>
    </vue-star> -->
    <Footer />
    <div class="push"></div>
    <BottomNavi />
  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import Footer from '@/components/Footer.vue'
  import BottomNavi from '@/components/BottomNavi.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import api from '../services/api'
  // import Vue from 'vue'
  // import VueStar from 'vue-star'
  // Vue.component('VueStar', VueStar)

  export default {
    name: 'Home',
    data(){
      return {
        offers: '',
        shop_Info: [],
        headers: [
          {
            text: '',
            align: 'center',
            sortable: false,
            value: 'item_image',
          },
          { text: '車種', value: 'item_name', align: 'center' },
          { text: 'グレード', value: 'grade', align: 'center' },
          { text: '製造年', value: 'model_year', align: 'center' },
          { text: '走行距離', value: 'mileage', align: 'center' },
          { text: '査定店舗', value: 'assessed_store', align: 'center' },
          { text: '査定額', value: 'assessed_amount', align: 'center', filter: this.filters },
          { text: '写真', value: 'img', align: 'center', filter: 'center' },
        ],
        search: '',
        cars: [],
        offer_Items: [],
        assesment_price: [],
        prefectures: [
          {name: '東京', en: 'tokyo', img: require('../assets/tokyo.png')},
          {name: '神奈川', en: 'kanagawa', img: require('../assets/kanagawa.png')},
          {name: '埼玉', en: 'saitama', img: require('../assets/saitama.png')},
          {name: '千葉', en: 'chiba', img: require('../assets/chiba.png')},
          {name: '長野', en: 'nagano', img: require('../assets/chiba.png')},
          {name: '新潟', en: 'niigata', img: require('../assets/saitama.png')},
          {name: '山梨', en: 'yamanashi', img: require('../assets/kanagawa.png')},
          {name: '静岡', en: 'shizuoka', img: require('../assets/tokyo.png')},
        ]
      }
    },
    components: {
      Header,
      Footer,
      GlobalMenu,
      BottomNavi,
      // VueStar
    },
    filters: {
      priceLocaleString: function (value) {
          return value.toLocaleString()
      }
    },
    methods: {
      handleClick () {
        //do something
      }
      // chipColor(category) {
      //   if(category == '家電') {
      //     return 'yellow'
      //   }
      //   if(category == '家具') {
      //     return 'primary'
      //   }
      //   if(category == 'PC') {
      //     return 'black'
      //   }
      //   if(category == 'ファッション') {
      //     return 'orange'
      //   }
      //   if(category == '') {
      //     return 'black'
      //   }
      // },
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

      api({
        method: 'get',
        url: '/api/v1/api/client',
      })
      .then(response => this.shop_Info = response.data.results)
      .catch(error => console.log(error))
    },
  }
</script>

<style>
  ul li {
    display: inline-block;
    margin: 10px
  }
  #app .VueStar {
    position: relative;
  }
  .VueStar__icon .fa {
    font-size: 3em;
    cursor: pointer;
  }

  .push {
    height: 55px;/*フッターと同じ高さに指定*/
  }

  .tableshow_wrap {
    overflow-x: scroll;
    width: 100%;
  }

  .tableshow {
    width: 200vw;
    flex-wrap: wrap;
    display: flex;
  }

  .div1 {
    width: 12.5%;
  }
</style>