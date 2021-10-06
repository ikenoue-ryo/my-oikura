<template>
  <div>
    <p>高価買取・不要品買取の[おいくら] リサイクルショップや質屋の買取価格を見積り＆簡単比較！</p>
    <ul>
      <li><a href="/"><img src="https://oikura.jp/common/img/logo_oikura.svg" alt=""></a></li>
      <li>全国のリサイクルショップ・質屋  1,000件掲載></li>
    </ul>

    <p><a href="login">ログイン</a></p>
    <template>
      <div v-if="mypage">
        <p>ログイン中：ID:{{ mypage.id }} Email: {{ mypage.email }}</p>
      </div>
      <div v-else>
        ログインしてください
      </div>
    </template>
    
    <p><a href="#" @click="clickLogout">ログアウト</a></p>
    <!-- <p><a href="mypage">マイページ</a></p> -->
    <router-link :to="`/mypage/`">マイページ</router-link>
  
    <div class="text-right"><a href="/client/shop/">加盟店の方はこちら</a></div>
  
  </div>
</template>

<script>
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        mypage: '',
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