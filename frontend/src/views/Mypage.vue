<template>
  <div>
    <Header />
    <GlobalMenu />
    <p v-if="isLoggedIn">ログインしています{{mypage}}</p>
    <p v-else>ログインしてください</p>
      
      サインアップは<router-link to="/signup">こちら</router-link>
        <p>Email: {{ mypage.email }}</p>
        <p>ID:{{ mypage.id }}</p>

          <!-- <div>{{ assesment }}</div> -->
          <CreateProfile /><br><br>

            <div v-if="assesment">
            ご連絡頂きました査定依頼に、以下の店舗から査定結果が届いています。
            </div>
            <div v-else>
              まだ査定依頼を行っていません。
            </div>

            <div v-for="assesment_info in assesment" :key="assesment_info.item_name">
              <ul>
                <li><v-img :src="assesment_info.offer.image" width="100" max-height="100"></v-img></li>
                <li>{{assesment_info.offer.item_name}}</li>
              </ul>
            </div>
            <div v-for="assesment_info in assesment" :key="assesment_info.item_name">
              <ul>
                <li>{{assesment_info.client_shop.name}}</li>
                <li><v-img :src="assesment_info.client_shop.img" width="100" max-height="100"></v-img></li>
                <li>{{assesment_info.client_shop.manager}}</li>
                <li>{{assesment_info.client_shop.email}}</li>
                <li>{{assesment_info.client_shop.place}}</li>
                <li>{{assesment_info.value}}円</li>
              </ul>
            </div>
          


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
        profiles: [],
        assesment: [],
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

      api({
        method: 'get',
        url: '/api/v1/api/assesment_price/'
      })
      .then(response => this.assesment = response.data.results.filter(assesment => assesment.offer.profile.user.email === this.email))
      .catch(error => console.log(error))
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
        const profiles = this.profiles.results.find(profiles => profiles.client_shop.assesment_price === profiles.profile.user.id);
        return profiles;
      }
    }
  }
</script>

<style>

</style>