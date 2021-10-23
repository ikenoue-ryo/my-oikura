<template>
  <div>
    <TopNavi />
    あ
    <br>
    <br>
    <br>

    <v-container class="pa-8">
      <v-row>
        <v-col cols="8">
          <h2>こんにちは、{{profiles.nickname}} です</h2>
        </v-col>
        <v-col cols="4">
          <v-img :src="profiles.img" 
            width="70px" 
            height="70px" 
            class="mx-auto ma-5 rounded-circle"
          >
          </v-img>
        </v-col>
      </v-row>
      <v-divider></v-divider>

      <v-row class="mt-5">
        <v-col>
          <h3 class="my-3">査定結果 ({{assesment.length}}件)</h3>
          <div v-if="assesment">
            ご連絡頂きました査定依頼に、以下の店舗から査定結果が届いています。
            <template>
              <div
                class="mt-3"
                tile
              >
                <v-list flat>
                  <v-list-item-group
                    v-model="selectedItem"
                    color="primary"
                  >
                    <v-list-item
                      v-for="(assesment_info, i) in assesment"
                      :key="i"
                      class="pa-0"
                    >
                      <v-list-item-icon>
                        <v-img :src="assesment_info.client_shop.img" width="70" height="70" :class="`rounded-circle`"></v-img>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title v-text="assesment_info.client_shop.name"></v-list-item-title>
                        <v-list-item-subtitle>車種： {{assesment_info.offer.item_name}}</v-list-item-subtitle>
                        <v-list-item-subtitle>Price：{{assesment_info.value|priceLocaleString}} 円</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </div>
            </template>
          </div>
          <div v-else>
            まだ査定依頼を行っていません。
          </div>
        </v-col>
      </v-row>
      <v-divider></v-divider>
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
  // import CreateProfile from '@/components/CreateProfile.vue'
  import BottomNavi from '@/components/BottomNavi.vue'
  import api from '@/services/api'

  export default {
    name: 'Mypage',
    data() {
      return {
        mypage: '',
        profiles: [],
        assesment: [],
        scrollY: 0,
        isShow: true,
      }
    },
    components: {
      TopNavi,
      // CreateProfile,
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
        url: '/api/v1/auth/users/me/',
      })
      .then(response => this.mypage = response.data)
      .catch(error => console.log(error));

      api({
        method: 'get',
        url: '/profile/'
      })
      .then(response => this.profiles = response.data.results.find(profile => profile.user.id === this.id))
      .catch(error => console.log(error))

      api({
        method: 'get',
        url: '/api/v1/api/assesment_price/'
      })
      .then(response => this.assesment = response.data.results.filter(assesment => assesment.offer.profile.user.email === this.email))
      .catch(error => console.log(error))

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
.fade-enter-active, .fade-leave-active {
  will-change: opacity;
  transition: opacity 225ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.fade-enter, .fade-leave-to {
  opacity: 0
}
</style>