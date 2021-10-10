<template>
  <div>
    <Header />
    <GlobalMenu />
    <p v-if="isLoggedIn">ログインしています{{mypage}}</p>
    <p v-else>ログインしてください</p>
      
      サインアップは<router-link to="/signup">こちら</router-link>
        <p>Email: {{ mypage.email }}</p>
        <p>ID:{{ mypage.id }}</p>
          <!-- <p>{{ user_profile}}</p> -->
          <CreateProfile />

  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import CreateProfile from '@/components/CreateProfile.vue'
  import api from '@/services/api'

  export default {
    name: 'Mypage',
    data() {
      return {
        mypage: '',
        profiles: []
      }
    },
    components: {
      Header,
      GlobalMenu,
      CreateProfile,
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
      email() {
        return this.$store.getters['auth/email']
      },
      user_profile() {
        const profiles = this.profiles.results.find(profiles => profiles.user.email === this.email)
        return profiles;
      }
    }
  }
</script>

<style>

</style>