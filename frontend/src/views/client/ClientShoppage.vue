<template>
  <div>
    <ClientHeader />
    <ClientGlobalMenu />
    <h1>加盟店マイページ</h1>

    <p v-if="isLoggedIn">ログインしています</p>
    <p v-else>ログインしてください</p>
      
      サインアップは<router-link to="/signup">こちら</router-link>
      
      <template>
        <p>Email: {{ mypage.email }}</p>
        <p>ID:{{ mypage.id }}</p>
      </template>
      <!-- {{mypage.email}}

      {{shop_Info}} -->


    <h2>店舗情報</h2>
    <p>ID: {{ shop_infos.id }}</p>
    <p>店舗名: {{ shop_infos.name }}</p>
    <p>店舗名カナ: {{ shop_infos.kana }}</p>
    <p>店舗画像 <img :src="shop_infos.img" alt="" width=200></p>
    <p>担当者: {{ shop_infos.manager }}</p>
    <p>電話番号: {{ shop_infos.tel }}</p>
    <p>Email: {{ shop_infos.email }}</p>
    <p>所在地: {{ shop_infos.place }}</p>
    <p>作成日: {{ shop_infos.created_on }}</p>
    <p>営業時間</p>
    <p>買取方法</p>
  <br><br><br>

  <vue-star animate="animated rubberBand" color="#F05654">
        <a slot="icon" class="fa fa-heart" @click="handleClick"></a>
      </vue-star>

  </div>
</template>

<script>
  import ClientHeader from '@/components/client/ClientHeader.vue'
  import ClientGlobalMenu from '@/components/client/ClientGlobalMenu.vue'
  import api from '@/services/api'
  import Vue from 'vue'
  import VueStar from 'vue-star'
  Vue.component('VueStar', VueStar)

  export default {
    name: 'Home',
    data() {
      return {
        mypage: '',
        client: '',
        shop_Info: [],
        profiles: [],
      }
    },
    components: {
      ClientHeader,
      ClientGlobalMenu,
      VueStar
    },
    methods: {
      handleClick () {
        //do something
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
        url: '/api/v1/api/client/' + this.$route.params['id']
        // url: '/api/v1/api/client/1'
      })
      .then(response => this.shop_Info = response.data)
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
        const shop_info = this.shop_Info;
        return shop_info;
      }
    }
  }
</script>

<style>

</style>