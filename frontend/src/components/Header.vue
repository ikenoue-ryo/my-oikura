<template>
  <div>
    <p>高価買取・不要品買取の[おいくら] リサイクルショップや質屋の買取価格を見積り＆簡単比較！</p>
    <ul>
      <li><a href="/"><img src="https://oikura.jp/common/img/logo_oikura.svg" alt=""></a></li>
      <li>全国のリサイクルショップ・質屋  1,000件掲載></li>
    </ul>

    <p><a href="login">ログイン</a></p>
    <p><a href="#" @click="clickLogout">ログアウト</a></p>
    <p><a href="mypage">マイページ</a></p>
    <p><a href="client">加盟店の方はこちら</a></p>
  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import axios from 'axios'
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {

      }
    },
    methods: {
      clickLogout() {
        this.$store.dispatch('auth/logout')
        this.$router.replace('/login')
      }
    },
  }
</script>