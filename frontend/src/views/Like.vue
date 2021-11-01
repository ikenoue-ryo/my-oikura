<template>
  <div>
    <TopNavi />
    <br>
    <v-container class="pa-8">
      <v-row class="mb-2">
        <v-col cols="12">
          <h2 class="headline font-weight-bold">お気に入り</h2>
        </v-col>
      </v-row>

      <v-divider></v-divider>
<!-- {{like}} -->
      <v-row class="mt-5">
        <v-col>
          <div v-if="like">
            以下をお気に入りに登録しています。
            <!-- {{like}} -->
            <template>
              <div
                class="mt-3 row"
                tile
              >
                <v-list flat width="100%">
                  <v-list-item-group
                    v-model="selectedItem"
                    color="black"
                  >
                    <v-list-item
                      v-for="(favorite, i) in like"
                      :key="i"
                      class="pa-0"
                      :href="`/client/shop/${favorite.client_shop.id}/`"
                    >
                      <v-list-item-icon>
                        <v-img :src="favorite.client_shop.img" width="70" height="70" :class="`rounded-lg`"></v-img>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title class="font-weight-bold" v-text="favorite.client_shop.name"></v-list-item-title>
                      </v-list-item-content>
                      <vue-star animate="animated flash" color="#F05654!important">
                        <span slot="icon" class="fa fa-heart" @click.prevent></span>
                      </vue-star>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </div>
            </template>
          </div>
          <div v-else>
            お気に入りに登録しているものがありません
          </div>
        </v-col>
      </v-row>
      
      <div class="push"></div>
        <BottomNavi />
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
    コンテンツ
    <!-- <div>{{ assesment }}</div> -->
    <!-- <CreateProfile /> -->
    </v-container>


    <div class="push"></div>
    <transition name="fade">
      <BottomNavi v-show="isShow" />
    </transition>
  </div>
</template>

<script>
  import TopNavi from '@/components/TopNavi.vue'
  import BottomNavi from '@/components/BottomNavi.vue'
  // import CreateProfile from '@/components/CreateProfile.vue'
  import Vue from 'vue'
  import VueStar from 'vue-star'
  Vue.component('VueStar', VueStar)
  import api from '@/services/api'

  export default {
    name: 'Like',
    data() {
      return {
        like: '',
        profiles: [],
        assesment: [],
        scrollY: 0,
        isShow: true,
      }
    },
    components: {
      TopNavi,
      // CreateProfile,
      VueStar,
      BottomNavi,
    },
    filters: {
      priceLocaleString: function (value) {
          return value.toLocaleString()
      }
    },
    methods: {
      // スクロール値の取得
      onScroll () {
        this.$set(this, 'scrollY', window.pageYOffset)
      }
    },
    mounted(){
      api({
        method: 'get',
        url: '/like/',
      })
      .then(response => this.like = response.data.results.filter(like_profile => like_profile.profile.user.email === this.email))
      .catch(error => console.log(error));

      // スクロールイベントを取得
      window.addEventListener('scroll', this.onScroll)
      window.addEventListener('load', () => {
        this.onScroll()
      })
    },
    computed: {
      id() {
        return this.$store.getters['auth/id']
      },
      username() {
        return this.$store.getters['auth/username']
      },
      isLoggedIn() {
        return this.$store.getters['auth/isLoggedIn']
      },
      email() {
        return this.$store.getters['auth/email']
      },
      user_profile() {
        const profiles = this.profiles.results.find(profiles => profiles.client_shop.assesment_price === profiles.profile.user.id);
        return profiles;
      },
    },
    watch: {
      // 上にスクロールした時に表示
      scrollY (newValue, oldValue) {
        this.$set(this, 'isShow', newValue < oldValue)
      }
    },
  }
</script>

<style scoped>
  #app .VueStar {
    position: relative;
    right: 30px;
    bottom: 20px;
    width: 50px;
    height: 50px;
  }
  .VueStar__icon .fa {
    font-size: 2em;
    cursor: pointer;
  }
</style>