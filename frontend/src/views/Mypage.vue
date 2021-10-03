<template>
  <div>
    <Header />
    <GlobalMenu />
    <p v-if="isLoggedIn">ログインしています</p>
    <p v-else>ログインしてください</p>
      
      サインアップは<router-link to="/signup">こちら</router-link>
      <template>
        <p>Email: {{ mypage.email }}</p>
        <p>ID:{{ mypage.id }}</p>
      </template>
  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        mypage: '',
      }
    },
    components: {
      Header,
      GlobalMenu,
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
    },
  }
</script>

<style>

</style>