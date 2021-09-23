<template>
  <div>
    <Header />
    <GlobalMenu />
    <p v-if="isLoggedIn">ログインしています</p>
    <p v-else>ログインしてください</p>
      <template>
        <p>{{ mypage.email }}</p>
        <p>{{ mypage.id }}</p>
        <p>{{ mypage.username }}</p>
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
        mypage: ''
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
        url: '/auth/users/me/',
      })
      .then(response => this.mypage = response.data)
      .catch(error => console.log(error));
    },
    computed: {
      username() {
        return this.$store.getters['auth/username']
      },
      isLoggedIn() {
        return this.$store.getters['auth/isLoggedIn']
      },
    }
  }
</script>

<style>

</style>