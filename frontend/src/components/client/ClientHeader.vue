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
          <v-toolbar-title class="pa-1"><a href="/client/shop/" class="white--text">店舗ページ</a></v-toolbar-title>
          <v-spacer></v-spacer>
          
          <v-btn 
            icon
            fab
            @click="dialog = !dialog"
          >
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <v-card>
              <v-card-text>
                <v-text-field label="File name"></v-text-field>

                <small class="grey--text">* This doesn't actually save.</small>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn
                  text
                  color="primary"
                  @click="dialog = false"
                >
                  Submit
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

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

        dialog: false,
        
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
          { title: '加盟店マイページ', link: "/client/shop/", icon: "mdi-history"},
          { title: '査定依頼一覧', link: "/client/auction/", icon: "mdi-format-list-bulleted" },
          { title: '来店予約', link: "/client/visit-reservation/", icon: "mdi-heart-outline" },
          { title: '店舗PR', link: "/client/pr/", icon: "mdi-pencil-outline" },
          { title: '問い合わせ', link: "/client/contact/", icon: "mdi-chat-processing-outline" },
          { title: 'ユーザーページ', link: "/", icon: "mdi-arrow-left" },
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