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

        <div v-if="profiles">
          <!-- {{user_profile}} -->
          <p>{{ user_profile.id }}</p>
          <p><img :src="user_profile.img" alt="" width="200"></p>
          <p>ニックネーム：{{ user_profile.nickname }}</p>
          <p>作成日：{{ user_profile.created_on }}</p>
          <p>Email：{{ user_profile.user.email }}</p>
          <p>ID：{{ user_profile.user.id }}</p>
          <p>username：{{ user_profile.user.name }}</p>
        </div>
        <div v-else>
          プロフィールを登録してください
        </div>
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
        profiles: []
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
      .then(response => {this.profiles = response.data})
      .catch(error => console.log(error));
    },
    computed: {
      username() {
        return this.$store.getters['auth/username']
      },
      isLoggedIn() {
        return this.$store.getters['auth/isLoggedIn']
      },
      user_profile() {
        const profiles = this.profiles.results.find(profiles => profiles.user.name === this.$route.params.username)
        return profiles;
      }
    }
  }
</script>

<style>

</style>