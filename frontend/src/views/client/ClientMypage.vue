<template>
  <div>
    <v-img 
      :src="shop_infos.img" 
      width="100%" 
      class="mx-auto ma-0"
    >
      <v-icon @click="$router.back()" class="pa-4" size="30">mdi-arrow-left</v-icon>
    </v-img>

    <template>
      <v-col
        sm="6"
        offset-sm="3"
      >
        <v-list two-line>
          <template>
            <v-subheader>
              店舗情報
            </v-subheader>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-avatar>
                <v-icon size="30">mdi-store-outline</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-subtitle>店舗名</v-list-item-subtitle>
                <v-list-item-title>{{shop_infos.name}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-avatar>
                <v-icon size="30">mdi-account</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-subtitle>担当者</v-list-item-subtitle>
                <v-list-item-title>{{shop_infos.manager}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-avatar>
                <v-icon size="30">mdi-cellphone</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-subtitle>電話番号</v-list-item-subtitle>
                <v-list-item-title>{{shop_infos.tel}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-avatar>
                <v-icon size="30">mdi-email-outline</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-subtitle>Email</v-list-item-subtitle>
                <v-list-item-title>{{shop_infos.email}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-avatar>
                <v-icon size="30">mdi-map-marker-outline</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-subtitle>所在地</v-list-item-subtitle>
                <v-list-item-title>{{shop_infos.place}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-avatar>
                <v-icon size="30">mdi-pencil</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-subtitle>作成日</v-list-item-subtitle>
                <v-list-item-title>{{shop_infos.created_on}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-col>
    </template>

    <!-- {{shop_infos}} -->
    <div class="push"></div>
    <ClientBottomNavi />
  </div>
</template>

<script>
  import ClientBottomNavi from '@/components/client/ClientBottomNavi.vue'
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        mypage: '',
        client: '',
        shop_Info: [],
        profiles: [],

        items: [
          { header: '店舗情報' },
          { avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg', title: 'Brunch this weekend?', subtitle: `<span class="font-weight-bold">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?` },
          { divider: true, inset: true },
          { avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg', title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>', subtitle: `<span class="font-weight-bold">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.` },
          { divider: true, inset: true },
          { avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg', title: 'Oui oui', subtitle: '<span class="font-weight-bold">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?' },
        ],
      }
    },
    components: {
      ClientBottomNavi,
    },
    methods: {
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
        // url: '/api/v1/api/client/' + this.$route.params['userid']
        url: '/api/v1/api/client/'
      })
      .then(response => this.shop_Info = response.data.results)
      .catch(error => console.log(error))
    },
    computed: {
      email() {
        return this.$store.getters['auth/email']
      },
      // user_profile() {
      //   const profiles = this.profiles.results.find(profiles => profiles.user.email === this.email)
      //   return profiles;
      // }
      shop_infos() {
        const shop_info = this.shop_Info.find(shop_info => shop_info.user === this.mypage.id);
        return shop_info;
      }
    }
  }
</script>

<style>

</style>