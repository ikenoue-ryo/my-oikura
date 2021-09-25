<template>
  <div>
    <Header />
    <GlobalMenu />
    <p v-if="isLoggedIn">ログインしています</p>
    <p v-else>ログインしてください</p>
      <template>
        <p>Email: {{ mypage.email }}</p>
        <p>ID:{{ mypage.id }}</p>


        <p>ID: {{profiles.results[0].id}}</p>
        <p>{{profiles.results[0].nickname}}</p>
        <p>{{profiles.results[0].created_on}}</p>
        <p><img :src="profiles.results[0].img" alt=""></p>
        <p>{{profiles.results[0].id}}</p>

        <!-- <div v-for="profile in profiles" :key="profile.id">
          {{ profile.img }}
        </div> -->
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
        profiles: ''
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

      api({
        method: 'get',
        url: 'api/user/profile/',
      })
      .then(response => this.profiles = response.data)
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