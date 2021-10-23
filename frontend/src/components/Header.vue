<template>
  <div>
    <div
      v-for="(bar, i) in bars"
      :key="i"
    >
      <v-card
        color="grey lighten-4"
        flat
        tile
      >
        <v-toolbar
          :color="bar.class"
          :dark="bar.dark"
        >
          <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
          <v-toolbar-title class="pa-1"><a href="/" class="white--text">車査定</a></v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
          <div class="text-center">
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item
                  v-for="(item, index) in items"
                  :key="index"
                  :to="item.link"
                >
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
        </v-toolbar>

      </v-card>
    </div>

    <!-- <p><a href="login">ログイン</a></p>
    <template>
      <div v-if="mypage">
        <p>ログイン中：ID:{{ mypage.id }} Email: {{ mypage.email }}</p>
      </div>
      <div v-else>
        ログインしてください
      </div>
    </template>
    
    <p><a href="#" @click="clickLogout">ログアウト</a></p>
    <router-link :to="`/mypage/`">マイページ</router-link> -->

    <!-- <div class="text-right"><a href="/client/shop/">加盟店の方はこちら</a></div> -->
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
        class="pa-5"
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item
            v-for="(menu, index) in menus"
              :key="index"
              :to="menu.link"
          >
            <v-list-item-icon>
              <v-icon>{{menu.icon}}</v-icon>
            </v-list-item-icon>
            <v-list-item-title class="menu_title">{{menu.title}}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

  </div>
</template>

<script>
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        mypage: '',
        
        bars: [
          { class: '', dark: true },
        ],
        items: [
          { title: 'ログイン', link: "/login" },
          { title: 'マイページ', link: "/mypage" },
          { title: '店舗ページ', link: "/client/shop" },
          { title: 'ログアウト', link: "/logout" },
        ],
        menus: [
          { title: '査定依頼', link: "/offer-form", icon: "mdi-auto-fix"},
          { title: '店舗を探す', link: "/client-shop-search", icon: "mdi-magnify" },
          { title: '相場を見る', link: "/car-search", icon: "mdi-currency-usd" },
        ],
        
        drawer: false,
        group: null,
      }
    },
    methods: {
      clickLogout() {
        this.$store.dispatch('auth/logout')
        this.$router.replace('/login')
      }
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/auth/users/me/',
      })
      .then(response => this.mypage = response.data)
      .catch(error => console.log(error));
    },
  }
</script>

<style scorped>
  .menu_title {
    font-size: 1.0rem!important;
  }
</style>